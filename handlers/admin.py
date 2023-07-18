import csv
from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InputFile
from aiogram.utils.deep_linking import get_start_link

from bot import bot
from markups.admin_markup import AdminMarkup
from data.commands import getter, setter
from states import states
from settings.config import KEYBOARD


class AdminMain:
    @staticmethod
    async def admin_main(callback: types.CallbackQuery, state: FSMContext):
        await state.finish()
        await callback.message.edit_text("<b>Добро пожаловать в меню Администратора</b>\n\n"
                                         "<b>Вы можете просмотреть список пользователей, "
                                         "список связей, найти пользователя, изменения лимитов.</b>\n\n",
                                         reply_markup=AdminMarkup.admin_menu())


class AdminLimits:
    @staticmethod
    async def admin_limits(callback: types.CallbackQuery):
        limits = await getter.get_limits()
        await callback.message.edit_text("Что будем менять ?\n\n"
                                         "Сейчас установлены такие лимиты:\n"
                                         f"Стандартный платёж - <b>{limits.standard_pay}</b>\n"
                                         f"Доп платёж - <b>{limits.add_pay}</b>\n"
                                         f"Лимит связей - <b>{limits.bind_limit}</b>",
                                         reply_markup=AdminMarkup.admin_change_limits())

    @staticmethod
    async def admin_change_standard(callback: types.CallbackQuery):
        limits = await getter.get_limits()
        await callback.message.edit_text("Сейчас установлен такой лимит:\n"
                                         f"Стандартный платёж - <b>{limits.standard_pay}</b>\n\n"
                                         f"Введите натуральное число, чтобы установить новый "
                                         f"Стандартный платёж\n\n"
                                         f"<i>Или можете вернуться в главное меню изменения лимитов</i>",
                                         reply_markup=AdminMarkup.admin_back_limit_menu())
        await states.AdminLimits.standard_pay.set()

    @staticmethod
    async def admin_change_standard_1(message: types.Message, state: FSMContext):
        if message.text.isdigit():
            await state.finish()
            await setter.admin_set_new_standard_payment(int(message.text))
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            limits = await getter.get_limits()
            await bot.send_message(message.from_user.id,
                                   "<b>Стандартный платёж успешно изменен!</b>\n\n"
                                   "Что будем менять ?\n\n"
                                   "Сейчас установлены такие лимиты:\n"
                                   f"Стандартный платёж - <b>{limits.standard_pay}</b>\n"
                                   f"Доп платёж - <b>{limits.add_pay}</b>\n"
                                   f"Лимит связей - <b>{limits.bind_limit}</b>",
                                   reply_markup=AdminMarkup.admin_change_limits())
        else:
            limits = await getter.get_limits()
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   f"<b>Надо ввести натуральное число!</b>\n\n"
                                   f"Стандартный платёж - <b>{limits.standard_pay}</b>\n\n"
                                   f"Введите натуральное число, чтобы установить новый "
                                   f"Стандартный платёж\n\n"
                                   f"<i>Или можете вернуться в главное меню изменения лимитов</i>",
                                   reply_markup=AdminMarkup.admin_back_limit_menu())

    @staticmethod
    async def admin_change_add(callback: types.CallbackQuery):
        limits = await getter.get_limits()
        await callback.message.edit_text("Сейчас установлен такой лимит:\n"
                                         f"Доп. платёж - <b>{limits.add_pay}</b>\n\n"
                                         f"Введите натуральное число, чтобы установить новый "
                                         f"Доп. платёж\n\n"
                                         f"<i>Или можете вернуться в главное меню изменения лимитов</i>",
                                         reply_markup=AdminMarkup.admin_back_limit_menu())
        await states.AdminLimits.add_pay.set()

    @staticmethod
    async def admin_change_add_1(message: types.Message, state: FSMContext):
        if message.text.isdigit():
            await state.finish()
            await setter.admin_set_new_add_payment(int(message.text))
            limits = await getter.get_limits()
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   "<b>Доп. платёж успешно изменен!</b>\n\n"
                                   "Что будем менять ?\n\n"
                                   "Сейчас установлены такие лимиты:\n"
                                   f"Стандартный платёж - <b>{limits.standard_pay}</b>\n"
                                   f"Доп платёж - <b>{limits.add_pay}</b>\n"
                                   f"Лимит связей - <b>{limits.bind_limit}</b>",
                                   reply_markup=AdminMarkup.admin_change_limits())
        else:
            limits = await getter.get_limits()
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   f"<b>Надо ввести натуральное число!</b>\n\n"
                                   f"Доп. платёж - <b>{limits.add_pay}</b>\n\n"
                                   f"Введите натуральное число, чтобы установить новый "
                                   f"Доп. платёж\n\n"
                                   f"<i>Или можете вернуться в главное меню изменения лимитов</i>",
                                   reply_markup=AdminMarkup.admin_back_limit_menu())

    @staticmethod
    async def admin_change_bind_limit(callback: types.CallbackQuery):
        limits = await getter.get_limits()
        await callback.message.edit_text("Сейчас установлен такой лимит:\n"
                                         f"Лимит по связям - <b>{limits.bind_limit}</b>\n\n"
                                         f"Введите натуральное число, чтобы установить новый "
                                         f"лимит по связям\n\n"
                                         f"<i>Или можете вернуться в главное меню изменения лимитов</i>",
                                         reply_markup=AdminMarkup.admin_back_limit_menu())
        await states.AdminLimits.bind_limit.set()

    @staticmethod
    async def admin_change_bind_limit_1(message: types.Message, state: FSMContext):
        if message.text.isdigit():
            await state.finish()
            await setter.admin_set_new_bind_limit(int(message.text))
            limits = await getter.get_limits()
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   "<b>Лимит по связям успешно изменен!</b>\n\n"
                                   "Что будем менять ?\n\n"
                                   "Сейчас установлены такие лимиты:\n"
                                   f"Стандартный платёж - <b>{limits.standard_pay}</b>\n"
                                   f"Доп платёж - <b>{limits.add_pay}</b>\n"
                                   f"Лимит связей - <b>{limits.bind_limit}</b>",
                                   reply_markup=AdminMarkup.admin_change_limits())
        else:
            limits = await getter.get_limits()
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   f"<b>Надо ввести натуральное число!</b>\n\n"
                                   f"Лимит по связям - <b>{limits.bind_limit}</b>\n\n"
                                   f"Введите натуральное число, чтобы установить новый "
                                   f"Лимит по связям\n\n"
                                   f"<i>Или можете вернуться в главное меню изменения лимитов</i>",
                                   reply_markup=AdminMarkup.admin_back_limit_menu())


class AdminUserList:
    @staticmethod
    async def admin_user_list(callback: types.CallbackQuery, state: FSMContext):
        user_list = await getter.get_all_clients()
        book = []
        i = 0
        while True:
            book.append(f"<b>ID</b> - <i>{user_list[i].id}</i>\n"
                        f"<b>ID пользователя</b> - <i>{user_list[i].user_id}</i>\n"
                        f"<b>Username пользователя</b> - "
                        f"{f'@{user_list[i].username}' if user_list[i].username is not None else 'Не указано'}\n"
                        f"<b>Доступ</b> - <i>{user_list[i].access}</i>\n"
                        f"<b>Кол-во связей</b> - <i>{user_list[i].binds}</i>\n"
                        f"<b>Лимит связей</b> - <i>{user_list[i].limit_binds}</i>\n\n")
            user_list.pop(i)
            if len(book) == 5 or user_list == []:
                break
        if not user_list:
            await callback.message.edit_text("".join(book),
                                             reply_markup=AdminMarkup.admin_back_main_menu())
        else:
            await callback.message.edit_text("".join(book),
                                             reply_markup=AdminMarkup.admin_user_list())
            async with state.proxy() as data:
                data["user_list"] = user_list

    @staticmethod
    async def admin_user_list_next(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            user_list = data.get("user_list")
        book = []
        while True:
            book.append(f"<b>ID</b> - <i>{user_list[0].id}</i>\n"
                        f"<b>ID пользователя</b> - <i>{user_list[0].user_id}</i>\n"
                        f"<b>Username пользователя</b> - "
                        f"{f'@{user_list[0].username}' if user_list[0].username is not None else 'Не указано'}\n"
                        f"<b>Доступ</b> - <i>{user_list[0].access}</i>\n"
                        f"<b>Кол-во связей</b> - <i>{user_list[0].binds}</i>\n"
                        f"<b>Лимит связей</b> - <i>{user_list[0].limit_binds}</i>\n\n")
            user_list.pop(0)
            if len(book) == 5 or user_list == []:
                break
        if not user_list:
            await callback.message.edit_text("".join(book),
                                             reply_markup=AdminMarkup.admin_user_list_back())
        else:
            await callback.message.edit_text("".join(book),
                                             reply_markup=AdminMarkup.admin_user_list())
            async with state.proxy() as data:
                data["user_list"] = user_list

    @staticmethod
    async def admin_user_sub_type(callback: types.CallbackQuery):
        user_list = await getter.get_all_clients()

        if user_list:
            total = {}
            for user in user_list:
                if user.subscribe_type in total:
                    total[user.subscribe_type] += 1
                else:
                    total[user.subscribe_type] = 1

            text = ''
            for t, c in total.items():
                text += f'<b>{t}:</b> {c}\n'

            text += f'\n<b>Не заблокировали бота:</b> {len([i for i in user_list if i.subscribe_type != "blocked"])}\n'
            text += f'<b>Всего:</b> {len(user_list)}'
        else:
            text = 'Пользователи не найдены'

        await callback.message.edit_text(text, reply_markup=AdminMarkup.admin_back_main_menu())

    @staticmethod
    async def admin_user_block(callback: types.CallbackQuery):
        user_list = await getter.get_clients_by_block_status(True)

        if user_list:
            text = f'<b>Всего заблокировали:</b>\n{len(user_list)}'
        else:
            text = 'Пользователи не найдены'

        await callback.message.edit_text(text, reply_markup=AdminMarkup.admin_back_main_menu())


class AdminBindList:
    @staticmethod
    async def admin_bind_list(callback: types.CallbackQuery, state: FSMContext):
        bind_list = await getter.get_all_binds()
        book = []
        while True:
            book.append(f"<b>ID</b> - <i>{bind_list[0].id}</i>\n"
                        f"<b>ID владельца</b> - <i>{bind_list[0].owner_id}</i>\n"
                        f"<b>TG channels names</b> - <i>{bind_list[0].tg_channels_names}</i>\n"
                        f"<b>TG channels IDs</b> - <i>{bind_list[0].tg_channels_ids}</i>\n"
                        f"<b>VK groups names</b> - <i>{bind_list[0].vk_groups_names}</i>\n"
                        f"<b>VK groups IDs</b> - <i>{bind_list[0].vk_groups_ids}</i>\n"
                        f"<b>Ограничения символов</b> - <i>{bind_list[0].qty}</i>\n"
                        f"<b>Хэштэги</b> - {bind_list[0].tags}\n"
                        f"<b>Доп. текст</b> - {bind_list[0].opt_text}\n"
                        f"<b>Исключающие тэги</b> - {bind_list[0].excl_tags}\n"
                        f"<b>URL</b> - {bool(bind_list[0].url)}\n"
                        f"<b>Связь в работе</b> - {bind_list[0].on}\n\n")
            bind_list.pop(0)
            if len(book) == 5 or bind_list == []:
                break
        if not bind_list:
            await callback.message.edit_text("".join(book),
                                             reply_markup=AdminMarkup.admin_back_main_menu())
        else:
            await callback.message.edit_text("".join(book),
                                             reply_markup=AdminMarkup.admin_bind_list())
            async with state.proxy() as data:
                data["bind_list"] = bind_list

    @staticmethod
    async def admin_bind_list_next(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind_list = data.get("bind_list")
        book = []
        while True:
            book.append(f"<b>ID</b> - <i>{bind_list[0].id}</i>\n"
                        f"<b>ID владельца</b> - <i>{bind_list[0].owner_id}</i>\n"
                        f"<b>TG channels names</b> - <i>{bind_list[0].tg_channels_names}</i>\n"
                        f"<b>TG channels IDs</b> - <i>{bind_list[0].tg_channels_ids}</i>\n"
                        f"<b>VK groups names</b> - <i>{bind_list[0].vk_groups_names}</i>\n"
                        f"<b>VK groups IDs</b> - <i>{bind_list[0].vk_groups_ids}</i>\n"
                        f"<b>Ограничения символов</b> - <i>{bind_list[0].qty}</i>\n"
                        f"<b>Хэштэги</b> - <i>{bind_list[0].tags}</i>\n"
                        f"<b>Доп. текст</b> - <i>{bind_list[0].opt_text}</i>\n"
                        f"<b>Исключающие тэги</b> - <i>{bind_list[0].excl_tags}</i>\n"
                        f"<b>URL</b> - <i>{bool(bind_list[0].url)}</i>\n"
                        f"<b>Связь в работе</b> - <i>{bind_list[0].on}</i>\n\n")
            bind_list.pop(0)
            if len(book) == 5 or bind_list == []:
                break
        if not bind_list:
            await callback.message.edit_text("".join(book),
                                             reply_markup=AdminMarkup.admin_bind_list_back())
        else:
            await callback.message.edit_text("".join(book),
                                             reply_markup=AdminMarkup.admin_bind_list())
            async with state.proxy() as data:
                data["bind_list"] = bind_list


class AdminFindUser:
    @staticmethod
    async def admin_find_user(callback: types.CallbackQuery, state: FSMContext):
        await state.finish()
        await callback.message.edit_text("Выберите метод поиска пользователя",
                                         reply_markup=AdminMarkup.admin_find_user())

    @staticmethod
    async def admin_find_id(callback: types.CallbackQuery):
        await callback.message.edit_text("Введите ID пользователя",
                                         reply_markup=AdminMarkup.admin_find_user_back())
        await states.AdminFind.find_id.set()

    @staticmethod
    async def admin_find_id_1(message: types.Message, state: FSMContext):
        if message.text.isdigit():
            user_id = int(message.text)
            client = await getter.client_select(user_id)
            await state.update_data(client=client)
            if client:
                try:
                    await bot.delete_message(message.from_user.id, message.message_id)
                    await bot.delete_message(message.from_user.id, message.message_id - 1)
                except:
                    pass
                start = False
                block = ""
                subscribe_type = ""
                subscribe = ""
                payment = ""
                timed = ""
                if client.block is True:
                    block = f"<b>{KEYBOARD.get('CROSS_MARK')} Пользователь Заблокирован!</b>\n\n"
                if client.payment:
                    payment = f"<i>Ежемесячный платёж</i> - <b>{client.payment}</b>\n"
                if client.subscribe_type == "start":
                    start = True
                    subscribe_type = "<b>Стартовый</b>\n"
                if client.subscribe_type == "promo":
                    subscribe_type = "<b>Пробный период</b>\n"
                    subscribe = client.subscribe - datetime.now()
                    subscribe = "" if str(subscribe)[:1] == "-" \
                        else f"<b>Действует до {client.subscribe.strftime('%d-%m-%Y')}</b>\n"
                    timed = client.subscribe - datetime.now()
                    timed = f"<b>Пробный период закончился {str(timed.days)[1:]} д. назад\n</b>" \
                        if str(timed)[:1] == "-" else f"<b>Осталось дней</b> - <i>{timed.days + 1}</i>\n"
                if client.subscribe_type == "paid":
                    subscribe_type = "<b>Оплаченный</b>\n"
                    subscribe = client.subscribe - datetime.now()
                    subscribe = f"<i>Подписка закончилась</i> - <b>{client.subscribe.strftime('%d-%m-%Y')}</b>\n" \
                        if str(subscribe)[:1] == "-" \
                        else f"<i>Действует до</i> - <b>{client.subscribe.strftime('%d-%m-%Y')}</b>\n"
                    timed = client.subscribe - datetime.now()
                    timed = f"<i>Оплаченный период закончился</i> - <b>{str(timed.days)[1:]} д. назад\n</b>" \
                        if str(timed)[:1] == "-" else f"<i>Осталось дней</i> - <b>{timed.days + 1}</b>\n"
                if client.payment is None:
                    payment = "<b>Не оплачивал</b>\n"
                await bot.send_message(message.from_user.id,
                                       "<b>Данные пользователя</b>\n\n"
                                       f"{block}"
                                       f"<i>User ID</i> - <b>{client.user_id}</b>\n"
                                       f"<i>Username</i> - "
                                       f"{f'@{client.username}' if client.username is not None else 'Не указано'}\n\n"
                                       f"<i>Тип подписки</i> - {subscribe_type}"
                                       f"{payment}"
                                       f"{subscribe}"
                                       f"{timed}\n"
                                       f"<b>Кол-во связей</b> - <i>{client.binds}</i>\n"
                                       f"<b>Лимит связей</b> - <i>{client.limit_binds}</i>\n",
                                       reply_markup=AdminMarkup.admin_enter_find_user(start,
                                                                                      client.block,
                                                                                      client.payment))
            else:
                await bot.delete_message(message.from_user.id, message.message_id)
                await bot.delete_message(message.from_user.id, message.message_id - 1)
                await bot.send_message(message.from_user.id,
                                       "Пользователь не найден!",
                                       reply_markup=AdminMarkup.admin_find_user())
        else:
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   "Надо ввести число!",
                                   reply_markup=AdminMarkup.admin_find_user())

    @staticmethod
    async def admin_find_username(callback: types.CallbackQuery):
        await callback.message.edit_text("Введите username пользователя",
                                         reply_markup=AdminMarkup.admin_find_user_back())
        await states.AdminFind.find_username.set()

    @staticmethod
    async def admin_find_username_1(message: types.Message, state: FSMContext):
        if message.text[0] == '@':
            username = message.text[1:]
        else:
            username = message.text
        client = await getter.admin_select_username(username)
        await state.update_data(client=client)
        if client:
            try:
                await bot.delete_message(message.from_user.id, message.message_id)
                await bot.delete_message(message.from_user.id, message.message_id - 1)
            except:
                pass
            start = False
            block = ""
            subscribe_type = ""
            subscribe = ""
            payment = ""
            timed = ""
            if client.block is True:
                block = f"<b>{KEYBOARD.get('CROSS_MARK')} Пользователь Заблокирован!</b>\n\n"
            if client.payment:
                payment = f"<i>Ежемесячный платёж</i> - <b>{client.payment}</b>\n"
            if client.subscribe_type == "start":
                start = True
                subscribe_type = "<b>Стартовый</b>\n"
            if client.subscribe_type == "promo":
                subscribe_type = "<b>Пробный период</b>\n"
                subscribe = client.subscribe - datetime.now()
                subscribe = "" if str(subscribe)[:1] == "-" \
                    else f"<b>Действует до {client.subscribe.strftime('%d-%m-%Y')}</b>\n"
                timed = client.subscribe - datetime.now()
                timed = f"<b>Пробный период закончился {str(timed.days)[1:]} д. назад\n</b>" \
                    if str(timed)[:1] == "-" else f"<b>Осталось дней</b> - <i>{timed.days + 1}</i>\n"
            if client.subscribe_type == "paid":
                subscribe_type = "<b>Оплаченный</b>\n"
                subscribe = client.subscribe - datetime.now()
                subscribe = f"<i>Подписка закончилась</i> - <b>{client.subscribe.strftime('%d-%m-%Y')}</b>\n" \
                    if str(subscribe)[:1] == "-" \
                    else f"<i>Действует до</i> - <b>{client.subscribe.strftime('%d-%m-%Y')}</b>\n"
                timed = client.subscribe - datetime.now()
                timed = f"<i>Оплаченный период закончился</i> - <b>{str(timed.days)[1:]} д. назад\n</b>" \
                    if str(timed)[:1] == "-" else f"<i>Осталось дней</i> - <b>{timed.days + 1}</b>\n"
            if client.payment is None:
                payment = "<b>Не оплачивал</b>\n"
            await bot.send_message(message.from_user.id,
                                   "<b>Данные пользователя</b>\n\n"
                                   f"{block}"
                                   f"<i>User ID</i> - <b>{client.user_id}</b>\n"
                                   f"<i>Username</i> - "
                                   f"{f'@{client.username}' if client.username is not None else 'Не указано'}\n\n"
                                   f"<i>Тип подписки</i> - {subscribe_type}"
                                   f"{payment}"
                                   f"{subscribe}"
                                   f"{timed}\n"
                                   f"<b>Кол-во связей</b> - <i>{client.binds}</i>\n"
                                   f"<b>Лимит связей</b> - <i>{client.limit_binds}</i>\n",
                                   reply_markup=AdminMarkup.admin_enter_find_user(start,
                                                                                  client.block,
                                                                                  client.payment))
        else:
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   "Пользователь не найден!",
                                   reply_markup=AdminMarkup.admin_find_user())

    @staticmethod
    async def admin_bind_list_user(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            client = data.get("client")
            bind_list = await getter.client_select_all_binds(client.user_id)
        if bind_list:
            book = []
            while True:
                book.append(f"<b>ID связи</b> - <i>{bind_list[0].id}</i>\n"
                            f"<b>TG channels names</b> - <i>{bind_list[0].tg_channels_names}</i>\n"
                            f"<b>TG channels IDs</b> - <i>{bind_list[0].tg_channels_ids}</i>\n"
                            f"<b>VK groups names</b> - <i>{bind_list[0].vk_groups_names}</i>\n"
                            f"<b>VK groups IDs</b> - <i>{bind_list[0].vk_groups_ids}</i>\n"
                            f"<b>Ограничения символов</b> - <i>{bind_list[0].qty}</i>\n"
                            f"<b>Хэштэги</b> - <i>{bind_list[0].tags}</i>\n"
                            f"<b>Доп. текст</b> - <i>{bind_list[0].opt_text}</i>\n"
                            f"<b>Исключающие тэги</b> - <i>{bind_list[0].excl_tags}</i>\n"
                            f"<b>URL</b> - <i>{bool(bind_list[0].url)}</i>\n"
                            f"<b>Связь в работе</b> - <i>{bind_list[0].on}</i>\n\n")
                bind_list.pop(0)
                if len(book) == 3 or bind_list == []:
                    break
            if not bind_list:
                await callback.message.edit_text("".join(book),
                                                 reply_markup=AdminMarkup.admin_back_user())
            else:
                await callback.message.edit_text("".join(book),
                                                 reply_markup=AdminMarkup.admin_bind_list_user())
                async with state.proxy() as data:
                    data["bind_list"] = bind_list
        else:
            await callback.message.edit_text("Связей нет",
                                             reply_markup=AdminMarkup.admin_back_to_find_user())

    @staticmethod
    async def admin_bind_list_user_next(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            bind_list = data.get("bind_list")
        book = []
        while True:
            book.append(f"<b>ID связи</b> - <i>{bind_list[0].id}</i>\n"
                        f"<b>TG channels names</b> - <i>{bind_list[0].tg_channels_names}</i>\n"
                        f"<b>TG channels IDs</b> - <i>{bind_list[0].tg_channels_ids}</i>\n"
                        f"<b>VK groups names</b> - <i>{bind_list[0].vk_groups_names}</i>\n"
                        f"<b>VK groups IDs</b> - <i>{bind_list[0].vk_groups_ids}</i>\n"
                        f"<b>Ограничения символов</b> - <i>{bind_list[0].qty}</i>\n"
                        f"<b>Хэштэги</b> - <i>{bind_list[0].tags}</i>\n"
                        f"<b>Доп. текст</b> - <i>{bind_list[0].opt_text}</i>\n"
                        f"<b>Исключающие тэги</b> - <i>{bind_list[0].excl_tags}</i>\n"
                        f"<b>URL</b> - <i>{bool(bind_list[0].url)}</i>\n"
                        f"<b>Связь в работе</b> - <i>{bind_list[0].on}</i>\n\n")
            bind_list.pop(0)
            if len(book) == 3 or bind_list == []:
                break
        if not bind_list:
            await callback.message.edit_text("".join(book),
                                             reply_markup=AdminMarkup.admin_bind_list_user_back())
        else:
            await callback.message.edit_text("".join(book),
                                             reply_markup=AdminMarkup.admin_bind_list_user())
            async with state.proxy() as data:
                data["bind_list"] = bind_list

    @staticmethod
    async def admin_back_user(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            client = data.get("client")
        client = await getter.client_select(client.user_id)
        await state.update_data(client=client)
        start = False
        block = ""
        subscribe_type = ""
        subscribe = ""
        payment = ""
        timed = ""
        if client.block is True:
            block = f"<b>{KEYBOARD.get('CROSS_MARK')} Пользователь Заблокирован!</b>\n\n"
        if client.payment:
            payment = f"<i>Ежемесячный платёж</i> - <b>{client.payment}</b>\n"
        if client.subscribe_type == "start":
            start = True
            subscribe_type = "<b>Стартовый</b>\n"
        if client.subscribe_type == "promo":
            subscribe_type = "<b>Пробный период</b>\n"
            subscribe = client.subscribe - datetime.now()
            subscribe = "" if str(subscribe)[:1] == "-" \
                else f"<b>Действует до {client.subscribe.strftime('%d-%m-%Y')}</b>\n"
            timed = client.subscribe - datetime.now()
            timed = f"<b>Пробный период закончился {str(timed.days)[1:]} д. назад\n</b>" \
                if str(timed)[:1] == "-" else f"<b>Осталось дней</b> - <i>{timed.days + 1}</i>\n"
        if client.subscribe_type == "paid":
            subscribe_type = "<b>Оплаченный</b>\n"
            subscribe = client.subscribe - datetime.now()
            subscribe = f"<i>Подписка закончилась</i> - <b>{client.subscribe.strftime('%d-%m-%Y')}</b>\n" \
                if str(subscribe)[:1] == "-" \
                else f"<i>Действует до</i> - <b>{client.subscribe.strftime('%d-%m-%Y')}</b>\n"
            timed = client.subscribe - datetime.now()
            timed = f"<i>Оплаченный период закончился</i> - <b>{str(timed.days)[1:]} д. назад\n</b>" \
                if str(timed)[:1] == "-" else f"<i>Осталось дней</i> - <b>{timed.days + 1}</b>\n"
        if client.payment is None:
            payment = "<b>Не оплачивал</b>\n"
        await callback.message.edit_text("<b>Данные пользователя</b>\n\n"
                                         f"{block}"
                                         f"<i>User ID</i> - <b>{client.user_id}</b>\n"
                                         f"<i>Username</i> - "
                                         f"{f'@{client.username}' if client.username is not None else 'Не указано'}\n\n"
                                         f"<i>Тип подписки</i> - {subscribe_type}"
                                         f"{payment}"
                                         f"{subscribe}"
                                         f"{timed}\n"
                                         f"<b>Кол-во связей</b> - <i>{client.binds}</i>\n"
                                         f"<b>Лимит связей</b> - <i>{client.limit_binds}</i>\n",
                                         reply_markup=AdminMarkup.admin_enter_find_user(start,
                                                                                        client.block,
                                                                                        client.payment))

    @staticmethod
    async def admin_change_user_month_payment(callback: types.CallbackQuery):
        await callback.message.edit_text("Введите стоимость мес. подписки для этого пользователя",
                                         reply_markup=AdminMarkup.admin_back_user())
        await states.AdminFind.change_month_payment.set()

    @staticmethod
    async def admin_change_user_month_payment_1(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            client = data.get("client")
        if message.text.isdigit():
            await setter.admin_set_new_month_payment_for_user(client.user_id,
                                                              int(message.text))
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   "Индивидуальный платёж изменен!",
                                   reply_markup=AdminMarkup.admin_back_user())
        else:
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id - 1)
            await bot.send_message(message.from_user.id,
                                   "Надо ввести число!",
                                   reply_markup=AdminMarkup.admin_back_user())

    @staticmethod
    async def admin_delete_user(callback: types.CallbackQuery):
        await callback.message.edit_text("Вы уверены что хотите удалить пользователя ?",
                                         reply_markup=AdminMarkup.admin_delete_user())

    @staticmethod
    async def admin_delete_user_1(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            client = data.get("client")
        await setter.admin_delete_user(client.user_id)
        await callback.message.edit_text("Пользователь удалён!",
                                         reply_markup=AdminMarkup.admin_menu())
        await state.finish()

    @staticmethod
    async def admin_block_user(callback: types.CallbackQuery):
        await callback.message.edit_text("Вы уверены что хотите заблокировать пользователя ?",
                                         reply_markup=AdminMarkup.admin_block_user())

    @staticmethod
    async def admin_block_user_1(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            client = data.get("client")
        await setter.admin_block_user(client.user_id)
        client = await getter.client_select(client.user_id)
        await state.update_data(client=client)
        await callback.message.edit_text("Пользователь Заблокирован!",
                                         reply_markup=AdminMarkup.admin_back_to_find_user())

    @staticmethod
    async def admin_unlock_user(callback: types.CallbackQuery):
        await callback.message.edit_text("Вы уверены что хотите разблокировать пользователя ?",
                                         reply_markup=AdminMarkup.admin_unlock_user())

    @staticmethod
    async def admin_unlock_user_1(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            client = data.get("client")
        await setter.admin_unlock_user(client.user_id)
        client = await getter.client_select(client.user_id)
        await state.update_data(client=client)
        await callback.message.edit_text("Пользователь Разблокирован!",
                                         reply_markup=AdminMarkup.admin_back_to_find_user())

    @staticmethod
    async def admin_appoint_admin(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            client = data.get("client")
        admins = await getter.admin_select_all()
        for i in admins:
            if i.user_id == client.user_id:
                await callback.message.edit_text("Этот пользователь уже является Админом",
                                                 reply_markup=AdminMarkup.admin_back_to_find_user())
                break
        else:
            await callback.message.edit_text("Вы уверены что хотите назначить данного пользователя Админом ?",
                                             reply_markup=AdminMarkup.admin_appoint_admin())

    @staticmethod
    async def admin_appoint_admin_1(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            client = data.get("client")
        await setter.admin_add(client.user_id, client.username)
        client = await getter.client_select(client.user_id)
        await state.update_data(client=client)
        await callback.message.edit_text(f"Пользователь @{client.username} назначен Администратором!",
                                         reply_markup=AdminMarkup.admin_back_to_find_user())

    @staticmethod
    async def admin_add_days(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            client = data.get("client")
        await callback.message.edit_text(f"<b>Подписка до</b> - <i>{client.subscribe.strftime('%d-%m-%Y')}</i>\n\n"
                                         f"<b>Сколько дней добавить к подписке ?</b>",
                                         reply_markup=AdminMarkup.admin_add_days())

    @staticmethod
    async def admin_add_days_1(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            client = data.get("client")
        days = callback.data[15:]
        await setter.admin_add_days(client.user_id, int(days))
        client = await getter.client_select(client.user_id)
        await state.update_data(client=client)
        await callback.message.edit_text(f"Добавлено дней - {days}",
                                         reply_markup=AdminMarkup.admin_back_to_find_user())

    @staticmethod
    async def admin_see_payments(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            client = data.get("client")
            payments_list = await getter.admin_select_all_payments(client.user_id)
        if payments_list:
            book = []
            while True:
                book.append(f"<b>ID платежа</b> - <i>{payments_list[0].id}</i>\n"
                            f"<b>Дата платежа</b> - <i>{payments_list[0].date_p.strftime('%d-%m-%Y')}</i>\n"
                            f"<b>Тип платежа</b> - <i>{payments_list[0].type_p}</i>\n"
                            f"<b>Сумма платежа</b> - <i>{payments_list[0].amount_p}</i>\n\n")
                payments_list.pop(0)
                if len(book) == 3 or payments_list == []:
                    break
            if not payments_list:
                await callback.message.edit_text("".join(book),
                                                 reply_markup=AdminMarkup.admin_back_user())
            else:
                await callback.message.edit_text("".join(book),
                                                 reply_markup=AdminMarkup.admin_list_payments())
                async with state.proxy() as data:
                    data["payments_list"] = payments_list
        else:
            await callback.message.edit_text("Платежей нет",
                                             reply_markup=AdminMarkup.admin_back_to_find_user())

    @staticmethod
    async def admin_see_payments_next(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            payments_list = data.get("payments_list")
        book = []
        while True:
            book.append(f"<b>ID платежа</b> - <i>{payments_list[0].id}</i>\n"
                        f"<b>Дата платежа</b> - <i>{payments_list[0].date_p.strftime('%d-%m-%Y')}</i>\n"
                        f"<b>Тип платежа</b> - <i>{payments_list[0].type_p}</i>\n"
                        f"<b>Сумма платежа</b> - <i>{payments_list[0].amount_p}</i>\n\n")
            payments_list.pop(0)
            if len(book) == 5 or payments_list == []:
                break
        if not payments_list:
            await callback.message.edit_text("".join(book),
                                             reply_markup=AdminMarkup.admin_list_payments_back())
        else:
            await callback.message.edit_text("".join(book),
                                             reply_markup=AdminMarkup.admin_list_payments())
            async with state.proxy() as data:
                data["payments_list"] = payments_list


class AdminAdvert:

    @staticmethod
    async def admin_advert(callback: types.CallbackQuery):
        await callback.message.edit_text("Введите объявление",
                                         reply_markup=AdminMarkup.admin_back_main_menu())
        await states.AdminAdvert.advert.set()

    @staticmethod
    async def admin_advert_1(message: types.Message, state: FSMContext):
        try:
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id-1)
        except:
            pass

        clients = await getter.all_active_clients()
        if not clients:
            await bot.send_message(
                chat_id=message.chat.id,
                text='Все пользователи в базе, заблокировали бота😤 никто не увидит сообщение',
                reply_markup=AdminMarkup.admin_back_main_menu()
            )

        await bot.send_message(
            chat_id=message.chat.id,
            text='Рассылка началась!\n Объявление:\n',
            reply_markup=AdminMarkup.admin_back_main_menu()
        )
        await bot.send_message(
            chat_id=message.chat.id,
            text=message.text,
            entities=message.entities,
            parse_mode=None
        )

        success, block = 0, 0
        for i in clients:
            try:
                await bot.send_message(i.user_id,
                                       f"{message.text}",
                                       entities=message.entities,
                                       parse_mode=None)
                success += 1
            except:
                block += 1
        await bot.send_message(message.from_user.id,
                               f"Ваше сообщение отправлено: - <b>{success}</b> клиентам\n"
                               f"<b>{block}</b> не получили сообщение",
                               reply_markup=AdminMarkup.admin_menu())
        await state.finish()


class AdminStats:
    @staticmethod
    async def admin_stats_menu(callback: types.CallbackQuery):
        await callback.message.edit_text("Какую статистику выгрузить ?",
                                         reply_markup=AdminMarkup.admin_stats_menu())

    @staticmethod
    async def admin_stats_clients(callback: types.CallbackQuery):
        all_clients = await getter.get_all_clients()
        with open("table_clients.csv", "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "user_id", "username", "access", "binds",
                             "limit_binds", "subscribe_type", "block"])
            for i in all_clients:
                writer.writerow([i.id, i.user_id, i.username, i.access, i.binds,
                                 i.limit_binds, i.subscribe_type, i.block])
        table_clients = InputFile("table_clients.csv")
        await bot.send_document(chat_id=callback.from_user.id,
                                document=table_clients)

    @staticmethod
    async def admin_stats_binds(callback: types.CallbackQuery):
        all_binds = await getter.get_all_binds()
        with open("table_binds.csv", "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "owner_id", "tg_channels_names", "tg_channels_ids", "tg_channels_urls",
                             "vk_groups_names", "vk_groups_ids", "vk_groups_urls", "qty", "tags", "opt_text",
                             "excl_tags", "url", "on"])
            for i in all_binds:
                writer.writerow([i.id, i.owner_id, i.tg_channels_names, i.tg_channels_ids, i.tg_channels_urls,
                                 i.vk_groups_names, i.vk_groups_ids, i.vk_groups_urls, i.qty, i.tags, i.opt_text,
                                 i.excl_tags, i.url, i.on])
        table_binds = InputFile("table_binds.csv")
        await bot.send_document(chat_id=callback.from_user.id,
                                document=table_binds)

    @staticmethod
    async def admin_stats_payments(callback: types.CallbackQuery):
        all_payments = await getter.all_payments()
        with open("table_payments.csv", "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "user_id", "date_p", "type_p", "amount_p"])
            for i in all_payments:
                writer.writerow([i.id, i.user_id, i.date_p, i.type_p, i.amount_p])
        table_payments = InputFile("table_payments.csv")
        await bot.send_document(chat_id=callback.from_user.id,
                                document=table_payments)


class AdminInviteLinks:
    @staticmethod
    async def admin_invite_links_stat(callback: types.CallbackQuery, state: FSMContext):
        links_list = await getter.get_invited_clients_sub_types()
        if links_list:

            book = []
            while True:
                link = links_list[0]['link']
                sub_types = links_list[0]['sub_types']

                text_block = f'{link.name} [{link.url}]\n'
                text_block += '\n'.join([f'<b>{j}</b>: {sub_types.count(j)}' for j in set(sub_types)])
                text_block += f'\n<b>Всего пользователей</b>: {len(sub_types)}'
                book.append(text_block)

                links_list.pop(0)
                if len(book) == 5 or links_list == []:
                    break

            if not links_list:
                await callback.message.edit_text("\n\n".join(book),
                                                 reply_markup=AdminMarkup.admin_back_main_menu())
            else:
                await callback.message.edit_text("\n\n".join(book),
                                                 reply_markup=AdminMarkup.admin_link_list())
                async with state.proxy() as data:
                    data["links_list"] = links_list

        else:
            await callback.message.edit_text(text='Пользователи не найдены',
                                             reply_markup=AdminMarkup.admin_back_main_menu())

    @staticmethod
    async def admin_invite_links_stat_next(callback: types.CallbackQuery, state: FSMContext):
        async with state.proxy() as data:
            links_list = data.get("links_list")

        book = []
        while True:
            link = links_list[0]['link']
            sub_types = links_list[0]['sub_types']

            text_block = f'{link.name} [{link.url}]\n'
            text_block += '\n'.join([f'<b>{j}</b>: {sub_types.count(j)}' for j in set(sub_types)])
            text_block += f'\n<b>Всего пользователей</b>: {len(sub_types)}'
            book.append(text_block)

            links_list.pop(0)
            if len(book) == 5 or links_list == []:
                break

        if not links_list:
            await callback.message.edit_text("\n\n".join(book),
                                             reply_markup=AdminMarkup.admin_link_list_back())
        else:
            await callback.message.edit_text("\n\n".join(book),
                                             reply_markup=AdminMarkup.admin_link_list())
            async with state.proxy() as data:
                data["links_list"] = links_list

    @staticmethod
    async def admin_invite_link(callback: types.CallbackQuery):
        text = 'Введите название пригласительной ссылки (до 250 символов)'
        await bot.edit_message_text(
            chat_id=callback.message.chat.id,
            message_id=callback.message.message_id,
            text=text,
            reply_markup=AdminMarkup.admin_back_main_menu())

        await states.AdminInviteLinks.name.set()

    @staticmethod
    async def admin_invite_link_message(message: types.Message, state: FSMContext):
        try:
            await bot.delete_message(message.from_user.id, message.message_id)
            await bot.delete_message(message.from_user.id, message.message_id-1)
        except:
            pass

        if len(message.text) > 250:
            await bot.send_message(
                chat_id=message.chat.id,
                text='Текст превышает лимит в 250 символов',
                reply_markup=AdminMarkup.admin_back_main_menu()
            )
            return

        link_id = await setter.create_invite_link(message.text)
        link = await get_start_link(f'{link_id}', encode=True)
        await setter.update_invite_link_url(link_id, link)

        text = (
            f'Пригласительная ссылка создана!\n'
            f'Название: {message.text}\n'
            f'Ссылка {link}'
        )
        await bot.send_message(
            chat_id=message.chat.id,
            text=text,
            reply_markup=AdminMarkup.admin_menu(),
            disable_web_page_preview=True, parse_mode=None)
        await state.finish()
