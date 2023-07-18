import logging
import os
import json
import shutil

import asyncio

from typing import Callable, Optional
from collections import defaultdict
from datetime import datetime

import aioschedule
# import aioschedule
import requests
import vk_api
from aiogram import types, executor, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram.utils.deep_linking import decode_payload

from bot import dp, bot
from data.commands import getter, setter
from data.db_gino import db
from handlers import register_admin_handler, register_client_handler
from logger import init_logger
from markups.client_markup import ClientMarkup
from markups.admin_markup import AdminMarkup
from reply_process.main import (
    collect_post,
    process_queue,
    HANDLE_TYPES,
    queue_manager
)
from settings.config import KEYBOARD, ADMIN_ID

lock = asyncio.Lock()

init_logger('bot')
logger = logging.getLogger("bot.main")


@dp.message_handler(Command("start"))
async def main_menu(message: types.Message):
    client = await getter.client_select(message.from_user.id)
    binds = await getter.client_select_all_binds(message.from_user.id)
    limits = await getter.get_limits()

    link_id = None
    args = message.get_args()
    payload = decode_payload(args)
    if payload:
        link_id = int(payload)

    if not client:
        await bot.send_message(message.from_user.id,
                               "Привет, рады видеть тебя в боте!\n"
                               "Для начала, давай немного расскажу про то, что он умеет:\n\n"
                               "SMPoster позволяет запустить дополнительный источник подписчиков "
                               "для ваших тг-каналов или создать дополнительный источник дохода."
                               "SMPoster – это бот, который автоматически берет посты из ваших "
                               "тг-каналов и постит их в ВК.\n\n"
                               "<b>Если подробнее:</b>\n"
                               "✧ настройка нескольких связок между тг и вк, которые будут работать параллельно;\n"
                               "✧ привязка к одному тг-каналу нескольких групп вк "
                               "и к одной группе вк несколько тг-каналов;\n"
                               "✧ возможность сокращать посты до определённого количества символов "
                               "(чтобы за полным текстом переходили в ТГ);\n"
                               "✧ возможность исключать посты с определёнными хэштегами (например #реклама);\n"
                               "✧ возможность добавлять дополнительные хэштеги;\n"
                               "✧ возможность добавлять прямую ссылку на пост;\n"
                               "✧ возможность добавлять текст после поста, например добавлять UTM-ссылку на канал;\n"
                               "✧ постинг любого типа контента (текст, видео, картинки, музыка и т.д.);\n\n"
                               f"Стоимость: {limits.standard_pay} рублей/месяц, куда входит 5 связок TG - VK, "
                               f"если требуется больше, каждая дополнительная связка стоит {limits.add_pay} р."
                               "Это минимум в 10 раз дешевле, чем если это делает сотрудник.\n\n"
                               "Бонус – 7 дней пробного периода, с момента, как вы настроите первую связку.\n\n"
                               "Для помощи с настройкой или для обратной связи пишите сюда – @egormk",
                               reply_markup=ClientMarkup.client_start(link_id))
    else:
        if client.block:
            await bot.send_message(message.from_user.id,
                                   "<b>Вы заблокированы!</b>\n\n"
                                   "По всем вопросам @egormk")
        else:
            if client.access:
                await bot.send_message(message.from_user.id,
                                       "<b>Меню автопостинга</b>\n\n"
                                       "Связь – это связка вашего Telegram-канала и группы/паблика VK\n"
                                       "- к одной группе/паблику VK может быть привязано несколько Telegram-каналов\n"
                                       "- к нескольким группам/пабликам VK может быть привязан один Telegram-канал (можете настроить любую "
                                       "логику распределения контента)\n\n"
                                       "Техническая поддержка и дополнительные материалы – https://t.me/smposter_support\n\n"
                                       f"<b>{KEYBOARD.get('CHECK_MARK_BUTTON')} Ваша подписка активна!</b>\n"
                                       f"<b>{KEYBOARD.get('STOPWATCH')} Подписка заканчивается</b> - "
                                       f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n\n"
                                       f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - "
                                       f"<i>{len(binds)}/{client.limit_binds}</i>\n",
                                       reply_markup=ClientMarkup.client_main())
            elif client.subscribe_type == "start":
                await bot.send_message(message.from_user.id,
                                       "<b>Меню автопостинга</b>\n\n"
                                       "Связь – это связка вашего Telegram-канала и группы/паблика VK\n"
                                       "- к одной группе/паблику VK может быть привязано несколько Telegram-каналов\n"
                                       "- к нескольким группам/пабликам VK может быть привязан один Telegram-канал (можете настроить любую "
                                       "логику распределения контента)\n\n"
                                       "Мы дарим 7 дней бесплатного периода, всем, кто подключился!\n"
                                       "Для активации откройте раздел 'Подписка' и затем 'Промо подписка'\n\n"
                                       "Техническая поддержка и дополнительные материалы – https://t.me/smposter_support\n\n"
                                       f"<b>{KEYBOARD.get('CROSS_MARK')} Ваша подписка неактивна!</b>\n\n"
                                       f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - "
                                       f"<i>{len(binds)}/{client.limit_binds}</i>\n",
                                       disable_web_page_preview=True,
                                       reply_markup=ClientMarkup.client_main())
            else:
                await bot.send_message(message.from_user.id,
                                       "<b>Меню автопостинга</b>\n\n"
                                       "Связь – это связка вашего Telegram-канала и группы/паблика VK\n"
                                       "- к одной группе/паблику VK может быть привязано несколько Telegram-каналов\n"
                                       "- к нескольким группам/пабликам VK может быть привязан один Telegram-канал (можете настроить любую "
                                       "логику распределения контента)\n\n"
                                       "Техническая поддержка и дополнительные материалы – https://t.me/smposter_support\n\n"
                                       f"<b>{KEYBOARD.get('CROSS_MARK')} Ваша подписка неактивна!</b>\n"
                                       f"<b>{KEYBOARD.get('STOPWATCH')} Подписка закончилась</b> - "
                                       f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n\n"
                                       f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - "
                                       f"<i>{len(binds)}/{client.limit_binds}</i>\n",
                                       reply_markup=ClientMarkup.client_main())


@dp.message_handler(Command("admin"), state=["*"])
async def admin(message: types.Message, state: FSMContext):
    await state.finish()
    admins = await getter.admin_select_all()
    if str(message.from_user.id) in ADMIN_ID:
        admin_ = await getter.admin_select(message.from_user.id)
        if not admin_:
            await setter.admin_add(message.from_user.id,
                                   message.from_user.username)
        await bot.send_message(message.from_user.id,
                               "<b>Добро пожаловать в меню Администратора</b>\n\n"
                               "<b>Вы можете просмотреть cписок пользователей, "
                               "список связей, найти пользователя, изменения лимитов.</b>\n\n",
                               reply_markup=AdminMarkup.admin_menu())
    else:
        for i in admins:
            if i.user_id == message.from_user.id:
                await bot.send_message(message.from_user.id,
                                       "<b>Добро пожаловать в меню Администратора</b>\n\n"
                                       "<b>Вы можете просмотреть cписок пользователей, "
                                       "список связей, найти пользователя, изменения лимитов.</b>\n\n",
                                       reply_markup=AdminMarkup.admin_menu())
                break
        else:
            await bot.send_message(message.from_user.id, "У вас нет прав доступа!")


# async def send_to_vk(tg_chat_id):
#     bind = await getter.client_select_bind_with_tg_channel_id(str(tg_chat_id))
#     owner = await getter.client_select(bind.owner_id)
#     vk = vk_api.VkApi(token=owner.vk_token, api_version="5.131")
#     for vk_group_id in bind.vk_groups_ids:
#         attachments = []
#         if os.path.exists(f"files/{bind.owner_id}/{tg_chat_id}/photos"):
#             for photo in os.listdir(f"files/{bind.owner_id}/{tg_chat_id}/photos"):
#                 result = vk.method('photos.getWallUploadServer', {'group_id': vk_group_id})
#                 with open(f'files/{bind.owner_id}/{tg_chat_id}/photos/{photo}', 'rb') as file:
#                     response = requests.post(result['upload_url'], files={'photo': file})
#                 result = json.loads(response.text)
#                 result = vk.method('photos.saveWallPhoto',
#                                    {'photo': result['photo'], 'hash': result['hash'], 'server': result['server'],
#                                     'group_id': vk_group_id})
#                 attachments.append(f'photo{result[0]["owner_id"]}_{result[0]["id"]}')
#         if os.path.exists(f"files/{bind.owner_id}/{tg_chat_id}/videos"):
#             for video in os.listdir(f"files/{bind.owner_id}/{tg_chat_id}/videos"):
#                 try:
#                     result = vk.method('video.save', {'group_id': vk_group_id})
#                 except Exception as ex:
#                     print(f"Не удалось сохранить Видео пользователь - {bind.owner_id}\n"
#                           f"Ошибка - {ex}")
#                 else:
#                     with open(f'files/{bind.owner_id}/{tg_chat_id}/videos/{video}', 'rb') as file:
#                         response = requests.post(result['upload_url'], files={'video': file})
#                     result = json.loads(response.text)
#                     attachments.append(f'video{result["owner_id"]}_{result["video_id"]}')
#         attachments = ','.join(attachments)
#         message = ""
#         if os.path.exists(f"files/{bind.owner_id}/{tg_chat_id}/text.txt"):
#             with open(f"files/{bind.owner_id}/{tg_chat_id}/text.txt", "r") as file_text:
#                 message = file_text.read()
#         vk.method('wall.post',
#                   {'owner_id': -int(vk_group_id),
#                    'message': message,
#                    'from_group': 1,
#                    'attachments': attachments})


#     print(f"Файлы загружены! для {tg_chat_id}", datetime.now())
#     await asyncio.sleep(30)
#     shutil.rmtree(f'files/{bind.owner_id}/{tg_chat_id}')
#     print(f"Файлы {tg_chat_id} удалены!", datetime.now())


# async def check_tg_channels():
#     clients = await getter.all_clients()
#     for i in clients:
#         if str(i.user_id) in os.listdir("files"):
#             if os.listdir(f"files/{str(i.user_id)}"):
#                 for tg_chat_id in os.listdir(f"files/{str(i.user_id)}"):
#                     print("Запускаю на отправку в ВК")
#                     await send_to_vk(str(tg_chat_id))


@dp.channel_post_handler(content_types=HANDLE_TYPES)
async def message_collector(message: types.Message):
    collected_item = await collect_post(message)
    dp = Dispatcher.get_current()
    await process_queue(collected_item, dp.queue, message.message_id)


# @dp.channel_post_handler(content_types=['text', 'audio', 'document', 'photo', 'video', 'animation'])
# async def check_tg_channel(message: types.Message):
#     async with lock:
#         media_group = None
#         if message.media_group_id:
#             bind = await getter.client_select_bind_with_tg_channel_id(str(message.chat.id))
#             client = await getter.client_select(bind.owner_id)
#             if bind.on and client.access:
#                 media_group = await getter.get_post_with_media_group(message.media_group_id)
#                 if media_group:
#                     await setter.bot_set_media_group_id_new_count(message.media_group_id)
#                 else:
#                     await setter.bot_new_media_group_id(bind.owner_id,
#                                                         message.chat.title,
#                                                         str(message.chat.id),
#                                                         str(message.media_group_id))
#     async with lock:
#         bind = await getter.client_select_bind_with_tg_channel_id(str(message.chat.id))
#         client = await getter.client_select(bind.owner_id)
#         if bind.on and client.access:
#             owner = await getter.client_select(bind.owner_id)
#             try:
#                 msg = message.text if message.text else message.caption
#                 excl_tags = bind.excl_tags
#                 cont = True
#                 if excl_tags:
#                     excl_tags = excl_tags.split()
#                     for i in excl_tags:
#                         if i in msg:
#                             cont = False
#                             break
#                 if cont:
#                     for vk_group_id in bind.vk_groups_ids:
#                         if message.text:
#                             result_text = message.text
#                             url = message.link("", as_html=False).split(']')
#                             if message.entities:
#                                 a = 0
#                                 result_text = list(result_text)
#                                 for i in message.entities:
#                                     if i.url:
#                                         ind = i.offset + a + i.length
#                                         result_text.insert(ind, f" {i.url}")
#                                         a += 1
#                                     if i.type == "mention":
#                                         ind = i.offset + a
#                                         result_text.insert(ind, f"t.me/")
#                                         result_text.pop(ind + 1)
#                                 result_text = "".join(result_text)
#                             if bind.qty:
#                                 a = message.link("\nЧитать далее", as_html=False).split(']')
#                                 result_text = f"{result_text[:bind.qty]}...\n{a[0][1:]} - {a[1][1:-1]}"
#                             if bind.opt_text:
#                                 result_text = f"{result_text}\n\n" \
#                                               f"{bind.opt_text}"
#                             if bind.url:
#                                 result_text = f"{result_text}\n\n" \
#                                               f"Подробнее: {url[1][1:-1]}"
#                             if bind.tags:
#                                 result_text = f"{result_text}\n\n" \
#                                               f"{bind.tags}"
#                             requests.post(url="https://api.vk.com/method/wall.post",
#                                           params={
#                                               "access_token": owner.vk_token,
#                                               "from_group": 1,
#                                               "owner_id": -int(vk_group_id),
#                                               "message": f"{result_text}",
#                                               "v": "5.131"})
#                     if message.photo:
#                         if message.caption:
#                             try:
#                                 os.makedirs(f"files/{bind.owner_id}/{message.chat.id}")
#                             except FileExistsError:
#                                 pass
#                             with open(f"files/{bind.owner_id}/{message.chat.id}/text.txt", "w") as file:
#                                 result_text = message.caption
#                                 url = message.link("", as_html=False).split(']')
#                                 if message.caption_entities:
#                                     a = 0
#                                     result_text = list(result_text)
#                                     for i in message.caption_entities:
#                                         if i.url:
#                                             ind = i.offset + a + i.length
#                                             result_text.insert(ind, f" {i.url}")
#                                             a += 1
#                                         if i.type == "mention":
#                                             ind = i.offset + a
#                                             result_text.insert(ind, f"t.me/")
#                                             result_text.pop(ind + 1)
#                                     result_text = "".join(result_text)
#                                 if bind.qty:
#                                     a = message.link("\nЧитать далее", as_html=False).split(']')
#                                     result_text = f"{result_text[:bind.qty]}...\n{a[0][1:]} - {a[1][1:-1]}"
#                                 if bind.opt_text:
#                                     result_text = f"{result_text}\n\n" \
#                                                   f"{bind.opt_text}"
#                                 if bind.url:
#                                     result_text = f"{result_text}\n\n" \
#                                                   f"Подробнее: {url[1][1:-1]}"
#                                 if bind.tags:
#                                     result_text = f"{result_text}\n\n" \
#                                                   f"{bind.tags}"
#                                 file.write(result_text)
#                         await message.photo[-1] \
#                             .download(destination_file=f"files/{bind.owner_id}/{message.chat.id}/"
#                                                        f"photos/{message.photo[-1].file_unique_id}.jpg")
#                         print("ФОТО", datetime.now())
#                         if message.media_group_id:
#                             await setter.bot_set_media_group_id_decrease_count(message.media_group_id)
#                     if message.video:
#                         if message.caption:
#                             try:
#                                 os.makedirs(f"files/{bind.owner_id}/{message.chat.id}")
#                             except FileExistsError:
#                                 pass
#                             with open(f"files/{bind.owner_id}/{message.chat.id}/text.txt", "w") as file:
#                                 result_text = message.caption
#                                 url = message.link("", as_html=False).split(']')
#                                 if message.caption_entities:
#                                     a = 0
#                                     result_text = list(result_text)
#                                     for i in message.caption_entities:
#                                         if i.url:
#                                             ind = i.offset + a + i.length
#                                             result_text.insert(ind, f" {i.url}")
#                                             a += 1
#                                         if i.type == "mention":
#                                             ind = i.offset + a
#                                             result_text.insert(ind, f"t.me/")
#                                             result_text.pop(ind + 1)
#                                     result_text = "".join(result_text)
#                                 if bind.qty:
#                                     a = message.link("\nЧитать далее", as_html=False).split(']')
#                                     result_text = f"{result_text[:bind.qty]}...\n{a[0][1:]} - {a[1][1:-1]}"
#                                 if bind.opt_text:
#                                     result_text = f"{result_text}\n\n" \
#                                                   f"{bind.opt_text}"
#                                 if bind.url:
#                                     result_text = f"{result_text}\n\n" \
#                                                   f"Подробнее: {url[1][1:-1]}"
#                                 if bind.tags:
#                                     result_text = f"{result_text}\n\n" \
#                                                   f"{bind.tags}"
#                                 file.write(result_text)
#                         await message.video \
#                             .download(destination_file=f"files/{bind.owner_id}/{message.chat.id}/"
#                                                        f"videos/{message.video.file_unique_id}.mp4")
#                         print("ВИДЕО", datetime.now())
#                         if message.media_group_id:
#                             await setter.bot_set_media_group_id_decrease_count(message.media_group_id)
#             except AttributeError as attr:
#                 print(f"Бот является Администратором ТГ канала\n"
#                       f"ID - {message.chat.id}\n"
#                       f"Название - {message.chat.title}\n"
#                       f"Но данный ТГ канал отсутствует в базе данных!\n"
#                       f"Ошибка - {attr}")
#             media_group = await getter.get_post_with_media_group(message.media_group_id)
#     async with lock:
#         if media_group:
#             if media_group.count_files == 0:
#                 await check_tg_channels()
#         else:
#             await check_tg_channels()


async def check_subscribe():
    clients = await getter.check_subscribe()
    for client in clients:
        if client.subscribe <= datetime.now():
            subscribe_type = client.subscribe_type
            if subscribe_type == 'promo':
                subscribe_type = 'dropout'
            elif subscribe_type == 'paid':
                subscribe_type = 'after payment'
            await client.update(access=False, subscribe_type=subscribe_type).apply()


async def notifications():
    clients = await getter.check_subscribe()
    for client in clients:
        res = client.subscribe - datetime.now()
        try:
            message = await bot.send_message(client.user_id, '.', disable_notification=True)
            await bot.delete_message(client.user_id, message.message_id)
        except:
            await client.update(subscribe_type='blocked').apply()
        try:
            if res.days == 3:
                await bot.send_message(client.user_id,
                                       f"<i>Ваша подписка закончится через <b>3 дня</b>, "
                                       "оплатите, чтобы постинг не остановился</i>\n\n"
                                       "Пройдите в меню 'Подписка' и нажмите кнопку "
                                       "'Оплатить +1 месяц'")
            if res.days == 1:
                await bot.send_message(client.user_id,
                                       f"<i>Ваша подписка закончится через <b>1 день</b>, "
                                       "оплатите, чтобы постинг не остановился</i>\n\n"
                                       "Пройдите в меню 'Подписка' и нажмите кнопку "
                                       "'Оплатить +1 месяц'")
            if res.days == -1:
                await bot.send_message(client.user_id,
                                       f"<i>Ваша подписка</i> <b>закончилась!</b>\n\n"
                                       "Пройдите в меню 'Подписка' и нажмите кнопку "
                                       "'Оплатить +1 месяц'")
            if res.days % 3 == 0:
                await bot.send_message(client.user_id,
                                 f"Видел, что ваша подписка закончилась и вы решили ее не продлевать😞\n\n"
                                 f"Поделитесь своим опытом, использования нашего сервиса: @egormk\n"
                                 f"А с нас бонус😉")
        except:
            pass


async def scheduler(func: Callable, sleep_time, wait_for_start: Optional[int] = None):
    if wait_for_start:
        await asyncio.sleep(wait_for_start)
    while 1:
        try:
            await func()
        except Exception as ex:
            print(ex)

        await asyncio.sleep(sleep_time)


# async def scheduler():
#     aioschedule.every().day.do(notifications)
#     aioschedule.every().minute.do(check_subscribe)
#
#     while True:
#         await aioschedule.run_pending()
#         await asyncio.sleep(1)


async def on_startup(_):
    from data import db_gino
    await db_gino.on_startup(dp)
    print("Database connected")

    asyncio.create_task(scheduler(notifications, 60 * 60 * 24, wait_for_start=60 * 60))
    asyncio.create_task(scheduler(check_subscribe, 60 * 60))
    print("Scheduler running")

    """Создание БД"""
    await db_gino.db.gino.create_all()
    await setter.create_limits()

    """Регистрация хэндлеров"""
    register_admin_handler(dp)
    register_client_handler(dp)
    print("Handlers registered")

    """Регистрация команд"""
    await dp.bot.set_my_commands([types.BotCommand('start', 'Запустить бота')])
    print("Commands registered")

    """Очередь постов"""
    dp.queue = defaultdict(list)
    asyncio.create_task(queue_manager())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
