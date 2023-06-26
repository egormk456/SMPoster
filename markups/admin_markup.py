from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from settings.config import KEYBOARD


class AdminMarkup:
    @staticmethod
    def admin_menu():
        approve_ = InlineKeyboardMarkup(row_width=2)
        get = InlineKeyboardButton(text="Список пользователей",
                                   callback_data="admin_user_list")
        get1 = InlineKeyboardButton(text="Список связей",
                                    callback_data="admin_bind_list")
        get2 = InlineKeyboardButton(text="Найти пользователя",
                                    callback_data="admin_find_user")
        get3 = InlineKeyboardButton(text="Изменения лимитов",
                                    callback_data="admin_limits_changes")
        get4 = InlineKeyboardButton(text="Сделать объявление",
                                    callback_data="admin_advert")
        get5 = InlineKeyboardButton(text="Выгрузить Статистику",
                                    callback_data="admin_stats_menu")
        approve_.insert(get)
        approve_.insert(get1)
        approve_.insert(get2)
        approve_.insert(get3)
        approve_.insert(get4)
        approve_.insert(get5)
        return approve_

    @staticmethod
    def admin_back_main_menu():
        approve_ = InlineKeyboardMarkup(row_width=2)
        get = InlineKeyboardButton(text=f"{KEYBOARD.get('RIGHT_ARROW_CURVING_LEFT')} "
                                        f"Вернуться в главное меню",
                                   callback_data="admin_main")
        approve_.insert(get)
        return approve_

    @staticmethod
    def admin_back_limit_menu():
        approve_ = InlineKeyboardMarkup(row_width=2)
        get = InlineKeyboardButton(text=f"{KEYBOARD.get('RIGHT_ARROW_CURVING_LEFT')} "
                                        f"Назад",
                                   callback_data="admin_limits_changes")
        approve_.insert(get)
        return approve_

    @staticmethod
    def admin_change_limits():
        approve_ = InlineKeyboardMarkup(row_width=2)
        get = InlineKeyboardButton(text="Стандартный платёж",
                                   callback_data="admin_change_standard_payment")
        get1 = InlineKeyboardButton(text="Дополнительный платёж",
                                    callback_data="admin_change_add_payment")
        get2 = InlineKeyboardButton(text="Лимит связей",
                                    callback_data="admin_change_limit_payment")
        get3 = InlineKeyboardButton(text=f"{KEYBOARD.get('RIGHT_ARROW_CURVING_LEFT')} "
                                         f"Вернуться в главное меню",
                                    callback_data="admin_main")
        approve_.insert(get)
        approve_.insert(get1)
        approve_.insert(get2)
        approve_.insert(get3)
        return approve_

    @staticmethod
    def admin_user_list():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text=f"Следующая страница",
                                   callback_data="admin_user_list_next")
        get1 = InlineKeyboardButton(text=f"{KEYBOARD.get('RIGHT_ARROW_CURVING_LEFT')} "
                                         f"Вернуться в главное меню",
                                    callback_data="admin_main")
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def admin_bind_list():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text=f"Следующая страница",
                                   callback_data="admin_bind_list_next")
        get1 = InlineKeyboardButton(text=f"{KEYBOARD.get('RIGHT_ARROW_CURVING_LEFT')} "
                                         f"Вернуться в главное меню",
                                    callback_data="admin_main")
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def admin_user_list_back():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text=f"С начала",
                                   callback_data="admin_user_list")
        get1 = InlineKeyboardButton(text=f"{KEYBOARD.get('RIGHT_ARROW_CURVING_LEFT')} "
                                         f"Вернуться в главное меню",
                                    callback_data="admin_main")
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def admin_bind_list_back():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text=f"С начала",
                                   callback_data="admin_bind_list")
        get1 = InlineKeyboardButton(text=f"{KEYBOARD.get('RIGHT_ARROW_CURVING_LEFT')} "
                                         f"Вернуться в главное меню",
                                    callback_data="admin_main")
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def admin_find_user():
        approve_ = InlineKeyboardMarkup(row_width=2)
        get = InlineKeyboardButton(text=f"Поиск по User id",
                                   callback_data="admin_find_user_id")
        get1 = InlineKeyboardButton(text=f"Поиск по Username",
                                    callback_data="admin_find_user_username")
        get2 = InlineKeyboardButton(text=f"{KEYBOARD.get('RIGHT_ARROW_CURVING_LEFT')} "
                                         f"Вернуться в главное меню",
                                    callback_data="admin_main")
        approve_.insert(get)
        approve_.insert(get1)
        approve_.insert(get2)
        return approve_

    @staticmethod
    def admin_find_user_back():
        approve_ = InlineKeyboardMarkup(row_width=2)
        get2 = InlineKeyboardButton(text=f"{KEYBOARD.get('RIGHT_ARROW_CURVING_LEFT')} "
                                         f"Назад",
                                    callback_data="admin_find_user")
        approve_.insert(get2)
        return approve_

    @staticmethod
    def admin_enter_find_user(start, block, payment):
        approve_ = InlineKeyboardMarkup(row_width=2)
        if start:
            if block:
                get1 = InlineKeyboardButton(text=f"Разблокировать",
                                            callback_data="admin_find_user_unlock_user")
                approve_.insert(get1)
            if not block:
                get1 = InlineKeyboardButton(text=f"Заблокировать",
                                            callback_data="admin_find_user_block_user")
                approve_.insert(get1)
            get2 = InlineKeyboardButton(text=f"Назн. Админом",
                                        callback_data="admin_find_user_admin_appoint")
            get5 = InlineKeyboardButton(text=f"{KEYBOARD.get('RIGHT_ARROW_CURVING_LEFT')} "
                                             f"Вернуться в главное меню",
                                        callback_data="admin_main")
            approve_.insert(get2)
            approve_.insert(get5)
            return approve_
        else:
            get = InlineKeyboardButton(text=f"Просмотр связей",
                                       callback_data="admin_bind_list_user")
            if block:
                get1 = InlineKeyboardButton(text=f"Разблокировать",
                                            callback_data="admin_find_user_unlock_user")
                approve_.insert(get1)
            if not block:
                get1 = InlineKeyboardButton(text=f"Заблокировать",
                                            callback_data="admin_find_user_block_user")
                approve_.insert(get1)
            get2 = InlineKeyboardButton(text=f"Назн. Админом",
                                        callback_data="admin_find_user_admin_appoint")
            if payment:
                get3 = InlineKeyboardButton(text=f"Изменить ст. мес. подписки",
                                            callback_data="admin_find_user_change_month_payment")
                approve_.insert(get3)
                get4 = InlineKeyboardButton(text=f"Показать платежи",
                                            callback_data="admin_find_user_see_payments")
                approve_.insert(get4)
            get5 = InlineKeyboardButton(text=f"Добавить дни подписки",
                                        callback_data="admin_find_user_add_days")
            get6 = InlineKeyboardButton(text=f"{KEYBOARD.get('RIGHT_ARROW_CURVING_LEFT')} "
                                             f"Вернуться в главное меню",
                                        callback_data="admin_main")
            approve_.insert(get)
            approve_.insert(get2)
            approve_.insert(get5)
            approve_.insert(get6)
            return approve_

    @staticmethod
    def admin_back_user():
        approve_ = InlineKeyboardMarkup(row_width=2)
        get = InlineKeyboardButton(text=f"{KEYBOARD.get('RIGHT_ARROW_CURVING_LEFT')} "
                                        f"Вернуться в меню пользователя",
                                   callback_data="admin_back_user")
        approve_.insert(get)
        return approve_

    @staticmethod
    def admin_bind_list_user():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text=f"Следующая страница",
                                   callback_data="admin_bind_list_user_next")
        get1 = InlineKeyboardButton(text=f"{KEYBOARD.get('RIGHT_ARROW_CURVING_LEFT')} "
                                         f"Вернуться в меню пользователя",
                                    callback_data="admin_back_user")
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def admin_bind_list_user_back():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text=f"С начала",
                                   callback_data="admin_bind_list_user")
        get1 = InlineKeyboardButton(text=f"{KEYBOARD.get('RIGHT_ARROW_CURVING_LEFT')} "
                                         f"Вернуться в меню пользователя",
                                    callback_data="admin_back_user")
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def admin_list_payments():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text=f"Следующая страница",
                                   callback_data="admin_list_payments_next")
        get1 = InlineKeyboardButton(text=f"{KEYBOARD.get('RIGHT_ARROW_CURVING_LEFT')} "
                                         f"Вернуться в меню пользователя",
                                    callback_data="admin_back_user")
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def admin_list_payments_back():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text=f"С начала",
                                   callback_data="admin_find_user_see_payments")
        get1 = InlineKeyboardButton(text=f"{KEYBOARD.get('RIGHT_ARROW_CURVING_LEFT')} "
                                         f"Вернуться в меню пользователя",
                                    callback_data="admin_back_user")
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def admin_back_to_find_user():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get1 = InlineKeyboardButton(text=f"{KEYBOARD.get('RIGHT_ARROW_CURVING_LEFT')} "
                                         f"Вернуться в меню пользователя",
                                    callback_data="admin_back_user")
        approve_.insert(get1)
        return approve_

    @staticmethod
    def admin_delete_user():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text=f"Удалить",
                                   callback_data="admin_delete_user")
        get1 = InlineKeyboardButton(text=f"{KEYBOARD.get('RIGHT_ARROW_CURVING_LEFT')} "
                                         f"Вернуться в меню пользователя",
                                    callback_data="admin_back_user")
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def admin_block_user():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text=f"Заблокировать",
                                   callback_data="admin_block_user")
        get1 = InlineKeyboardButton(text=f"{KEYBOARD.get('RIGHT_ARROW_CURVING_LEFT')} "
                                         f"Вернуться в меню пользователя",
                                    callback_data="admin_back_user")
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def admin_unlock_user():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text=f"Разблокировать",
                                   callback_data="admin_unlock_user")
        get1 = InlineKeyboardButton(text=f"{KEYBOARD.get('RIGHT_ARROW_CURVING_LEFT')} "
                                         f"Вернуться в меню пользователя",
                                    callback_data="admin_back_user")
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def admin_appoint_admin():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text=f"Назначить Админом",
                                   callback_data="admin_appoint_admin")
        get1 = InlineKeyboardButton(text=f"{KEYBOARD.get('RIGHT_ARROW_CURVING_LEFT')} "
                                         f"Вернуться в меню пользователя",
                                    callback_data="admin_back_user")
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def admin_add_days():
        approve_ = InlineKeyboardMarkup(row_width=2)
        get = InlineKeyboardButton(text=f"Добавить 5 дней",
                                   callback_data="admin_add_days_5")
        get1 = InlineKeyboardButton(text=f"Добавить 10 дней",
                                    callback_data="admin_add_days_10")
        get2 = InlineKeyboardButton(text=f"Добавить 30 дней",
                                    callback_data="admin_add_days_30")
        get3 = InlineKeyboardButton(text=f"{KEYBOARD.get('RIGHT_ARROW_CURVING_LEFT')} "
                                         f"Вернуться в меню пользователя",
                                    callback_data="admin_back_user")
        approve_.insert(get)
        approve_.insert(get1)
        approve_.insert(get2)
        approve_.insert(get3)
        return approve_

    @staticmethod
    def admin_stats_menu():
        approve_ = InlineKeyboardMarkup(row_width=2)
        get = InlineKeyboardButton(text=f"Клиенты",
                                   callback_data="admin_stats_clients")
        get1 = InlineKeyboardButton(text=f"Связи",
                                    callback_data="admin_stats_binds")
        get2 = InlineKeyboardButton(text=f"Платежи",
                                    callback_data="admin_stats_payments")
        get3 = InlineKeyboardButton(text=f"{KEYBOARD.get('RIGHT_ARROW_CURVING_LEFT')} "
                                         f"Вернуться в главное меню",
                                    callback_data="admin_main")
        approve_.insert(get)
        approve_.insert(get1)
        approve_.insert(get2)
        approve_.insert(get3)
        return approve_
