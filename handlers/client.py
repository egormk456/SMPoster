from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import LabeledPrice, PreCheckoutQuery

from bot import bot
from markups.client_markup import ClientMarkup
from data.commands import getter, setter
from states import states
from settings.config import KEYBOARD, PAY_TOKEN


class ClientMain:

    @staticmethod
    async def client_start(callback: types.CallbackQuery):
        await setter.client_add(callback.from_user.id,
                                callback.from_user.username)
        client = await getter.client_select(callback.from_user.id)
        binds = await getter.client_select_all_binds(callback.from_user.id)

        callback_data = callback.data.split(':')
        if len(callback_data) == 2:
            link_id = int(callback_data[-1])
            await setter.update_client_invite_link_id(callback.from_user.id, link_id)

        if client.access:
            await callback.message.edit_text(
                "<b>Меню автопостинга</b>\n\n"
                "Связь – это связка вашего Telegram-канала и группы/паблика VK\n"
                "- к одной группе/паблику VK может быть привязано несколько Telegram-каналов\n"
                "- к нескольким группам/пабликам VK может быть привязан один Telegram-канал (можете настроить любую логику распределения контента)\n\n"
                "Мы дарим 7 дней бесплатного периода, всем, кто подключился! Для активации откройте раздел \"Подписка\" и затем \"Промо подписка\"\n\n"
                "Техническая поддержка и дополнительные материалы – https://t.me/smposter_support\n\n"
                f"<b>{KEYBOARD.get('CHECK_MARK_BUTTON')} Ваша подписка активна!</b>\n"
                f"<b>{KEYBOARD.get('STOPWATCH')} Подписка заканчивается</b> - "
                f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n\n"
                f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - "
                f"<i>{len(binds)}/{client.limit_binds}</i>\n",
                disable_web_page_preview=True,
                reply_markup=ClientMarkup.client_main())
        elif client.subscribe_type == "start":
            await callback.message.edit_text(
                "<b>Меню автопостинга</b>\n\n"
                "Связь – это связка вашего Telegram-канала и группы/паблика VK\n"
                "- к одной группе/паблику VK может быть привязано несколько Telegram-каналов\n"
                "- к нескольким группам/пабликам VK может быть привязан один Telegram-канал (можете настроить любую логику распределения контента)\n\n"
                "Мы дарим 7 дней бесплатного периода, всем, кто подключился! Для активации откройте раздел \"Подписка\" и затем \"Промо подписка\"\n\n"
                "Техническая поддержка и дополнительные материалы – https://t.me/smposter_support\n\n"
                f"<b>{KEYBOARD.get('CROSS_MARK')} Ваша подписка неактивна!</b>\n\n"
                f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - "
                f"<i>{len(binds)}/{client.limit_binds}</i>\n",
                disable_web_page_preview=True,
                reply_markup=ClientMarkup.client_main())
        else:
            await callback.message.edit_text(
                "<b>Меню автопостинга</b>\n\n"
                "Связь – это связка вашего Telegram-канала и группы/паблика VK\n"
                "- к одной группе/паблику VK может быть привязано несколько Telegram-каналов\n"
                "- к нескольким группам/пабликам VK может быть привязан один Telegram-канал (можете настроить любую логику распределения контента)\n\n"
                "Мы дарим 7 дней бесплатного периода, всем, кто подключился! Для активации откройте раздел \"Подписка\" и затем \"Промо подписка\"\n\n"
                "Техническая поддержка и дополнительные материалы – https://t.me/smposter_support\n\n"
                f"<b>{KEYBOARD.get('CROSS_MARK')} Ваша подписка неактивна!</b>\n\n"
                f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - "
                f"<i>{len(binds)}/{client.limit_binds}</i>\n",
                disable_web_page_preview=True,
                reply_markup=ClientMarkup.client_main())

    @staticmethod
    async def client_main(callback: types.CallbackQuery, state: FSMContext):
        client = await getter.client_select(callback.from_user.id)
        binds = await getter.client_select_all_binds(callback.from_user.id)
        try:
            if client.access:
                await callback.message.edit_text(
                    "<b>Меню автопостинга</b>\n\n"
                    "Связь – это связка вашего Telegram-канала и группы/паблика VK\n"
                    "- к одной группе/паблику VK может быть привязано несколько Telegram-каналов\n"
                    "- к нескольким группам/пабликам VK может быть привязан один Telegram-канал (можете настроить любую логику распределения контента)\n\n"
                    "Мы дарим 7 дней бесплатного периода, всем, кто подключился! Для активации откройте раздел \"Подписка\" и затем \"Промо подписка\"\n\n"
                    "Техническая поддержка и дополнительные материалы – https://t.me/smposter_support\n\n"
                    f"<b>{KEYBOARD.get('CHECK_MARK_BUTTON')} Ваша подписка активна!</b>\n"
                    f"<b>{KEYBOARD.get('STOPWATCH')} Подписка заканчивается</b> - "
                    f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n\n"
                    f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - "
                    f"<i>{len(binds)}/{client.limit_binds}</i>\n",
                    disable_web_page_preview=True,
                    reply_markup=ClientMarkup.client_main())
            elif client.subscribe_type == "start":
                await callback.message.edit_text(
                    "<b>Меню автопостинга</b>\n\n"
                    "Связь – это связка вашего Telegram-канала и группы/паблика VK\n"
                    "- к одной группе/паблику VK может быть привязано несколько Telegram-каналов\n"
                    "- к нескольким группам/пабликам VK может быть привязан один Telegram-канал (можете настроить любую логику распределения контента)\n\n"
                    "Мы дарим 7 дней бесплатного периода, всем, кто подключился! Для активации откройте раздел \"Подписка\" и затем \"Промо подписка\"\n\n"
                    "Техническая поддержка и дополнительные материалы – https://t.me/smposter_support\n\n"
                    f"<b>{KEYBOARD.get('CROSS_MARK')} Ваша подписка неактивна!</b>\n\n"
                    f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - "
                    f"<i>{len(binds)}/{client.limit_binds}</i>\n",
                    disable_web_page_preview=True,
                    reply_markup=ClientMarkup.client_main())
            else:
                await callback.message.edit_text(
                    "<b>Меню автопостинга</b>\n\n"
                    "Связь – это связка вашего Telegram-канала и группы/паблика VK\n"
                    "- к одной группе/паблику VK может быть привязано несколько Telegram-каналов\n"
                    "- к нескольким группам/пабликам VK может быть привязан один Telegram-канал (можете настроить любую логику распределения контента)\n\n"
                    "Мы дарим 7 дней бесплатного периода, всем, кто подключился! Для активации откройте раздел \"Подписка\" и затем \"Промо подписка\"\n\n"
                    "Техническая поддержка и дополнительные материалы – https://t.me/smposter_support\n\n"
                    f"<b>{KEYBOARD.get('CROSS_MARK')} Ваша подписка неактивна!</b>\n"
                    f"<b>{KEYBOARD.get('STOPWATCH')} Подписка закончилась</b> - "
                    f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n\n"
                    f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - "
                    f"<i>{len(binds)}/{client.limit_binds}</i>\n",
                    disable_web_page_preview=True,
                    reply_markup=ClientMarkup.client_main())
        except Exception as ex:
            await bot.delete_message(callback.from_user.id, callback.message.message_id)
            if client.access:
                await bot.send_message(callback.from_user.id,
                                        "<b>Меню автопостинга</b>\n\n"
                                        "Связь – это связка вашего Telegram-канала и группы/паблика VK\n"
                                        "- к одной группе/паблику VK может быть привязано несколько Telegram-каналов\n"
                                        "- к нескольким группам/пабликам VK может быть привязан один Telegram-канал (можете настроить любую логику распределения контента)\n\n"
                                        "Мы дарим 7 дней бесплатного периода, всем, кто подключился! Для активации откройте раздел \"Подписка\" и затем \"Промо подписка\"\n\n"
                                        "Техническая поддержка и дополнительные материалы – https://t.me/smposter_support\n\n"
                                        f"<b>{KEYBOARD.get('CHECK_MARK_BUTTON')} Ваша подписка активна!</b>\n"
                                        f"<b>{KEYBOARD.get('STOPWATCH')} Подписка заканчивается</b> - "
                                        f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n\n"
                                        f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - "
                                        f"<i>{len(binds)}/{client.limit_binds}</i>\n",
                                        disable_web_page_preview=True,
                                        reply_markup=ClientMarkup.client_main())
            else:
                await bot.send_message(callback.from_user.id,
                                        "<b>Меню автопостинга</b>\n\n"
                                        "Связь – это связка вашего Telegram-канала и группы/паблика VK\n"
                                        "- к одной группе/паблику VK может быть привязано несколько Telegram-каналов\n"
                                        "- к нескольким группам/пабликам VK может быть привязан один Telegram-канал (можете настроить любую логику распределения контента)\n\n"
                                        "Мы дарим 7 дней бесплатного периода, всем, кто подключился! Для активации откройте раздел \"Подписка\" и затем \"Промо подписка\"\n\n"
                                        "Техническая поддержка и дополнительные материалы – https://t.me/smposter_support\n\n"
                                        f"<b>{KEYBOARD.get('CROSS_MARK')} Ваша подписка неактивна!</b>\n"
                                        f"<b>{KEYBOARD.get('STOPWATCH')} Подписка закончилась</b> - "
                                        f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n\n"
                                        f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - "
                                        f"<i>{len(binds)}/{client.limit_binds}</i>\n",
                                        disable_web_page_preview=True,
                                        reply_markup=ClientMarkup.client_main())
        await state.finish()

    @staticmethod
    async def client_main_menu_with_caption(callback: types.CallbackQuery, state: FSMContext):
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
        client = await getter.client_select(callback.from_user.id)
        binds = await getter.client_select_all_binds(callback.from_user.id)
        if client.access:
            await bot.send_message(callback.from_user.id,
                                    "<b>Меню автопостинга</b>\n\n"
                                    "Связь – это связка вашего Telegram-канала и группы/паблика VK\n"
                                    "- к одной группе/паблику VK может быть привязано несколько Telegram-каналов\n"
                                    "- к нескольким группам/пабликам VK может быть привязан один Telegram-канал (можете настроить любую логику распределения контента)\n\n"
                                    "Мы дарим 7 дней бесплатного периода, всем, кто подключился! Для активации откройте раздел \"Подписка\" и затем \"Промо подписка\"\n\n"
                                    "Техническая поддержка и дополнительные материалы – https://t.me/smposter_support\n\n"
                                    f"<b>{KEYBOARD.get('CHECK_MARK_BUTTON')} Ваша подписка активна!</b>\n"
                                    f"<b>{KEYBOARD.get('STOPWATCH')} Подписка заканчивается</b> - "
                                    f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n\n"
                                    f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - "
                                    f"<i>{len(binds)}/{client.limit_binds}</i>\n",
                                    disable_web_page_preview=True,
                                    reply_markup=ClientMarkup.client_main())
        else:
            await bot.send_message(callback.from_user.id,
                                    "<b>Меню автопостинга</b>\n\n"
                                    "Связь – это связка вашего Telegram-канала и группы/паблика VK\n"
                                    "- к одной группе/паблику VK может быть привязано несколько Telegram-каналов\n"
                                    "- к нескольким группам/пабликам VK может быть привязан один Telegram-канал (можете настроить любую логику распределения контента)\n\n"
                                    "Мы дарим 7 дней бесплатного периода, всем, кто подключился! Для активации откройте раздел \"Подписка\" и затем \"Промо подписка\"\n\n"
                                    "Техническая поддержка и дополнительные материалы – https://t.me/smposter_support\n\n"
                                    f"<b>{KEYBOARD.get('CROSS_MARK')} Ваша подписка неактивна!</b>\n"
                                    f"<b>{KEYBOARD.get('STOPWATCH')} Подписка закончилась</b> - "
                                    f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n\n"
                                    f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - "
                                    f"<i>{len(binds)}/{client.limit_binds}</i>\n",
                                    disable_web_page_preview=True,
                                    reply_markup=ClientMarkup.client_main())
        await state.finish()

    @staticmethod
    async def client_need_support(callback: types.CallbackQuery):
        await callback.message.edit_text("<i>Поддержка</i>\n\n"
                                         "<i>По всем вопросам обращаться к</i> <b>@egormk</b>",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_back_main_menu())

    @staticmethod
    async def client_add_new_vk_token(message: types.Message):
        if message.text:
            a = message.text.find("=")
            b = message.text.find("&")
            if a == -1 or b == -1:
                await bot.delete_message(message.from_user.id, message.message_id)
                await bot.delete_message(message.from_user.id, message.message_id - 1)
                await bot.send_message(message.from_user.id,
                                       "<b>Надо скопировать всю ссылку и послать мне</b>\n\n"
                                       "<i>Или можете вернуться в главное меню</i>",
                                       disable_web_page_preview=True,
                                       reply_markup=ClientMarkup.client_back_main_menu())
            else:
                vk_token = message.text[a + 1:b]
                await setter.client_add_vk_token(message.from_user.id, vk_token)
                await bot.delete_message(message.from_user.id, message.message_id)
                await bot.delete_message(message.from_user.id, message.message_id - 1)
                await bot.send_photo(message.from_user.id,
                                     photo="https://i.ibb.co/WFFBc8F/234.png",
                                     caption="<b>Токен успешно добавлен!</b>\n\n"
                                             "<i>Этап 3</i>\n\n"
                                             "<b>Теперь скопируйте адрес любого поста Вашей группы или паблика "
                                             "ВК и перешлите мне</b>\n\n"
                                             "<i>Или можете вернуться в главное меню</i>",
                                     reply_markup=ClientMarkup.client_back_main_menu())
                await states.ClientAddBind.add_vk_channel.set()
        else:
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.send_message(message.from_user.id,
                                   "<b>Надо скопировать всю ссылку ПОСТА и послать мне</b>\n\n"
                                   "<i>Или можете вернуться в главное меню</i>",
                                   disable_web_page_preview=True,
                                   reply_markup=ClientMarkup.client_back_main_menu())


class ClientBinds:

    @staticmethod
    async def client_binds(callback: types.CallbackQuery):
        binds = await getter.client_select_all_binds(callback.from_user.id)
        if binds:
            book = []
            ids = []
            v = 1
            for i in binds:
                on = f"{KEYBOARD.get('CHECK_MARK_BUTTON')} Работает" if i.on \
                    else f"{KEYBOARD.get('CROSS_MARK')} Отключено"
                book.append(f"<b>ID Связи</b> - <i>{v}</i> | {on}\n\n"
                            f"<b>Название ТГ канала (ов)</b> - <i>{' | '.join(i.tg_channels_names)}</i>\n"
                            f"<b>URL ТГ канала (ов)</b> - <i>{' | '.join(i.tg_channels_urls)}</i>\n"
                            f"<b>Название ВК групп</b> - <i>{' | '.join(i.vk_groups_names)}</i>\n"
                            f"<b>URL ВК групп</b> - <i>{' | '.join(i.vk_groups_urls)}</i>\n\n")
                ids.append(i.id)
                v += 1
            await callback.message.edit_text(
                "<b>Список моих связей</b>\n\n"
                f"{''.join(book)}\n\n",
                disable_web_page_preview=True,
                reply_markup=ClientMarkup.client_list_binds(ids))
        else:
            client = await getter.client_select(callback.from_user.id)
            binds = await getter.client_select_all_binds(callback.from_user.id)
            if client.access:
                await callback.message.edit_text(
                    "<b>Меню автопостинга</b>\n\n"
                    "Связь – это связка вашего Telegram-канала и группы/паблика VK\n"
                    "- к одной группе/паблику VK может быть привязано несколько Telegram-каналов\n"
                    "- к нескольким группам/пабликам VK может быть привязан один Telegram-канал (можете настроить любую логику распределения контента)\n\n"
                    "Мы дарим 7 дней бесплатного периода, всем, кто подключился! Для активации откройте раздел \"Подписка\" и затем \"Промо подписка\"\n\n"
                    "Техническая поддержка и дополнительные материалы – https://t.me/smposter_support\n\n"
                    "<b>У вас нет ни одной связи!</b>\n\n"
                    "<i>Вам нужно добавить связь\n\n</i>"
                    f"<b>{KEYBOARD.get('CHECK_MARK_BUTTON')} Ваша подписка активна!</b>\n"
                    f"<b>{KEYBOARD.get('STOPWATCH')} Подписка заканчивается</b> - "
                    f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n\n"
                    f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - "
                    f"<i>{len(binds)}/{client.limit_binds}</i>\n",
                    disable_web_page_preview=True,
                    reply_markup=ClientMarkup.client_main())
            elif client.subscribe_type == "start":
                await callback.message.edit_text(
                    "<b>Меню автопостинга</b>\n\n"
                    "Связь – это связка вашего Telegram-канала и группы/паблика VK\n"
                    "- к одной группе/паблику VK может быть привязано несколько Telegram-каналов\n"
                    "- к нескольким группам/пабликам VK может быть привязан один Telegram-канал (можете настроить любую логику распределения контента)\n\n"
                    "Мы дарим 7 дней бесплатного периода, всем, кто подключился! Для активации откройте раздел \"Подписка\" и затем \"Промо подписка\"\n\n"
                    "Техническая поддержка и дополнительные материалы – https://t.me/smposter_support\n\n"
                    "<b>У вас нет ни одной связи!</b>\n\n"
                    f"<b>{KEYBOARD.get('CROSS_MARK')} Ваша подписка неактивна!</b>\n\n"
                    f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - "
                    f"<i>{len(binds)}/{client.limit_binds}</i>\n",
                    disable_web_page_preview=True,
                    reply_markup=ClientMarkup.client_main())
            else:
                await callback.message.edit_text(
                    "<b>Меню автопостинга</b>\n\n"
                    "Связь – это связка вашего Telegram-канала и группы/паблика VK\n"
                    "- к одной группе/паблику VK может быть привязано несколько Telegram-каналов\n"
                    "- к нескольким группам/пабликам VK может быть привязан один Telegram-канал (можете настроить любую логику распределения контента)\n\n"
                    "Мы дарим 7 дней бесплатного периода, всем, кто подключился! Для активации откройте раздел \"Подписка\" и затем \"Промо подписка\"\n\n"
                    "Техническая поддержка и дополнительные материалы – https://t.me/smposter_support\n\n"
                    "<b>У вас нет ни одной связи!</b>\n\n"
                    "<i>Вам нужно добавить связь\n\n</i>"
                    f"<b>{KEYBOARD.get('CROSS_MARK')} Ваша подписка неактивна!</b>\n"
                    f"<b>{KEYBOARD.get('STOPWATCH')} Подписка закончилась</b> - "
                    f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n\n"
                    f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - "
                    f"<i>{len(binds)}/{client.limit_binds}</i>\n",
                    disable_web_page_preview=True,
                    reply_markup=ClientMarkup.client_main())

    @staticmethod
    async def client_enter_bind(callback: types.CallbackQuery, state: FSMContext):
        await state.finish()
        bind_id = callback.data[18:]
        bind = await getter.client_select_bind(int(bind_id))
        binds = await getter.client_select_all_binds(callback.from_user.id)
        v = 1
        for i in binds:
            if i.id == bind.id:
                break
            else:
                v += 1
        await state.update_data(bind=bind)
        url = "Включено" if bind.url else "Отключено"
        qty = bind.qty if bind.qty else "Отключено"
        tags = bind.tags if bind.tags else "Отсутствуют"
        opt_text = bind.opt_text if bind.opt_text else "Отсутствует"
        excl_tags = bind.excl_tags if bind.excl_tags else "Отсутствуют"
        on = f"{KEYBOARD.get('CHECK_MARK_BUTTON')} Работает" if bind.on \
            else f"{KEYBOARD.get('CROSS_MARK')} Отключено"
        try:
            await callback.message.edit_text(f"Вы вошли в связь под номером <i>{v}</i> | {on}\n\n"
                                             f"<b>Название ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_names)}</i>\n"
                                             f"<b>URL ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_urls)}</i>\n\n"
                                             f"<b>Название ВК групп</b> - <i>{' | '.join(bind.vk_groups_names)}</i>\n"
                                             f"<b>URL ВК групп</b> - <i>{' | '.join(bind.vk_groups_urls)}</i>\n\n"
                                             f"<b>Опции:</b>\n"
                                             f"<b>Ограничение символов</b> - <i>{qty}</i>\n"
                                             f"<b>Хэштэги</b> - <i>{tags}</i>\n"
                                             f"<b>Дополнительный текст после поста</b> - <i>{opt_text}</i>\n"
                                             f"<b>Исключение постов с указанными хэштэгами</b> - <i>{excl_tags}</i>\n"
                                             f"<b>URL-ссылка на пост</b> - <i>{url}</i>",
                                             disable_web_page_preview=True,
                                             reply_markup=ClientMarkup.client_enter_to_bind(bind.on))
        except Exception as ex:
            await bot.delete_message(callback.from_user.id, callback.message.message_id)
            await bot.send_message(callback.from_user.id,
                                   f"Вы вошли в связь под номером <i>{v}</i> | {on}\n\n"
                                   f"<b>Название ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_names)}</i>\n"
                                   f"<b>URL ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_urls)}</i>\n\n"
                                   f"<b>Название ВК групп</b> - <i>{' | '.join(bind.vk_groups_names)}</i>\n"
                                   f"<b>URL ВК групп</b> - <i>{' | '.join(bind.vk_groups_urls)}</i>\n\n"
                                   f"<b>Опции:</b>\n"
                                   f"<b>Ограничение символов</b> - <i>{qty}</i>\n"
                                   f"<b>Хэштэги</b> - <i>{tags}</i>\n"
                                   f"<b>Дополнительный текст после поста</b> - <i>{opt_text}</i>\n"
                                   f"<b>Исключение постов с указанными хэштэгами</b> - <i>{excl_tags}</i>\n"
                                   f"<b>URL-ссылка на пост</b> - <i>{url}</i>",
                                   disable_web_page_preview=True,
                                   reply_markup=ClientMarkup.client_enter_to_bind(bind.on))

    @staticmethod
    async def client_on_bind(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
        await setter.client_on_bind(callback.from_user.id, bind.id)
        bind = await getter.client_select_bind(int(bind.id))
        binds = await getter.client_select_all_binds(callback.from_user.id)
        v = 1
        for i in binds:
            if i.id == bind.id:
                break
            else:
                v += 1
        await state.update_data(bind=bind)
        url = "Включено" if bind.url else "Отключено"
        qty = bind.qty if bind.qty else "Отключено"
        tags = bind.tags if bind.tags else "Отсутствуют"
        opt_text = bind.opt_text if bind.opt_text else "Отсутствует"
        excl_tags = bind.excl_tags if bind.excl_tags else "Отсутствуют"
        on = f"{KEYBOARD.get('CHECK_MARK_BUTTON')} Работает" if bind.on \
            else f"{KEYBOARD.get('CROSS_MARK')} Отключено"
        await callback.message.edit_text(f"<b>Связь включена!</b>\n\n"
                                         f"Вы вошли в связь под номером <i>{v}</i> | {on}\n\n"
                                         f"<b>Название ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_names)}</i>\n"
                                         f"<b>URL ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_urls)}</i>\n\n"
                                         f"<b>Название ВК групп</b> - <i>{' | '.join(bind.vk_groups_names)}</i>\n"
                                         f"<b>URL ВК групп</b> - <i>{' | '.join(bind.vk_groups_urls)}</i>\n\n"
                                         f"<b>Опции:</b>\n"
                                         f"<b>Ограничение символов</b> - <i>{qty}</i>\n"
                                         f"<b>Хэштэги</b> - <i>{tags}</i>\n"
                                         f"<b>Дополнительный текст после поста</b> - <i>{opt_text}</i>\n"
                                         f"<b>Исключение постов с указанными хэштэгами</b> - <i>{excl_tags}</i>\n"
                                         f"<b>URL-ссылка на пост</b> - <i>{url}</i>",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_enter_to_bind(bind.on))

    @staticmethod
    async def client_off_bind(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
        await setter.client_off_bind(callback.from_user.id, bind.id)
        bind = await getter.client_select_bind(int(bind.id))
        binds = await getter.client_select_all_binds(callback.from_user.id)
        v = 1
        for i in binds:
            if i.id == bind.id:
                break
            else:
                v += 1
        await state.update_data(bind=bind)
        url = "Включено" if bind.url else "Отключено"
        qty = bind.qty if bind.qty else "Отключено"
        tags = bind.tags if bind.tags else "Отсутствуют"
        opt_text = bind.opt_text if bind.opt_text else "Отсутствует"
        excl_tags = bind.excl_tags if bind.excl_tags else "Отсутствуют"
        on = f"{KEYBOARD.get('CHECK_MARK_BUTTON')} Работает" if bind.on \
            else f"{KEYBOARD.get('CROSS_MARK')} Отключено"
        await callback.message.edit_text(f"<b>Связь выключена!</b>\n\n"
                                         f"Вы вошли в связь под номером <i>{v}</i> | {on}\n\n"
                                         f"<b>Название ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_names)}</i>\n"
                                         f"<b>URL ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_urls)}</i>\n\n"
                                         f"<b>Название ВК групп</b> - <i>{' | '.join(bind.vk_groups_names)}</i>\n"
                                         f"<b>URL ВК групп</b> - <i>{' | '.join(bind.vk_groups_urls)}</i>\n\n"
                                         f"<b>Опции:</b>\n"
                                         f"<b>Ограничение символов</b> - <i>{qty}</i>\n"
                                         f"<b>Хэштэги</b> - <i>{tags}</i>\n"
                                         f"<b>Дополнительный текст после поста</b> - <i>{opt_text}</i>\n"
                                         f"<b>Исключение постов с указанными хэштэгами</b> - <i>{excl_tags}</i>\n"
                                         f"<b>URL-ссылка на пост</b> - <i>{url}</i>",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_enter_to_bind(bind.on))

    @staticmethod
    async def client_add_one_more_tg_channel(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
            await bot.delete_message(callback.from_user.id, callback.message.message_id)
            await bot.send_photo(callback.from_user.id,
                                 photo="https://i.ibb.co/Xknv9Fv/image.png",
                                 caption="<i>Вы добавляете ТГ канал в данную связь\n\n</i>"
                                         "<b>Нужно пригласить бота @smposter_bot в свой канал"
                                         " в качестве администратора\n\n</b>"
                                         "<b>А потом переслать сюда любой пост (СОДЕРЖАЩИЙ 1 СООБЩЕНИЕ) "
                                         "из этого канала.</b>\n\n"
                                         "<i>Или можете вернуться в меню связи</i>",
                                 reply_markup=ClientMarkup.client_back_to_bind(bind.id))
            await states.ClientAddChannels.new_tg_channel.set()

    @staticmethod
    async def client_add_one_more_tg_channel_1(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
            try:
                if message.forward_from_chat.type == "channel":
                    await message.forward_from_chat.get_administrators()
                    data["tg_channel_id"] = message.forward_from_chat.id
                    data["tg_channel_name"] = message.forward_from_chat.title
                    data["tg_channel_url"] = message.forward_from_chat.username
                    try:
                        for i in range(0, 10):
                            await bot.delete_message(message.from_user.id, message.message_id - i)
                    except Exception as ex:
                        pass
                    for tg_channel_id in bind.tg_channels_ids:
                        if tg_channel_id == str(message.forward_from_chat.id):
                            await bot.send_message(message.from_user.id,
                                                   "Этот канал уже существует в данной связи!",
                                                   disable_web_page_preview=True,
                                                   reply_markup=ClientMarkup.client_back_to_bind(bind.id))
                            await state.finish()
                            break
                    else:
                        url = f"@{data.get('tg_channel_url')}" if data.get('tg_channel_url') else "URL-недоступен"
                        await bot.send_message(message.from_user.id,
                                               "Отлично!\n\n"
                                               f"Название вашего ТГ-канала - <b>{data.get('tg_channel_name')}</b>\n"
                                               f"URL вашего ТГ-канала - <b>{url}</b>\n\n"
                                               "Если всё верно нажмите 'Добавить ТГ канал'\n\n"
                                               "<i>Или можете вернуться в меню связи</i>",
                                               disable_web_page_preview=True,
                                               reply_markup=ClientMarkup.client_approve_new_tg_channel(bind.id))
                else:
                    await bot.send_message(message.from_user.id,
                                           "<b>Что то вы переслали не то</b>")
            except Exception as ex:
                print(ex)
                try:
                    for i in range(0, 10):
                        await bot.delete_message(message.from_user.id, message.message_id - i)
                except Exception as ex:
                    pass
                await bot.send_message(message.from_user.id,
                                       '<b>Добавление канала\n\n'
                                       'Бот не является администратором канала. '
                                       'Убедитесь, что вы добавили бота в свой канал.</b>',
                                       disable_web_page_preview=True,
                                       reply_markup=ClientMarkup.client_back_to_bind(bind.id))

    @staticmethod
    async def client_add_one_more_tg_channel_2(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
            url = f'@{data.get("tg_channel_url")}' if data.get("tg_channel_url") else "URL-недоступен"
            await setter.client_add_new_tg_channel(callback.from_user.id,
                                                   bind.id,
                                                   data.get("tg_channel_name"),
                                                   str(data.get("tg_channel_id")),
                                                   str(url))
        bind = await getter.client_select_bind(int(bind.id))
        await state.finish()
        binds = await getter.client_select_all_binds(callback.from_user.id)
        v = 1
        for i in binds:
            if i.id == bind.id:
                break
            else:
                v += 1
        await state.update_data(bind=bind)
        url = "Включено" if bind.url else "Отключено"
        qty = bind.qty if bind.qty else "Отключено"
        tags = bind.tags if bind.tags else "Отсутствуют"
        opt_text = bind.opt_text if bind.opt_text else "Отсутствует"
        excl_tags = bind.excl_tags if bind.excl_tags else "Отсутствуют"
        on = f"{KEYBOARD.get('CHECK_MARK_BUTTON')} Работает" if bind.on \
            else f"{KEYBOARD.get('CROSS_MARK')} Отключено"
        await callback.message.edit_text(f"<b>Канал успешно добавлен!</b>\n\n"
                                         f"Вы вошли в связь под номером <i>{v}</i> | {on}\n\n"
                                         f"<b>Название ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_names)}</i>\n"
                                         f"<b>URL ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_urls)}</i>\n\n"
                                         f"<b>Название ВК групп</b> - <i>{' | '.join(bind.vk_groups_names)}</i>\n"
                                         f"<b>URL ВК групп</b> - <i>{' | '.join(bind.vk_groups_urls)}</i>\n\n"
                                         f"<b>Опции:</b>\n"
                                         f"<b>Ограничение символов</b> - <i>{qty}</i>\n"
                                         f"<b>Хэштэги</b> - <i>{tags}</i>\n"
                                         f"<b>Дополнительный текст после поста</b> - <i>{opt_text}</i>\n"
                                         f"<b>Исключение постов с указанными хэштэгами</b> - <i>{excl_tags}</i>\n"
                                         f"<b>URL-ссылка на пост</b> - <i>{url}</i>",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_enter_to_bind(bind.on))

    @staticmethod
    async def client_delete_tg_channel(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
            if len(bind.tg_channels_names) == 1:
                await callback.message.edit_text("<b>Вы не можете удалить 1 ТГ канал</b>\n"
                                                 "<b>Как минимум должен быть 1 ТГ канал</b>\n\n"
                                                 "<i>Но Вы можете удалить данную связь из меню связи</i>",
                                                 disable_web_page_preview=True,
                                                 reply_markup=ClientMarkup.client_back_to_bind(bind.id))
            else:
                book_tg_names = []
                book_tg_ids = []
                book = []
                for i in bind.tg_channels_names:
                    book_tg_names.append(f"Название ТГ канала - <b>{i}</b>\n")
                for i in bind.tg_channels_ids:
                    book_tg_ids.append(f"ID ТГ канала - <b>{i}</b>\n\n")
                v = 0
                while v != len(book_tg_names):
                    book.append(book_tg_names[v])
                    book.append(book_tg_ids[v])
                    v += 1
                await callback.message.edit_text(f"Количество ТГ каналов - {len(bind.tg_channels_names)}\n\n"
                                                 f"{''.join(book)}\n"
                                                 f"<i>Выберите ID ТГ канала, чтобы удалить из данной связи</i>\n\n"
                                                 f"<i>Или можете вернуться в меню данной связи</i>",
                                                 disable_web_page_preview=True,
                                                 reply_markup=ClientMarkup.client_delete_tg_channel(
                                                     bind.tg_channels_ids, bind.id))

    @staticmethod
    async def client_delete_tg_channel_1(callback: types.CallbackQuery, state: FSMContext):
        tg_channel_id = callback.data[25:]
        await state.update_data(tg_channel_id=tg_channel_id)
        await callback.message.edit_text(f"Вы точно хотите удалить данный ТГ канал <b>{tg_channel_id}</b> из связи ?",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_delete_tg_channel_approve())

    @staticmethod
    async def client_delete_tg_channel_2(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            tg_channel_id = data.get("tg_channel_id")
            bind = data.get("bind")
            await setter.client_delete_tg_channel(callback.from_user.id,
                                                  bind.id,
                                                  tg_channel_id)
        await state.finish()
        bind = await getter.client_select_bind(int(bind.id))
        binds = await getter.client_select_all_binds(callback.from_user.id)
        v = 1
        for i in binds:
            if i.id == bind.id:
                break
            else:
                v += 1
        await state.update_data(bind=bind)
        url = "Включено" if bind.url else "Отключено"
        qty = bind.qty if bind.qty else "Отключено"
        tags = bind.tags if bind.tags else "Отсутствуют"
        opt_text = bind.opt_text if bind.opt_text else "Отсутствует"
        excl_tags = bind.excl_tags if bind.excl_tags else "Отсутствуют"
        on = f"{KEYBOARD.get('CHECK_MARK_BUTTON')} Работает" if bind.on \
            else f"{KEYBOARD.get('CROSS_MARK')} Отключено"
        await callback.message.edit_text(f"<b>Канал успешно удален!</b>\n\n"
                                         f"Вы вошли в связь под номером <i>{v}</i> | {on}\n\n"
                                         f"<b>Название ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_names)}</i>\n"
                                         f"<b>URL ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_urls)}</i>\n\n"
                                         f"<b>Название ВК групп</b> - <i>{' | '.join(bind.vk_groups_names)}</i>\n"
                                         f"<b>URL ВК групп</b> - <i>{' | '.join(bind.vk_groups_urls)}</i>\n\n"
                                         f"<b>Опции:</b>\n"
                                         f"<b>Ограничение символов</b> - <i>{qty}</i>\n"
                                         f"<b>Хэштэги</b> - <i>{tags}</i>\n"
                                         f"<b>Дополнительный текст после поста</b> - <i>{opt_text}</i>\n"
                                         f"<b>Исключение постов с указанными хэштэгами</b> - <i>{excl_tags}</i>\n"
                                         f"<b>URL-ссылка на пост</b> - <i>{url}</i>",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_enter_to_bind(bind.on))

    @staticmethod
    async def client_add_one_more_vk_group(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
            await callback.message.edit_text("<b>Добавьте название группы ВК, "
                                             "чтобы вы смогли понять какую группу подключили, "
                                             "можете просто скопировать название группы и прислать сюда </b>\n\n"
                                             "<i>Или можете вернуться в меню связи</i>",
                                             disable_web_page_preview=True,
                                             reply_markup=ClientMarkup.client_back_to_bind(bind.id))
        await states.ClientAddChannels.new_vk_group_name.set()

    @staticmethod
    async def client_add_one_more_vk_group_1(message: types.Message, state: FSMContext):
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        async with state.proxy() as data:
            bind = data.get("bind")
            data["vk_group_name"] = message.text
            await bot.send_message(message.from_user.id,
                                   "<b>Отлично!</b>\n"
                                   f"Название ВК-группы - <i>{message.text}</i>\n\n"
                                   f"Если всё верно нажмите <b>Следующий этап</b>\n\n"
                                   f"Если хотите новое название ВК-группы, "
                                   f"введите еще раз сообщение и отправьте мне\n\n"
                                   f"<i>Или можете вернуться в меню связи</i>",
                                   disable_web_page_preview=True,
                                   reply_markup=ClientMarkup.client_approve_new_vk_group_name(bind.id))

    @staticmethod
    async def client_add_one_more_vk_group_2(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
            await bot.delete_message(callback.from_user.id, callback.message.message_id)
            await bot.send_photo(callback.from_user.id,
                                 photo="https://i.ibb.co/WFFBc8F/234.png",
                                 caption="<b>Теперь скопируйте адрес любого поста Вашей группы или паблика "
                                         "ВК и перешлите мне</b>\n\n"
                                         "<i>Или можете вернуться в меню связи</i>",
                                 reply_markup=ClientMarkup.client_back_to_bind(bind.id))
        await states.ClientAddChannels.new_vk_group.set()

    @staticmethod
    async def client_add_one_more_vk_group_3(message: types.Message, state: FSMContext):
        res = message.text.find("wall-")
        if res != -1:
            res1 = message.text[message.text.find("wall-") + 5:]
            result = res1[:res1.find("_")]
            await state.update_data(vk_group_id=result,
                                    vk_group_url=f"vk.com/club{result}")
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            async with state.proxy() as data:
                bind = data.get("bind")
                for vk_group_id in bind.vk_groups_ids:
                    if vk_group_id == result:
                        await bot.send_message(message.from_user.id,
                                               "Этот канал уже существует в данной связи!",
                                               disable_web_page_preview=True,
                                               reply_markup=ClientMarkup.client_back_to_bind(bind.id))
                        await state.finish()
                        break
                else:
                    await bot.send_message(message.from_user.id,
                                           f"<b>Вы добавляете данную группу ВК:</b>\n"
                                           f"<b>Название</b> - <i>{data.get('vk_group_name')}</i>\n"
                                           f"<b>Ссылка</b> - <i>{message.text[:message.text.find('?')]}</i>\n\n"
                                           f'<b>Нажмите "Все верно!" чтобы добавить</b>\n\n'
                                           f"<i>Или можете вернуться в меню данной связи</i>",
                                           disable_web_page_preview=True,
                                           reply_markup=ClientMarkup.client_add_new_group(bind.id))
        else:
            async with state.proxy() as data:
                bind = data.get("bind")
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   "<b>Надо скинуть ссылку на ПОСТ во Вконтакте!</b>\n\n"
                                   "<i>Этап 3</i>\n\n"
                                   "<b>Теперь скопируйте адрес любого поста Вашей группы или паблика "
                                   "ВК и перешлите мне</b>\n\n"
                                   "<i>Или можете вернуться в главное меню</i>",
                                   disable_web_page_preview=True,
                                   reply_markup=ClientMarkup.client_back_to_bind(bind.id))

    @staticmethod
    async def client_add_one_more_vk_group_4(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
            vk_group_id = data.get("vk_group_id")
            vk_group_name = data.get("vk_group_name")
            vk_group_url = data.get("vk_group_url")
        await setter.client_add_vk_group(bind.id, vk_group_name, vk_group_id, vk_group_url)
        await state.finish()
        bind = await getter.client_select_bind(int(bind.id))
        binds = await getter.client_select_all_binds(callback.from_user.id)
        v = 1
        for i in binds:
            if i.id == bind.id:
                break
            else:
                v += 1
        await state.update_data(bind=bind)
        url = "Включено" if bind.url else "Отключено"
        qty = bind.qty if bind.qty else "Отключено"
        tags = bind.tags if bind.tags else "Отсутствуют"
        opt_text = bind.opt_text if bind.opt_text else "Отсутствует"
        excl_tags = bind.excl_tags if bind.excl_tags else "Отсутствуют"
        on = f"{KEYBOARD.get('CHECK_MARK_BUTTON')} Работает" if bind.on \
            else f"{KEYBOARD.get('CROSS_MARK')} Отключено"
        await callback.message.edit_text(f"<b>ВК-группа успешно добавлена!</b>\n\n"
                                         f"Вы вошли в связь под номером <i>{v}</i> | {on}\n\n"
                                         f"<b>Название ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_names)}</i>\n"
                                         f"<b>URL ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_urls)}</i>\n\n"
                                         f"<b>Название ВК групп</b> - <i>{' | '.join(bind.vk_groups_names)}</i>\n"
                                         f"<b>URL ВК групп</b> - <i>{' | '.join(bind.vk_groups_urls)}</i>\n\n"
                                         f"<b>Опции:</b>\n"
                                         f"<b>Ограничение символов</b> - <i>{qty}</i>\n"
                                         f"<b>Хэштэги</b> - <i>{tags}</i>\n"
                                         f"<b>Дополнительный текст после поста</b> - <i>{opt_text}</i>\n"
                                         f"<b>Исключение постов с указанными хэштэгами</b> - <i>{excl_tags}</i>\n"
                                         f"<b>URL-ссылка на пост</b> - <i>{url}</i>",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_enter_to_bind(bind.on))

    @staticmethod
    async def client_delete_vk_group(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
            if len(bind.vk_groups_ids) == 1:
                await callback.message.edit_text("<b>Вы не можете удалить 1 группу</b>\n"
                                                 "<b>Как минимум должна быть 1 группа ВК</b>\n\n"
                                                 "<i>Но Вы можете удалить данную связь из меню связи</i>",
                                                 disable_web_page_preview=True,
                                                 reply_markup=ClientMarkup.client_back_to_bind(bind.id))
            else:
                book_vk_names = []
                book_vk_ids = []
                book = []
                for i in bind.vk_groups_names:
                    book_vk_names.append(f"Название ВК-групп - <b>{i}</b>\n")
                for i in bind.vk_groups_ids:
                    book_vk_ids.append(f"ID ВК-групп - <b>{i}</b>\n\n")
                v = 0
                while v != len(book_vk_names):
                    book.append(book_vk_names[v])
                    book.append(book_vk_ids[v])
                    v += 1
                await callback.message.edit_text(f"Количество ВК-групп - {len(bind.vk_groups_ids)}\n\n"
                                                 f"{''.join(book)}\n"
                                                 f"<i>Выберите ID ВК-группы, чтобы удалить из данной связи</i>\n\n"
                                                 f"<i>Или можете вернуться в меню данной связи</i>",
                                                 disable_web_page_preview=True,
                                                 reply_markup=ClientMarkup.client_delete_group(
                                                     bind.vk_groups_ids, bind.id))

    @staticmethod
    async def client_delete_vk_group_1(callback: types.CallbackQuery, state: FSMContext):
        vk_group_id = callback.data[23:]
        await state.update_data(vk_group_id=vk_group_id)
        await callback.message.edit_text(f"Вы точно хотите удалить данную группу <b>{vk_group_id}</b> из связи ?",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_delete_group_approve())

    @staticmethod
    async def client_delete_vk_group_2(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            vk_group_id = data.get("vk_group_id")
            bind = data.get("bind")
            await setter.client_delete_vk_group(bind.id, vk_group_id)
            await state.finish()
            bind = await getter.client_select_bind(int(bind.id))
            binds = await getter.client_select_all_binds(callback.from_user.id)
            v = 1
            for i in binds:
                if i.id == bind.id:
                    break
                else:
                    v += 1
            await state.update_data(bind=bind)
            url = "Включено" if bind.url else "Отключено"
            qty = bind.qty if bind.qty else "Отключено"
            tags = bind.tags if bind.tags else "Отсутствуют"
            opt_text = bind.opt_text if bind.opt_text else "Отсутствует"
            excl_tags = bind.excl_tags if bind.excl_tags else "Отсутствуют"
            on = f"{KEYBOARD.get('CHECK_MARK_BUTTON')} Работает" if bind.on \
                else f"{KEYBOARD.get('CROSS_MARK')} Отключено"
            await callback.message.edit_text(f"<b>ВК-группа успешно удалена!</b>\n\n"
                                             f"Вы вошли в связь под номером <i>{v}</i> | {on}\n\n"
                                             f"<b>Название ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_names)}</i>\n"
                                             f"<b>URL ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_urls)}</i>\n\n"
                                             f"<b>Название ВК групп</b> - <i>{' | '.join(bind.vk_groups_names)}</i>\n"
                                             f"<b>URL ВК групп</b> - <i>{' | '.join(bind.vk_groups_urls)}</i>\n\n"
                                             f"<b>Опции:</b>\n"
                                             f"<b>Ограничение символов</b> - <i>{qty}</i>\n"
                                             f"<b>Хэштэги</b> - <i>{tags}</i>\n"
                                             f"<b>Дополнительный текст после поста</b> - <i>{opt_text}</i>\n"
                                             f"<b>Исключение постов с указанными хэштэгами</b> - <i>{excl_tags}</i>\n"
                                             f"<b>URL-ссылка на пост</b> - <i>{url}</i>",
                                             disable_web_page_preview=True,
                                             reply_markup=ClientMarkup.client_enter_to_bind(bind.on))

    @staticmethod
    async def client_delete_bind(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
        await callback.message.edit_text(f"<b>Вы уверены что хотите удалить данную связь ?</b>\n\n"
                                         f"<b>Название ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_names)}</i>\n"
                                         f"<b>URL ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_urls)}</i>\n\n"
                                         f"<b>Название ВК групп</b> - <i>{' | '.join(bind.vk_groups_names)}</i>\n"
                                         f"<b>URL ВК групп</b> - <i>{' | '.join(bind.vk_groups_urls)}</i>\n\n",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_delete_bind_approve(bind.id))

    @staticmethod
    async def client_approve_delete_bind(callback: types.CallbackQuery, state: FSMContext):
        bind_id = callback.data[27:]
        await setter.client_delete_bind(int(bind_id))
        await setter.client_del_bind_in_client_table(callback.from_user.id)
        await state.finish()
        binds = await getter.client_select_all_binds(callback.from_user.id)
        if binds:
            book = []
            ids = []
            v = 1
            for i in binds:
                on = f"{KEYBOARD.get('CHECK_MARK_BUTTON')} Работает" if i.on \
                    else f"{KEYBOARD.get('CROSS_MARK')} Отключено"
                book.append(f"<b>ID Связи</b> - <i>{v}</i> | {on}\n\n"
                            f"<b>Название ТГ канала (ов)</b> - <i>{' | '.join(i.tg_channels_names)}</i>\n"
                            f"<b>URL ТГ канала (ов)</b> - <i>{' | '.join(i.tg_channels_urls)}</i>\n"
                            f"<b>Название ВК групп</b> - <i>{' | '.join(i.vk_groups_names)}</i>\n"
                            f"<b>URL ВК групп</b> - <i>{' | '.join(i.vk_groups_urls)}</i>\n\n")
                ids.append(i.id)
                v += 1
            await callback.message.edit_text(
                "<b>Список моих связей</b>\n\n"
                f"{''.join(book)}\n\n",
                disable_web_page_preview=True,
                reply_markup=ClientMarkup.client_list_binds(ids))

    @staticmethod
    async def client_options(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
        binds = await getter.client_select_all_binds(callback.from_user.id)
        v = 1
        for i in binds:
            if not bind:
                continue
            if i.id == bind.id:
                break
            else:
                v += 1
        url = "Включено" if bind.url else "Отключено"
        qty = bind.qty if bind.qty else "Отключено"
        tags = bind.tags if bind.tags else "Отсутствуют"
        opt_text = bind.opt_text if bind.opt_text else "Отсутствует"
        excl_tags = bind.excl_tags if bind.excl_tags else "Отсутствуют"
        on = f"{KEYBOARD.get('CHECK_MARK_BUTTON')} Работает" if bind.on \
            else f"{KEYBOARD.get('CROSS_MARK')} Отключено"
        await callback.message.edit_text(f"Вы вошли в связь под номером <i>{v}</i> | {on}\n\n"
                                         f"<b>Название ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_names)}</i>\n"
                                         f"<b>URL ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_urls)}</i>\n\n"
                                         f"<b>Название ВК групп</b> - <i>{' | '.join(bind.vk_groups_names)}</i>\n"
                                         f"<b>URL ВК групп</b> - <i>{' | '.join(bind.vk_groups_urls)}</i>\n\n"
                                         f"<b>Опции:</b>\n"
                                         f"<b>Ограничение символов</b> - <i>{qty}</i>\n"
                                         f"<b>Хэштэги</b> - <i>{tags}</i>\n"
                                         f"<b>Дополнительный текст после поста</b> - <i>{opt_text}</i>\n"
                                         f"<b>Исключение постов с указанными хэштэгами</b> - <i>{excl_tags}</i>\n"
                                         f"<b>URL-ссылка на пост</b> - <i>{url}</i>",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_change_optionals(bind.id))

    @staticmethod
    async def client_change_qty(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
        await callback.message.edit_text("<i>Сокращение поста. У пользователя есть выбор, "
                                         "в каком виде посты будут публиковаться в ВК - "
                                         "полностью или сокращенные. Если пользователь выбирает "
                                         "вариант с сокращенными постами, в конце записи вставляется "
                                         "ссылка на этот пост в TG-канале + надпись “Читать далее”. "
                                         "Этот параметр задается для всей связи и действует на все посты.</i>\n\n"
                                         "<b>Введите число (кол-во символов) "
                                         "если хотите включить ограничение символов поста</b>\n\n"
                                         "<i>Или можете вернуться в меню данной связи</i>",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_change_qty(bind.qty))
        await states.ClientOptions.qty.set()

    @staticmethod
    async def client_change_qty_1(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
        if message.text.isdigit():
            await setter.client_change_qty(bind.id, int(message.text))
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            bind = await getter.client_select_bind(bind.id)
            binds = await getter.client_select_all_binds(message.from_user.id)
            v = 1
            for i in binds:
                if i.id == bind.id:
                    break
                else:
                    v += 1
            await state.update_data(bind=bind)
            url = "Включено" if bind.url else "Отключено"
            qty = bind.qty if bind.qty else "Отключено"
            tags = bind.tags if bind.tags else "Отсутствуют"
            opt_text = bind.opt_text if bind.opt_text else "Отсутствует"
            excl_tags = bind.excl_tags if bind.excl_tags else "Отсутствуют"
            on = f"{KEYBOARD.get('CHECK_MARK_BUTTON')} Работает" if bind.on \
                else f"{KEYBOARD.get('CROSS_MARK')} Отключено"
            await bot.send_message(message.from_user.id,
                                   f"<b>Ограничение символов установлено!</b>\n\n"
                                   f"Вы вошли в связь под номером <i>{v}</i> | {on}\n\n"
                                   f"<b>Название ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_names)}</i>\n"
                                   f"<b>URL ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_urls)}</i>\n\n"
                                   f"<b>Название ВК групп</b> - <i>{' | '.join(bind.vk_groups_names)}</i>\n"
                                   f"<b>URL ВК групп</b> - <i>{' | '.join(bind.vk_groups_urls)}</i>\n\n"
                                   f"<b>Опции:</b>\n"
                                   f"<b>Ограничение символов</b> - <i>{qty}</i>\n"
                                   f"<b>Хэштэги</b> - <i>{tags}</i>\n"
                                   f"<b>Дополнительный текст после поста</b> - <i>{opt_text}</i>\n"
                                   f"<b>Исключение постов с указанными хэштэгами</b> - <i>{excl_tags}</i>\n"
                                   f"<b>URL-ссылка на пост</b> - <i>{url}</i>",
                                   disable_web_page_preview=True,
                                   reply_markup=ClientMarkup.client_change_optionals(bind.id))
        else:
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   f"<b>Вам надо ввести натуральное число</b>",
                                   disable_web_page_preview=True,
                                   reply_markup=ClientMarkup.client_back_to_bind_options())

    @staticmethod
    async def client_delete_qty(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
        await setter.client_change_delete_qty(bind.id)
        bind = await getter.client_select_bind(bind.id)
        binds = await getter.client_select_all_binds(callback.from_user.id)
        v = 1
        for i in binds:
            if i.id == bind.id:
                break
            else:
                v += 1
        await state.update_data(bind=bind)
        url = "Включено" if bind.url else "Отключено"
        qty = bind.qty if bind.qty else "Отключено"
        tags = bind.tags if bind.tags else "Отсутствуют"
        opt_text = bind.opt_text if bind.opt_text else "Отсутствует"
        excl_tags = bind.excl_tags if bind.excl_tags else "Отсутствуют"
        on = f"{KEYBOARD.get('CHECK_MARK_BUTTON')} Работает" if bind.on \
            else f"{KEYBOARD.get('CROSS_MARK')} Отключено"
        await callback.message.edit_text(f"<b>Ограничение символов удалено!</b>\n\n"
                                         f"Вы вошли в связь под номером <i>{v}</i> | {on}\n\n"
                                         f"<b>Название ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_names)}</i>\n"
                                         f"<b>URL ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_urls)}</i>\n\n"
                                         f"<b>Название ВК групп</b> - <i>{' | '.join(bind.vk_groups_names)}</i>\n"
                                         f"<b>URL ВК групп</b> - <i>{' | '.join(bind.vk_groups_urls)}</i>\n\n"
                                         f"<b>Опции:</b>\n"
                                         f"<b>Ограничение символов</b> - <i>{qty}</i>\n"
                                         f"<b>Хэштэги</b> - <i>{tags}</i>\n"
                                         f"<b>Дополнительный текст после поста</b> - <i>{opt_text}</i>\n"
                                         f"<b>Исключение постов с указанными хэштэгами</b> - <i>{excl_tags}</i>\n"
                                         f"<b>URL-ссылка на пост</b> - <i>{url}</i>",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_change_optionals(bind.id))

    @staticmethod
    async def client_change_tags(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
        await callback.message.edit_text("<i>Добавление хэштегов. "
                                         "Пользователь может выбрать, добавлять  "
                                         "дополнительные хэштеги к репосту записей или нет. "
                                         "Этот параметр задается для всей связи и действует на все посты.</i>\n\n"
                                         "<b>Введите слова без знака хэштэга # через пробел.</b> "
                                         "Пример: <i>вакансия</i> <i>программист</i> <i>работа</i>\n\n"
                                         "<i>Или можете вернуться в меню данной связи</i>",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_change_tags(bind.tags))
        await states.ClientOptions.tags.set()

    @staticmethod
    async def client_change_tags_1(message: types.Message, state: FSMContext):
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        result = ' #'.join(message.text.split())
        await state.update_data(tags=result)
        await bot.send_message(message.from_user.id,
                               f"Вот такие хэштэги будут после каждого поста:\n\n"
                               f"<b>#{result}</b>\n\n"
                               f"<i>Вы можете еще раз написать сюда хэштэги и отправить мне сообщением, "
                               f"если хотите исправить</i>\n\n"
                               f"<i>Или можете вернуться в главное меню</i>",
                               disable_web_page_preview=True,
                               reply_markup=ClientMarkup.client_add_new_tags())

    @staticmethod
    async def client_change_tags_2(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
            tags = data.get("tags")
        await setter.client_change_tags(bind.id, f"#{tags}")
        bind = await getter.client_select_bind(bind.id)
        binds = await getter.client_select_all_binds(callback.from_user.id)
        v = 1
        for i in binds:
            if i.id == bind.id:
                break
            else:
                v += 1
        await state.update_data(bind=bind)
        url = "Включено" if bind.url else "Отключено"
        qty = bind.qty if bind.qty else "Отключено"
        tags = bind.tags if bind.tags else "Отсутствуют"
        opt_text = bind.opt_text if bind.opt_text else "Отсутствует"
        excl_tags = bind.excl_tags if bind.excl_tags else "Отсутствуют"
        on = f"{KEYBOARD.get('CHECK_MARK_BUTTON')} Работает" if bind.on \
            else f"{KEYBOARD.get('CROSS_MARK')} Отключено"
        await callback.message.edit_text(f"<b>Добавлены новые хэштэги!</b>\n\n"
                                         f"Вы вошли в связь под номером <i>{v}</i> | {on}\n\n"
                                         f"<b>Название ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_names)}</i>\n"
                                         f"<b>URL ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_urls)}</i>\n\n"
                                         f"<b>Название ВК групп</b> - <i>{' | '.join(bind.vk_groups_names)}</i>\n"
                                         f"<b>URL ВК групп</b> - <i>{' | '.join(bind.vk_groups_urls)}</i>\n\n"
                                         f"<b>Опции:</b>\n"
                                         f"<b>Ограничение символов</b> - <i>{qty}</i>\n"
                                         f"<b>Хэштэги</b> - <i>{tags}</i>\n"
                                         f"<b>Дополнительный текст после поста</b> - <i>{opt_text}</i>\n"
                                         f"<b>Исключение постов с указанными хэштэгами</b> - <i>{excl_tags}</i>\n"
                                         f"<b>URL-ссылка на пост</b> - <i>{url}</i>",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_change_optionals(bind.id))

    @staticmethod
    async def client_delete_tags(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
        await setter.client_change_delete_tags(bind.id)
        bind = await getter.client_select_bind(bind.id)
        binds = await getter.client_select_all_binds(callback.from_user.id)
        v = 1
        for i in binds:
            if i.id == bind.id:
                break
            else:
                v += 1
        await state.update_data(bind=bind)
        url = "Включено" if bind.url else "Отключено"
        qty = bind.qty if bind.qty else "Отключено"
        tags = bind.tags if bind.tags else "Отсутствуют"
        opt_text = bind.opt_text if bind.opt_text else "Отсутствует"
        excl_tags = bind.excl_tags if bind.excl_tags else "Отсутствуют"
        on = f"{KEYBOARD.get('CHECK_MARK_BUTTON')} Работает" if bind.on \
            else f"{KEYBOARD.get('CROSS_MARK')} Отключено"
        await callback.message.edit_text(f"<b>Хэштэги удалены!</b>\n\n"
                                         f"Вы вошли в связь под номером <i>{v}</i> | {on}\n\n"
                                         f"<b>Название ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_names)}</i>\n"
                                         f"<b>URL ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_urls)}</i>\n\n"
                                         f"<b>Название ВК групп</b> - <i>{' | '.join(bind.vk_groups_names)}</i>\n"
                                         f"<b>URL ВК групп</b> - <i>{' | '.join(bind.vk_groups_urls)}</i>\n\n"
                                         f"<b>Опции:</b>\n"
                                         f"<b>Ограничение символов</b> - <i>{qty}</i>\n"
                                         f"<b>Хэштэги</b> - <i>{tags}</i>\n"
                                         f"<b>Дополнительный текст после поста</b> - <i>{opt_text}</i>\n"
                                         f"<b>Исключение постов с указанными хэштэгами</b> - <i>{excl_tags}</i>\n"
                                         f"<b>URL-ссылка на пост</b> - <i>{url}</i>",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_change_optionals(bind.id))

    @staticmethod
    async def client_change_opt_text(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
        await callback.message.edit_text("<i>Добавление текста после поста. "
                                         "У пользователя есть возможность добавить какой-нибудь текст после поста, "
                                         "либо не добавлять ничего. Этот параметр задается для всей связи и действует "
                                         "на все посты.</i>\n\n"
                                         "<b>Введите текст</b>\n\n"
                                         "<i>Или можете вернуться в меню данной связи</i>",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_change_opt_text(bind.opt_text))
        await states.ClientOptions.opt_text.set()

    @staticmethod
    async def client_change_opt_text_1(message: types.Message, state: FSMContext):
        try:
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
        except:
            pass
        await state.update_data(opt_text=message.text)
        await bot.send_message(message.from_user.id,
                               f"Вот такой текст будет после каждого поста:\n\n"
                               f"<b>{message.text}</b>\n\n"
                               f"<i>Вы можете еще раз написать сюда текст и отправить мне сообщением, "
                               f"если хотите исправить</i>\n\n"
                               f"<i>Или можете вернуться в главное меню</i>",
                               disable_web_page_preview=True,
                               reply_markup=ClientMarkup.client_add_new_opt_text())

    @staticmethod
    async def client_change_opt_text_2(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
            opt_text = data.get("opt_text")
        await setter.client_change_opt_text(bind.id, opt_text)
        bind = await getter.client_select_bind(bind.id)
        binds = await getter.client_select_all_binds(callback.from_user.id)
        v = 1
        for i in binds:
            if i.id == bind.id:
                break
            else:
                v += 1
        await state.update_data(bind=bind)
        url = "Включено" if bind.url else "Отключено"
        qty = bind.qty if bind.qty else "Отключено"
        tags = bind.tags if bind.tags else "Отсутствуют"
        opt_text = bind.opt_text if bind.opt_text else "Отсутствует"
        excl_tags = bind.excl_tags if bind.excl_tags else "Отсутствуют"
        on = f"{KEYBOARD.get('CHECK_MARK_BUTTON')} Работает" if bind.on \
            else f"{KEYBOARD.get('CROSS_MARK')} Отключено"
        await callback.message.edit_text(f"<b>Добавлен новый доп. текст!</b>\n\n"
                                         f"Вы вошли в связь под номером <i>{v}</i> | {on}\n\n"
                                         f"<b>Название ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_names)}</i>\n"
                                         f"<b>URL ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_urls)}</i>\n\n"
                                         f"<b>Название ВК групп</b> - <i>{' | '.join(bind.vk_groups_names)}</i>\n"
                                         f"<b>URL ВК групп</b> - <i>{' | '.join(bind.vk_groups_urls)}</i>\n\n"
                                         f"<b>Опции:</b>\n"
                                         f"<b>Ограничение символов</b> - <i>{qty}</i>\n"
                                         f"<b>Хэштэги</b> - <i>{tags}</i>\n"
                                         f"<b>Дополнительный текст после поста</b> - <i>{opt_text}</i>\n"
                                         f"<b>Исключение постов с указанными хэштэгами</b> - <i>{excl_tags}</i>\n"
                                         f"<b>URL-ссылка на пост</b> - <i>{url}</i>",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_change_optionals(bind.id))

    @staticmethod
    async def client_delete_opt_text(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
        await setter.client_change_delete_opt_text(bind.id)
        bind = await getter.client_select_bind(bind.id)
        binds = await getter.client_select_all_binds(callback.from_user.id)
        v = 1
        for i in binds:
            if i.id == bind.id:
                break
            else:
                v += 1
        await state.update_data(bind=bind)
        url = "Включено" if bind.url else "Отключено"
        qty = bind.qty if bind.qty else "Отключено"
        tags = bind.tags if bind.tags else "Отсутствуют"
        opt_text = bind.opt_text if bind.opt_text else "Отсутствует"
        excl_tags = bind.excl_tags if bind.excl_tags else "Отсутствуют"
        on = f"{KEYBOARD.get('CHECK_MARK_BUTTON')} Работает" if bind.on \
            else f"{KEYBOARD.get('CROSS_MARK')} Отключено"
        await callback.message.edit_text(f"<b>Доп. текст удален!</b>\n\n"
                                         f"Вы вошли в связь под номером <i>{v}</i> | {on}\n\n"
                                         f"<b>Название ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_names)}</i>\n"
                                         f"<b>URL ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_urls)}</i>\n\n"
                                         f"<b>Название ВК групп</b> - <i>{' | '.join(bind.vk_groups_names)}</i>\n"
                                         f"<b>URL ВК групп</b> - <i>{' | '.join(bind.vk_groups_urls)}</i>\n\n"
                                         f"<b>Опции:</b>\n"
                                         f"<b>Ограничение символов</b> - <i>{qty}</i>\n"
                                         f"<b>Хэштэги</b> - <i>{tags}</i>\n"
                                         f"<b>Дополнительный текст после поста</b> - <i>{opt_text}</i>\n"
                                         f"<b>Исключение постов с указанными хэштэгами</b> - <i>{excl_tags}</i>\n"
                                         f"<b>URL-ссылка на пост</b> - <i>{url}</i>",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_change_optionals(bind.id))

    @staticmethod
    async def client_change_excl_tags(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
        await callback.message.edit_text("<i>Исключение постов с указанными хэштегами. "
                                         "Пользователь может указать определенные хэштеги, "
                                         "и посты, в которых они содержатся, не должны публиковаться в ВК-группе. "
                                         "Этот параметр задается для всей связи и действует на все посты.</i>\n\n"
                                         "<b>Введите слова без знака хэштэга # через пробел.</b> "
                                         "Пример: <i>реклама</i> <i>задача</i> <i>статья</i>\n\n"
                                         "<i>Или можете вернуться в меню данной связи</i>",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_change_excl_tags(bind.excl_tags))
        await states.ClientOptions.excl_tags.set()

    @staticmethod
    async def client_change_excl_tags_1(message: types.Message, state: FSMContext):
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        result = ' #'.join(message.text.split())
        await state.update_data(excl_tags=result)
        await bot.send_message(message.from_user.id,
                               f"По таким хэштэгам ваши посты будут игнорироваться:\n\n"
                               f"<b>#{result}</b>\n\n"
                               f"<i>Вы можете еще раз написать сюда хэштэги и отправить мне сообщением, "
                               f"если хотите исправить</i>\n\n"
                               f"<i>Или можете вернуться в главное меню</i>",
                               disable_web_page_preview=True,
                               reply_markup=ClientMarkup.client_add_new_excl_tags())

    @staticmethod
    async def client_change_excl_tags_2(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
            excl_tags = data.get("excl_tags")
        await setter.client_change_excl_tags(bind.id, f"#{excl_tags}")
        bind = await getter.client_select_bind(bind.id)
        binds = await getter.client_select_all_binds(callback.from_user.id)
        v = 1
        for i in binds:
            if i.id == bind.id:
                break
            else:
                v += 1
        await state.update_data(bind=bind)
        url = "Включено" if bind.url else "Отключено"
        qty = bind.qty if bind.qty else "Отключено"
        tags = bind.tags if bind.tags else "Отсутствуют"
        opt_text = bind.opt_text if bind.opt_text else "Отсутствует"
        excl_tags = bind.excl_tags if bind.excl_tags else "Отсутствуют"
        on = f"{KEYBOARD.get('CHECK_MARK_BUTTON')} Работает" if bind.on \
            else f"{KEYBOARD.get('CROSS_MARK')} Отключено"
        await callback.message.edit_text(f"<b>Исключающие хэштэги добавлены!</b>\n\n"
                                         f"Вы вошли в связь под номером <i>{v}</i> | {on}\n\n"
                                         f"<b>Название ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_names)}</i>\n"
                                         f"<b>URL ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_urls)}</i>\n\n"
                                         f"<b>Название ВК групп</b> - <i>{' | '.join(bind.vk_groups_names)}</i>\n"
                                         f"<b>URL ВК групп</b> - <i>{' | '.join(bind.vk_groups_urls)}</i>\n\n"
                                         f"<b>Опции:</b>\n"
                                         f"<b>Ограничение символов</b> - <i>{qty}</i>\n"
                                         f"<b>Хэштэги</b> - <i>{tags}</i>\n"
                                         f"<b>Дополнительный текст после поста</b> - <i>{opt_text}</i>\n"
                                         f"<b>Исключение постов с указанными хэштэгами</b> - <i>{excl_tags}</i>\n"
                                         f"<b>URL-ссылка на пост</b> - <i>{url}</i>",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_change_optionals(bind.id))

    @staticmethod
    async def client_delete_excl_tags(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
        await setter.client_change_delete_excl_tags(bind.id)
        bind = await getter.client_select_bind(bind.id)
        binds = await getter.client_select_all_binds(callback.from_user.id)
        v = 1
        for i in binds:
            if i.id == bind.id:
                break
            else:
                v += 1
        await state.update_data(bind=bind)
        url = "Включено" if bind.url else "Отключено"
        qty = bind.qty if bind.qty else "Отключено"
        tags = bind.tags if bind.tags else "Отсутствуют"
        opt_text = bind.opt_text if bind.opt_text else "Отсутствует"
        excl_tags = bind.excl_tags if bind.excl_tags else "Отсутствуют"
        on = f"{KEYBOARD.get('CHECK_MARK_BUTTON')} Работает" if bind.on \
            else f"{KEYBOARD.get('CROSS_MARK')} Отключено"
        await callback.message.edit_text(f"<b>Исключающие хэштэги удалены!</b>\n\n"
                                         f"Вы вошли в связь под номером <i>{v}</i> | {on}\n\n"
                                         f"<b>Название ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_names)}</i>\n"
                                         f"<b>URL ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_urls)}</i>\n\n"
                                         f"<b>Название ВК групп</b> - <i>{' | '.join(bind.vk_groups_names)}</i>\n"
                                         f"<b>URL ВК групп</b> - <i>{' | '.join(bind.vk_groups_urls)}</i>\n\n"
                                         f"<b>Опции:</b>\n"
                                         f"<b>Ограничение символов</b> - <i>{qty}</i>\n"
                                         f"<b>Хэштэги</b> - <i>{tags}</i>\n"
                                         f"<b>Дополнительный текст после поста</b> - <i>{opt_text}</i>\n"
                                         f"<b>Исключение постов с указанными хэштэгами</b> - <i>{excl_tags}</i>\n"
                                         f"<b>URL-ссылка на пост</b> - <i>{url}</i>",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_change_optionals(bind.id))

    @staticmethod
    async def client_url(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
        await callback.message.edit_text("<i>URL-ссылка на пост. "
                                         "Данная функция дает возможность добавлять ссылку "
                                         "на исходный пост или не добавлять ничего. "
                                         "Этот параметр задается для всей связи и действует на все посты.</i>\n\n"
                                         "<b>Добавлять или нет ?</b>\n\n"
                                         "<i>Или можете вернуться в меню данной связи</i>",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_add_url())

    @staticmethod
    async def client_url_add(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
        await setter.client_change_add_url(bind.id)
        bind = await getter.client_select_bind(bind.id)
        binds = await getter.client_select_all_binds(callback.from_user.id)
        v = 1
        for i in binds:
            if i.id == bind.id:
                break
            else:
                v += 1
        await state.update_data(bind=bind)
        url = "Включено" if bind.url else "Отключено"
        qty = bind.qty if bind.qty else "Отключено"
        tags = bind.tags if bind.tags else "Отсутствуют"
        opt_text = bind.opt_text if bind.opt_text else "Отсутствует"
        excl_tags = bind.excl_tags if bind.excl_tags else "Отсутствуют"
        on = f"{KEYBOARD.get('CHECK_MARK_BUTTON')} Работает" if bind.on \
            else f"{KEYBOARD.get('CROSS_MARK')} Отключено"
        await callback.message.edit_text(f"<b>URL в конце поста добавлен!</b>\n\n"
                                         f"Вы вошли в связь под номером <i>{v}</i> | {on}\n\n"
                                         f"<b>Название ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_names)}</i>\n"
                                         f"<b>URL ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_urls)}</i>\n\n"
                                         f"<b>Название ВК групп</b> - <i>{' | '.join(bind.vk_groups_names)}</i>\n"
                                         f"<b>URL ВК групп</b> - <i>{' | '.join(bind.vk_groups_urls)}</i>\n\n"
                                         f"<b>Опции:</b>\n"
                                         f"<b>Ограничение символов</b> - <i>{qty}</i>\n"
                                         f"<b>Хэштэги</b> - <i>{tags}</i>\n"
                                         f"<b>Дополнительный текст после поста</b> - <i>{opt_text}</i>\n"
                                         f"<b>Исключение постов с указанными хэштэгами</b> - <i>{excl_tags}</i>\n"
                                         f"<b>URL-ссылка на пост</b> - <i>{url}</i>",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_change_optionals(bind.id))

    @staticmethod
    async def client_url_delete(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
        await setter.client_change_delete_url(bind.id)
        bind = await getter.client_select_bind(bind.id)
        binds = await getter.client_select_all_binds(callback.from_user.id)
        v = 1
        for i in binds:
            if i.id == bind.id:
                break
            else:
                v += 1
        await state.update_data(bind=bind)
        url = "Включено" if bind.url else "Отключено"
        qty = bind.qty if bind.qty else "Отключено"
        tags = bind.tags if bind.tags else "Отсутствуют"
        opt_text = bind.opt_text if bind.opt_text else "Отсутствует"
        excl_tags = bind.excl_tags if bind.excl_tags else "Отсутствуют"
        on = f"{KEYBOARD.get('CHECK_MARK_BUTTON')} Работает" if bind.on \
            else f"{KEYBOARD.get('CROSS_MARK')} Отключено"
        await callback.message.edit_text(f"<b>URL в конце поста удален!</b>\n\n"
                                         f"Вы вошли в связь под номером <i>{v}</i> | {on}\n\n"
                                         f"<b>Название ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_names)}</i>\n"
                                         f"<b>URL ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_urls)}</i>\n\n"
                                         f"<b>Название ВК групп</b> - <i>{' | '.join(bind.vk_groups_names)}</i>\n"
                                         f"<b>URL ВК групп</b> - <i>{' | '.join(bind.vk_groups_urls)}</i>\n\n"
                                         f"<b>Опции:</b>\n"
                                         f"<b>Ограничение символов</b> - <i>{qty}</i>\n"
                                         f"<b>Хэштэги</b> - <i>{tags}</i>\n"
                                         f"<b>Дополнительный текст после поста</b> - <i>{opt_text}</i>\n"
                                         f"<b>Исключение постов с указанными хэштэгами</b> - <i>{excl_tags}</i>\n"
                                         f"<b>URL-ссылка на пост</b> - <i>{url}</i>",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_change_optionals(bind.id))


class ClientAddBinds:
    @staticmethod
    async def client_add_bind_1(callback: types.CallbackQuery):
        client = await getter.client_select(callback.from_user.id)
        if client.binds >= client.limit_binds:
            binds = await getter.client_select_all_binds(callback.from_user.id)
            if client.access:
                await callback.message.edit_text(
                    "<b>У вас достигнут лимит связей!</b>\n"
                    "<b>Чтобы увеличить лимит, пройдите в меню</b> "
                    "<b>Подписка, а затем нажмите кнопку Увеличить кол-во связей</b>"
                    "<b>Меню автопостинга</b>\n\n"
                    "Связь – это связка вашего Telegram-канала и группы/паблика VK\n"
                    "- к одной группе/паблику VK может быть привязано несколько Telegram-каналов\n"
                    "- к нескольким группам/пабликам VK может быть привязан один Telegram-канал (можете настроить любую логику распределения контента)\n\n"
                    "Мы дарим 7 дней бесплатного периода, всем, кто подключился! Для активации откройте раздел \"Подписка\" и затем \"Промо подписка\"\n\n"
                    "Техническая поддержка и дополнительные материалы – https://t.me/smposter_support\n\n"
                    f"<b>{KEYBOARD.get('CHECK_MARK_BUTTON')} Ваша подписка активна!</b>\n"
                    f"<b>{KEYBOARD.get('STOPWATCH')} Подписка заканчивается</b> - "
                    f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n\n"
                    f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - "
                    f"<i>{len(binds)}/{client.limit_binds}</i>\n",
                    disable_web_page_preview=True,
                    reply_markup=ClientMarkup.client_main())
            else:
                await callback.message.edit_text(
                    "<b>Меню автопостинга</b>\n\n"
                    "Связь – это связка вашего Telegram-канала и группы/паблика VK\n"
                    "- к одной группе/паблику VK может быть привязано несколько Telegram-каналов\n"
                    "- к нескольким группам/пабликам VK может быть привязан один Telegram-канал (можете настроить любую логику распределения контента)\n\n"
                    "Мы дарим 7 дней бесплатного периода, всем, кто подключился! Для активации откройте раздел \"Подписка\" и затем \"Промо подписка\"\n\n"
                    "Техническая поддержка и дополнительные материалы – https://t.me/smposter_support\n\n"
                    f"<b>{KEYBOARD.get('CROSS_MARK')} Ваша подписка неактивна!</b>\n"
                    f"<b>{KEYBOARD.get('STOPWATCH')} Подписка закончилась</b> - "
                    f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n\n"
                    f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - "
                    f"<i>{len(binds)}/{client.limit_binds}</i>\n",
                    disable_web_page_preview=True,
                    reply_markup=ClientMarkup.client_main())
        elif client.access is False:
            await callback.message.edit_text("<b>Вы не можете добавить связь, так как у вас нет подписки!</b>\n\n"
                                             "<b>Пройдите в меню подписка</b>",
                                             reply_markup=ClientMarkup.client_main())
        else:
            await bot.delete_message(callback.from_user.id, callback.message.message_id)
            await bot.send_photo(callback.from_user.id,
                                 photo="https://i.ibb.co/Xknv9Fv/image.png",
                                 caption="<b>Создание связи ТГ-канал и ВК-группы</b>\n\n"
                                         "<i>1 Этап\n</i>"
                                         "<b>Пригласить бота @smposter_bot в свой канал"
                                         " в качестве администратора\n\n</b> "
                                         "<i>2 Этап</i>\n<b>Переслать сюда любой пост (СОДЕРЖАЩИЙ 1 СООБЩЕНИЕ) "
                                         "из этого канала.</b>\n\n"
                                         "<i>Или можете вернуться в главное меню</i>",
                                 reply_markup=ClientMarkup.client_back_main_menu())
            await states.ClientAddBind.add_bind.set()

    @staticmethod
    async def client_add_bind_2(message: types.Message, state: FSMContext):
        try:
            if message.forward_from_chat:
                if message.forward_from_chat.type == "channel":
                    await message.forward_from_chat.get_administrators()
                    await state.update_data(tg_channel_id=message.forward_from_chat.id,
                                            tg_channel_name=message.forward_from_chat.title,
                                            tg_channel_url=message.forward_from_chat.username)
                    client = await getter.client_select(message.from_user.id)
                    if client.vk_token is None:
                        try:
                            for i in range(0, 10):
                                await bot.delete_message(message.from_user.id, message.message_id - i)
                        except Exception as ex:
                            pass
                        await bot.send_message(message.from_user.id,
                                               "<b>Нужно получить токен VK, чтобы делать публикации.</b>\n\n"
                                               "<b>Это надо сделать один раз, при первой настройке.</b>\n\n"
                                               "<b>Для этого:</b>\n"
                                               "<b>1. Перейдите по ссылке – https://vkhost.github.io/</b>\n"
                                               "<b>2. Нажмите кнопку “VK admin” (первая в верхнем ряду)</b>\n"
                                               "<b>3. Дайте все необходимые разрешения, которые запрашивают</b>\n"
                                               "<b>4. Скопируйте ссылку из строки браузера и"
                                               " полностью перешлите ее сюда</b>\n\n"
                                               "<i>Или можете вернуться в главное меню</i>",
                                               disable_web_page_preview=True,
                                               reply_markup=ClientMarkup.client_back_main_menu())
                        await states.ClientAddBind.new_vk_token.set()
                    else:
                        all_binds = await getter.all_binds()
                        clean = True
                        for bind in all_binds:
                            for tg_channel in bind.tg_channels_ids:
                                if str(message.forward_from_chat.id) == tg_channel:
                                    try:
                                        for i in range(0, 10):
                                            await bot.delete_message(message.from_user.id, message.message_id - i)
                                    except Exception as ex:
                                        pass
                                    await bot.send_message(message.from_user.id,
                                                           "Для данного ТГ канала уже существует связь!",
                                                           disable_web_page_preview=True,
                                                           reply_markup=ClientMarkup.client_main())
                                    clean = False
                                    break
                        if clean:
                            try:
                                for i in range(0, 10):
                                    await bot.delete_message(message.from_user.id, message.message_id - i)
                            except Exception as ex:
                                pass
                            await bot.send_photo(message.from_user.id,
                                                 photo="https://i.ibb.co/WFFBc8F/234.png",
                                                 caption="<b>Отлично!</b>\n\n"
                                                         "<i>Этап 3</i>\n\n"
                                                         "<b>Теперь скопируйте адрес любого поста Вашей группы или паблика "
                                                         "ВК и перешлите мне</b>\n\n"
                                                         "<i>Или можете вернуться в главное меню</i>",
                                                 reply_markup=ClientMarkup.client_back_main_menu_with_caption())
                            await states.ClientAddBind.add_vk_channel.set()
            else:
                try:
                    for i in range(0, 10):
                        await bot.delete_message(message.from_user.id, message.message_id - i)
                except Exception as ex:
                    pass
                await bot.send_message(message.from_user.id,
                                       "<b>Ошибка\n"
                                       "Скорее всего вы переслали сообщение из чата, а не канала</b>",
                                       disable_web_page_preview=True,
                                       reply_markup=ClientMarkup.client_back_main_menu())
        except Exception as ex:
            print(ex)
            try:
                for i in range(0, 10):
                    await bot.delete_message(message.from_user.id, message.message_id - i)
            except Exception as ex:
                pass
            await bot.send_message(message.from_user.id,
                                   '<b>Добавление канала\n\n'
                                   'Бот не является администратором канала. '
                                   'Убедитесь, что вы добавили бота в свой канал.</b>\n'
                                   'Или вы отправили боту пост без сообщения '
                                   '(просто переслали документ или картинку, нужно именно с текстом)',
                                   disable_web_page_preview=True,
                                   reply_markup=ClientMarkup.client_back_main_menu())

    @staticmethod
    async def client_add_bind_3(message: types.Message, state: FSMContext):
        res = message.text.find("wall-")
        if res != -1:
            res1 = message.text[message.text.find("wall-") + 5:]
            result = res1[:res1.find("_")]
            await state.update_data(vk_group_id=result,
                                    vk_group_url=f"vk.com/club{result}")
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            async with state.proxy() as data:
                url = f"@{data.get('tg_channel_url')}" if data.get('tg_channel_url') else "URL-недоступен"
                await bot.send_message(message.from_user.id,
                                       f"<i>4 Этап</i>\n\n"
                                       f"Название вашего ТГ-канала - <b>{data.get('tg_channel_name')}</b>\n"
                                       f"URL вашего ТГ-канала - <b>{url}</b>\n\n"
                                       f"К этому ТГ-каналу вы привязываете данную группу ВК - "
                                       f"<b>vk.com/club{result}</b>\n\n"
                                       f'<i>Остался последний этап!</i>\n\n'
                                       f'<b>Добавьте название группы ВК, '
                                       f'чтобы вы смогли понять какую группу подключили, '
                                       f'можете просто скопировать название группы и прислать сюда</b>\n\n'
                                       f"<i>Или можете вернуться в главное меню</i>",
                                       reply_markup=ClientMarkup.client_back_main_menu(),
                                       disable_web_page_preview=True)
                await states.ClientAddBind.add_bind_name_vk_group.set()
        else:
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_photo(message.from_user.id,
                                 photo="https://i.ibb.co/WFFBc8F/234.png",
                                 caption="<b>Надо скинуть ссылку на ПОСТ во Вконтакте!</b>\n\n"
                                         "<i>Этап 3</i>\n\n"
                                         "<b>Теперь скопируйте адрес любого поста Вашей группы или паблика "
                                         "ВК и перешлите мне</b>\n\n"
                                         "<i>Или можете вернуться в главное меню</i>",
                                 reply_markup=ClientMarkup.client_back_main_menu())

    @staticmethod
    async def client_add_bind_4(message: types.Message, state: FSMContext):
        await bot.delete_message(message.from_user.id, message.message_id)
        await bot.delete_message(message.from_user.id, message.message_id - 1)
        async with state.proxy() as data:
            await state.update_data(vk_group_name=message.text)
            url = f"@{data.get('tg_channel_url')}" if data.get('tg_channel_url') else "URL-недоступен"
            await bot.send_message(message.from_user.id,
                                   "Отлично!\n\n"
                                   f"Название вашего ТГ-канала - <b>{data.get('tg_channel_name')}</b>\n"
                                   f"URL вашего ТГ-канала - <b>{url}</b>\n\n"
                                   f"Название вашей ВК-группы - <b>{message.text}</b>\n"
                                   f"URL вашей ВК-группы - <b>vk.com/club{data.get('vk_group_id')}</b>\n\n"
                                   "<i>Вы можете еще раз написать название ВК-группы и отправить мне </i>"
                                   "<i>сообщение.</i>\nЕсли всё верно нажмите 'Всё верно!'\n\n"
                                   "<i>Или можете вернуться в главное меню</i>",
                                   disable_web_page_preview=True,
                                   reply_markup=ClientMarkup.client_approve())

    @staticmethod
    async def client_add_bind_5(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            url = f'@{data.get("tg_channel_url")}' if data.get("tg_channel_url") else "URL-недоступен"
            bind = await setter.client_add_new_bind(callback.from_user.id,
                                                    str(data.get("tg_channel_name")),
                                                    str(data.get("tg_channel_id")),
                                                    str(url),
                                                    str(data.get("vk_group_name")),
                                                    str(data.get("vk_group_id")),
                                                    str(data.get("vk_group_url")))
            await state.update_data(bind=bind)
            await setter.client_add_new_bind_in_client_table(callback.from_user.id)
        await callback.message.edit_text("<b>Каналы успешно добавлены!</b>\n\n"
                                         "<b>Вы можете перейти к настройкам сейчас или настроить позже</b>",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_bind_start_preferences())

    @staticmethod
    async def client_add_bind_6(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind = data.get("bind")
        bind = await getter.client_select_bind(bind.id)
        binds = await getter.client_select_all_binds(callback.from_user.id)
        v = 1
        for i in binds:
            if i.id == bind.id:
                break
            else:
                v += 1
        url = "Включено" if bind.url else "Отключено"
        qty = bind.qty if bind.qty else "Отключено"
        tags = bind.tags if bind.tags else "Отсутствуют"
        opt_text = bind.opt_text if bind.opt_text else "Отсутствует"
        excl_tags = bind.excl_tags if bind.excl_tags else "Отсутствуют"
        on = f"{KEYBOARD.get('CHECK_MARK_BUTTON')} Работает" if bind.on \
            else f"{KEYBOARD.get('CROSS_MARK')} Отключено"
        await callback.message.edit_text(f"Вы вошли в связь под номером <i>{v}</i> | {on}\n\n"
                                         f"<b>Название ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_names)}</i>\n"
                                         f"<b>URL ТГ канала (ов)</b> - <i>{' | '.join(bind.tg_channels_urls)}</i>\n\n"
                                         f"<b>Название ВК групп</b> - <i>{' | '.join(bind.vk_groups_names)}</i>\n"
                                         f"<b>URL ВК групп</b> - <i>{' | '.join(bind.vk_groups_urls)}</i>\n\n"
                                         f"<b>Опции:</b>\n"
                                         f"<b>Ограничение символов</b> - <i>{qty}</i>\n"
                                         f"<b>Хэштэги</b> - <i>{tags}</i>\n"
                                         f"<b>Дополнительный текст после поста</b> - <i>{opt_text}</i>\n"
                                         f"<b>Исключение постов с указанными хэштэгами</b> - <i>{excl_tags}</i>\n"
                                         f"<b>URL-ссылка на пост</b> - <i>{url}</i>",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_change_optionals(bind.id))


class ClientSubscribe:
    @staticmethod
    async def subscribe_main(callback: types.CallbackQuery):
        client = await getter.client_select(callback.from_user.id)
        if client.subscribe_type == "paid":
            if client.access is False:
                markup = ClientMarkup.client_end_subscribe()
            else:
                markup = ClientMarkup.client_subscribe()
            binds = await getter.client_select_all_binds(callback.from_user.id)
            timed = client.subscribe - datetime.now()
            timed = "0" if str(timed)[:1] == "-" else timed.days + 1
            access = f"<b>{KEYBOARD.get('CHECK_MARK_BUTTON')} Ваша подписка активна!</b>\n" \
                     f"<b>{KEYBOARD.get('STOPWATCH')} Подписка заканчивается</b> - " \
                     f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n" \
                     f"<b>{KEYBOARD.get('STOPWATCH')} Осталось </b> - " \
                     f"<i>{timed} дней</i>\n\n" \
                     f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - " \
                     f"<i>{len(binds)}/{client.limit_binds}</i>\n" \
                if client.access else f"<b>{KEYBOARD.get('CROSS_MARK')} Ваша подписка неактивна!</b>\n" \
                                      f"<b>{KEYBOARD.get('STOPWATCH')} Подписка закончилась</b> - " \
                                      f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n\n" \
                                      f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - " \
                                      f"<i>{len(binds)}/{client.limit_binds}</i>\n"
            subscribe_type = "Промо" if client.subscribe_type == "promo" else "Платная"
            await callback.message.edit_text(
                "<b>Стандартная подписка, включающая в себя до 5 связей и весь функционал - 199р./месяц.</b>\n"
                "<b>Каждая дополнительная связь - +80р./месяц. </b>\n\n"
                f"<b>Сейчас ваш ежемесячный платёж составляет</b> - <i>{client.payment} рублей</i>\n"
                f"<b>Тип подписки</b> - <i>{subscribe_type}</i>\n\n"
                f"{access}\n",
                disable_web_page_preview=True,
                reply_markup=markup)
        elif client.subscribe_type == "start":
            await callback.message.edit_text(
                f"<b>В данный момент у вас нет Подписки</b>\n\n"
                f"<b>Вы можете попробовать Промо подписку, вам будет доступен весь функционал, "
                f"кроме увеличения максимального кол-во связей</b>\n\n"
                f"<b>Так же вы можете сразу оформить Платную подписку, "
                f"тогда у вас будет возможность увеличить макс. кол-во связей</b>\n\n"
                "<b>Платная подписка, включающая в себя до 5 связей и весь функционал - 199р./месяц.</b>\n"
                "<b>Каждая дополнительная связь - +80р./месяц. </b>\n\n"
                "<b>Выберите вариант пополнения баланса</b>",
                disable_web_page_preview=True,
                reply_markup=ClientMarkup.client_subscribe_start())
        else:
            timed = client.subscribe - datetime.now()
            timed = "0" if str(timed)[:1] == "-" else timed.days + 1
            await callback.message.edit_text(
                f"<b>В данный момент у вас Промо подписка, действующая до</b> - "
                f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n"
                f"<b>Осталось - {timed} дней</b>\n\n"
                f"<b>Перейдите на платную подписку, тогда у вас будет "
                f"возможность увеличить макс. кол-во связей </b>\n\n"
                "<b>Платная подписка, включающая в себя до 5 связей и весь функционал - 199р./месяц.</b>\n"
                "<b>Каждая дополнительная связь - +80р./месяц. </b>\n\n"
                "<b>Выберите вариант пополнения баланса</b>",
                disable_web_page_preview=True,
                reply_markup=ClientMarkup.client_subscribe_promo())

    @staticmethod
    async def client_subscribe_promo(callback: types.CallbackQuery):
        await setter.client_subscribe_promo(callback.from_user.id)
        client = await getter.client_select(callback.from_user.id)
        timed = client.subscribe - datetime.now()
        timed = "0" if str(timed)[:1] == "-" else timed.days + 1
        await callback.message.edit_text(
            f"<b>В данный момент у вас Промо подписка, действующая до</b> - "
            f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n"
            f"<b>Осталось - {timed} дней</b>\n\n"
            f"<b>Перейдите на платную подписку, тогда у вас будет "
            f"возможность увеличить макс. кол-во связей </b>\n\n"
            "<b>Платная подписка, включающая в себя до 5 связей и весь функционал - 199р./месяц.</b>\n"
            "<b>Каждая дополнительная связь - +80р./месяц. </b>\n\n"
            "<b>Выберите вариант пополнения баланса</b>",
            disable_web_page_preview=True,
            reply_markup=ClientMarkup.client_subscribe_promo())

    @staticmethod
    async def client_subscribe_paid(callback: types.CallbackQuery):
        limits = await getter.get_limits()
        await callback.message.edit_text(f"Оплата с помощью Юкасса\n\n"
                                         f"Вам нужно пополнить баланс на "
                                         f"{limits.standard_pay} рублей",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_promo(limits.standard_pay))

    @staticmethod
    async def qiwi_promo(callback: types.CallbackQuery):
        limits = await getter.get_limits()
        await callback.message.edit_text(f"Оплата с помощью QIWI\n\n"
                                         f"Вам нужно пополнить баланс на "
                                         f"{limits.standard_pay} рублей",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_promo(limits.standard_pay))

    @staticmethod
    async def yookassa_promo(callback: types.CallbackQuery):
        limits = await getter.get_limits()
        await callback.message.edit_text(f"Оплата с помощью Юкасса\n\n"
                                         f"Вам нужно пополнить баланс на "
                                         f"{limits.standard_pay} рублей",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_promo(limits.standard_pay))

    @staticmethod
    async def client_first_paid(callback: types.CallbackQuery, state: FSMContext):
        payment = str(callback.data[18:]) + "00"
        await state.update_data(first_paid="first_paid")
        # Принято! Ваши тестовые настройки:
        # shopId 506751
        # shopArticleId 538350
        # Здесь всё.
        # Теперь возвращайтесь к @BotFather — он пришлет тестовый платежный токен.
        # Для оплаты используйте данные тестовой карты: 1111 1111 1111 1026, 12/22, CVC 000.
        prices = [LabeledPrice(label="First Paid", amount=int(payment))]
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
        await bot.send_invoice(callback.from_user.id,
                               title="Основная подписка",
                               description="Основная подписка включает 5 связок",
                               payload="some_invoice",
                               currency="RUB",
                               provider_token=PAY_TOKEN,
                               prices=prices)

    @staticmethod
    async def checkout_handler(pre_checkout_query: PreCheckoutQuery):
        await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

    @staticmethod
    async def client_first_paid_1(message: types.Message, state: FSMContext):
        amount = f"{message.successful_payment.total_amount}"[:-2]
        async with state.proxy() as data:
            if data.get("first_paid"):
                await setter.client_first_paid(message.from_user.id,
                                               int(amount))
                client = await getter.client_select(message.from_user.id)
                binds = await getter.client_select_all_binds(message.from_user.id)
                timed = client.subscribe - datetime.now()
                timed = "0" if str(timed)[:1] == "-" else timed.days + 1
                access = f"<b>{KEYBOARD.get('CHECK_MARK_BUTTON')} Ваша подписка активна!</b>\n" \
                         f"<b>{KEYBOARD.get('STOPWATCH')} Подписка заканчивается</b> - " \
                         f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n" \
                         f"<b>{KEYBOARD.get('STOPWATCH')} Осталось </b> - " \
                         f"<i>{timed} дней</i>\n\n" \
                         f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - " \
                         f"<i>{len(binds)}/{client.limit_binds}</i>\n" \
                    if client.access else f"<b>{KEYBOARD.get('CROSS_MARK')} Ваша подписка неактивна!</b>\n" \
                                          f"<b>{KEYBOARD.get('STOPWATCH')} Подписка закончилась</b> - " \
                                          f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n\n" \
                                          f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - " \
                                          f"<i>{len(binds)}/{client.limit_binds}</i>\n"
                subscribe_type = "Промо" if client.subscribe_type == "promo" else "Платная"
                await bot.send_message(message.from_user.id,
                    f"<b>Вы приобрели стандартную подписку!\n\n</b>"
                    "<b>Стандартная подписка, включающая в себя до 5 связей и весь функционал - 199р./месяц.</b>\n"
                    "<b>Каждая дополнительная связь - +80р./месяц. </b>\n\n"
                    f"<b>Сейчас ваш ежемесячный платёж составляет</b> - <i>{client.payment} рублей</i>\n"
                    f"<b>Тип подписки</b> - <i>{subscribe_type}</i>\n"
                    f"{access}\n",
                    disable_web_page_preview=True,
                    reply_markup=ClientMarkup.client_subscribe())
            if data.get("paid"):
                await setter.client_paid(message.from_user.id, int(amount))
                client = await getter.client_select(message.from_user.id)
                binds = await getter.client_select_all_binds(message.from_user.id)
                timed = client.subscribe - datetime.now()
                timed = "0" if str(timed)[:1] == "-" else timed.days + 1
                access = f"<b>{KEYBOARD.get('CHECK_MARK_BUTTON')} Ваша подписка активна!</b>\n" \
                         f"<b>{KEYBOARD.get('STOPWATCH')} Подписка заканчивается</b> - " \
                         f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n" \
                         f"<b>{KEYBOARD.get('STOPWATCH')} Осталось </b> - " \
                         f"<i>{timed} дней</i>\n\n" \
                         f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - " \
                         f"<i>{len(binds)}/{client.limit_binds}</i>\n" \
                    if client.access else f"<b>{KEYBOARD.get('CROSS_MARK')} Ваша подписка неактивна!</b>\n" \
                                          f"<b>{KEYBOARD.get('STOPWATCH')} Подписка закончилась</b> - " \
                                          f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n\n" \
                                          f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - " \
                                          f"<i>{len(binds)}/{client.limit_binds}</i>\n"
                subscribe_type = "Промо" if client.subscribe_type == "promo" else "Платная"
                await bot.send_message(message.from_user.id,
                                       "<b>Стандартная подписка, включающая в себя до 5 связей и весь функционал - 199р./месяц.</b>\n"
                                       "<b>Каждая дополнительная связь - +80р./месяц. </b>\n\n"
                                       f"<b>Сейчас ваш ежемесячный платёж составляет</b> - <i>{client.payment} рублей</i>\n"
                                       f"<b>Тип подписки</b> - <i>{subscribe_type}</i>\n"
                                       f"{access}\n",
                                       disable_web_page_preview=True,
                                       reply_markup=ClientMarkup.client_subscribe())
            if data.get("add_binds_pay"):
                payment = data.get("payment")
                amount_binds = data.get("amount_binds")
                await setter.client_paid_additional_binds(message.from_user.id,
                                                          int(payment),
                                                          int(amount_binds))
                client = await getter.client_select(message.from_user.id)
                binds = await getter.client_select_all_binds(message.from_user.id)
                timed = client.subscribe - datetime.now()
                timed = "0" if str(timed)[:1] == "-" else timed.days + 1
                access = f"<b>{KEYBOARD.get('CHECK_MARK_BUTTON')} Ваша подписка активна!</b>\n" \
                         f"<b>{KEYBOARD.get('STOPWATCH')} Подписка заканчивается</b> - " \
                         f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n" \
                         f"<b>{KEYBOARD.get('STOPWATCH')} Осталось </b> - " \
                         f"<i>{timed} дней</i>\n\n" \
                         f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - " \
                         f"<i>{len(binds)}/{client.limit_binds}</i>\n" \
                    if client.access else f"<b>{KEYBOARD.get('CROSS_MARK')} Ваша подписка неактивна!</b>\n" \
                                          f"<b>{KEYBOARD.get('STOPWATCH')} Подписка закончилась</b> - " \
                                          f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n\n" \
                                          f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - " \
                                          f"<i>{len(binds)}/{client.limit_binds}</i>\n"
                subscribe_type = "Промо" if client.subscribe_type == "promo" else "Платная"
                await bot.send_message(message.from_user.id,
                                       f"<b>Вы добавили количество связей</b> - <i>{amount_binds}</i>\n\n"
                                       "<b>Стандартная подписка, включающая в себя до 5 связей и весь функционал - 199р./месяц.</b>\n"
                                       "<b>Каждая дополнительная связь - +80р./месяц. </b>\n\n"
                                       f"<b>Сейчас ваш ежемесячный платёж составляет</b> - <i>{client.payment} рублей</i>\n"
                                       f"<b>Тип подписки</b> - <i>{subscribe_type}</i>\n"
                                       f"{access}\n",
                                       disable_web_page_preview=True,
                                       reply_markup=ClientMarkup.client_subscribe())

    @staticmethod
    async def qiwi_paid(callback: types.CallbackQuery):
        client = await getter.client_select(callback.from_user.id)
        await callback.message.edit_text(f"Оплата с помощью QIWI\n\n"
                                         f"Вам нужно пополнить баланс на "
                                         f"{client.payment} рублей",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_paid(client.payment))

    @staticmethod
    async def yookassa_paid(callback: types.CallbackQuery):
        client = await getter.client_select(callback.from_user.id)
        await callback.message.edit_text(f"Оплата с помощью Юкасса\n\n"
                                         f"Вам нужно пополнить баланс на "
                                         f"{client.payment} рублей",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_paid(client.payment))

    @staticmethod
    async def client_paid(callback: types.CallbackQuery, state: FSMContext):
        payment = str(callback.data[12:]) + "00"
        prices = [LabeledPrice(label="Paid", amount=int(payment))]
        await state.update_data(paid="paid")
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
        await bot.send_invoice(callback.from_user.id,
                               title="Платёж",
                               description=f"Вам нужно пополнить баланс на {payment[:-2]} рублей",
                               payload="some_invoice",
                               currency="RUB",
                               provider_token=PAY_TOKEN,
                               prices=prices)

    @staticmethod
    async def client_add_limit_binds(callback: types.CallbackQuery):
        client = await getter.client_select(callback.from_user.id)
        limits = await getter.get_limits()
        timed = client.subscribe - datetime.now()
        timed = "0" if str(timed)[:1] == "-" else timed.days + 1
        await callback.message.edit_text(f"Ваш следующий платёж будет "
                                         f"{client.subscribe.strftime('%d %B %Y')}\n"
                                         f"Осталось - {timed} дней\n"
                                         f"За 1 доп связь нужно заплатить {limits.add_pay} рублей за 30 дней\n"
                                         f"Выберите кол-во связей",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_add_limit_binds())

    @staticmethod
    async def client_add_limit_binds_1(callback: types.CallbackQuery):
        client = await getter.client_select(callback.from_user.id)
        limits = await getter.get_limits()
        days = client.subscribe - datetime.now()
        amount_binds = callback.data[23:]
        days = "0" if str(days)[:1] == "-" else days.days + 1
        result = round((limits.add_pay / 30) * days, 2)
        result_money = int(result) * int(amount_binds)
        await callback.message.edit_text(f"Вам нужно заплатить {result_money} рублей за {amount_binds} связей\n"
                                         f"На оставшиеся на этом месяце подписке {days} дней\n"
                                         f"В следующем месяце будет формироваться новая цена подписки",
                                         disable_web_page_preview=True,
                                         reply_markup=ClientMarkup.client_paid_additional_binds(result_money,
                                                                                                amount_binds))

    @staticmethod
    async def client_add_limit_binds_2(callback: types.CallbackQuery, state: FSMContext):
        payment = str(callback.data[19:]) + "00"
        await state.update_data(amount_binds=callback.data[:1],
                                payment=payment,
                                add_binds_pay="add_binds_pay")
        prices = [LabeledPrice(label="Paid", amount=int(payment))]
        await bot.delete_message(callback.from_user.id, callback.message.message_id)
        await bot.send_invoice(callback.from_user.id,
                               title="Платёж",
                               description=f"Вам нужно пополнить баланс на {payment[:-2]} рублей",
                               payload="some_invoice",
                               currency="RUB",
                               provider_token=PAY_TOKEN,
                               prices=prices)

    @staticmethod
    async def client_delete_limit_binds(callback: types.CallbackQuery):
        client = await getter.client_select(callback.from_user.id)
        limits = await getter.get_limits()
        if client.limit_binds <= limits.bind_limit:
            client = await getter.client_select(callback.from_user.id)
            binds = await getter.client_select_all_binds(callback.from_user.id)
            timed = client.subscribe - datetime.now()
            timed = "0" if str(timed)[:1] == "-" else timed.days + 1
            access = f"<b>{KEYBOARD.get('CHECK_MARK_BUTTON')} Ваша подписка активна!</b>\n" \
                     f"<b>{KEYBOARD.get('STOPWATCH')} Подписка заканчивается</b> - " \
                     f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n" \
                     f"<b>{KEYBOARD.get('STOPWATCH')} Осталось </b> - " \
                     f"<i>{timed} дней</i>\n\n" \
                     f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - " \
                     f"<i>{len(binds)}/{client.limit_binds}</i>\n" \
                if client.access else f"<b>{KEYBOARD.get('CROSS_MARK')} Ваша подписка неактивна!</b>\n" \
                                      f"<b>{KEYBOARD.get('STOPWATCH')} Подписка закончилась</b> - " \
                                      f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n\n" \
                                      f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - " \
                                      f"<i>{len(binds)}/{client.limit_binds}</i>\n"
            subscribe_type = "Промо" if client.subscribe_type == "promo" else "Платная"
            await callback.message.edit_text(
                "<b>Невозможно удалить связи меньше стандарта !</b>\n\n"
                "<b>Стандартная подписка, включающая в себя до 5 связей и весь функционал - 199р./месяц.</b>\n"
                "<b>Каждая дополнительная связь - +80р./месяц. </b>\n\n"
                f"<b>Сейчас ваш ежемесячный платёж составляет</b> - <i>{client.payment} рублей</i>\n"
                f"<b>Тип подписки</b> - <i>{subscribe_type}</i>\n\n"
                f"{access}\n",
                disable_web_page_preview=True,
                reply_markup=ClientMarkup.client_subscribe())
        else:
            await callback.message.edit_text("Выберите кол-во связей добавить",
                                             disable_web_page_preview=True,
                                             reply_markup=ClientMarkup.client_delete_limit_binds())

    @staticmethod
    async def client_delete_limit_binds_1(callback: types.CallbackQuery):
        limit = callback.data[26:]
        await setter.client_delete_limit_binds(callback.from_user.id, int(limit))
        client = await getter.client_select(callback.from_user.id)
        binds = await getter.client_select_all_binds(callback.from_user.id)
        timed = client.subscribe - datetime.now()
        timed = "0" if str(timed)[:1] == "-" else timed.days + 1
        access = f"<b>{KEYBOARD.get('CHECK_MARK_BUTTON')} Ваша подписка активна!</b>\n" \
                 f"<b>{KEYBOARD.get('STOPWATCH')} Подписка заканчивается</b> - " \
                 f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n" \
                 f"<b>{KEYBOARD.get('STOPWATCH')} Осталось </b> - " \
                 f"<i>{timed} дней</i>\n\n" \
                 f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - " \
                 f"<i>{len(binds)}/{client.limit_binds}</i>\n" \
            if client.access else f"<b>{KEYBOARD.get('CROSS_MARK')} Ваша подписка неактивна!</b>\n" \
                                  f"<b>{KEYBOARD.get('STOPWATCH')} Подписка закончилась</b> - " \
                                  f"<i>{client.subscribe.strftime('%d-%m-%Y, %H:%M:%S')}</i>\n\n" \
                                  f"<b>{KEYBOARD.get('LINKED_PAPERCLIPS')} Количество связей</b> - " \
                                  f"<i>{len(binds)}/{client.limit_binds}</i>\n"
        subscribe_type = "Промо" if client.subscribe_type == "promo" else "Платная"
        await callback.message.edit_text(
            f"<b>Вы удалили количество связей</b> - <i>{limit}</i>\n\n"
            "<b>Стандартная подписка, включающая в себя до 5 связей и весь функционал - 199р./месяц.</b>\n"
            "<b>Каждая дополнительная связь - +80р./месяц. </b>\n\n"
            f"<b>Сейчас ваш ежемесячный платёж составляет</b> - <i>{client.payment} рублей</i>\n"
            f"<b>Тип подписки</b> - <i>{subscribe_type}</i>\n\n"
            f"{access}\n",
            disable_web_page_preview=True,
            reply_markup=ClientMarkup.client_subscribe())
