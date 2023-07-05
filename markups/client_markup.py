from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from settings.config import KEYBOARD


class ClientMarkup:
    @staticmethod
    def client_start():
        approve_ = InlineKeyboardMarkup()
        get = InlineKeyboardButton(text='Начать настройку',
                                   callback_data='client_start')
        approve_.insert(get)
        return approve_

    @staticmethod
    def client_main():
        approve_ = InlineKeyboardMarkup(row_width=2)
        get = InlineKeyboardButton(text=f'{KEYBOARD.get("RECYCLING_SYMBOL")} '
                                        f'Мои каналы',
                                   callback_data='client_list_binds')
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("UPWARDS_BUTTON")} '
                                         f'Добавить связь',
                                    callback_data='client_add_binds')
        get2 = InlineKeyboardButton(text=f'{KEYBOARD.get("DOLLAR")} '
                                         'Подписка',
                                    callback_data='client_subscribe')
        get3 = InlineKeyboardButton(text=f'{KEYBOARD.get("SOS_BUTTON")} '
                                         f'Поддержка',
                                    callback_data='client_need_support')
        approve_.insert(get)
        approve_.insert(get1)
        approve_.insert(get2)
        approve_.insert(get3)
        return approve_

    @staticmethod
    def client_subscribe_start():
        approve_ = InlineKeyboardMarkup(row_width=2)
        get1 = InlineKeyboardButton(text=f'Промо подписка',
                                    callback_data='client_subscribe_promo')
        get2 = InlineKeyboardButton(text=f'Платная подписка',
                                    callback_data='client_subscribe_paid')
        get4 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Вернуться в главное меню',
                                    callback_data='client_main_menu')
        approve_.insert(get1)
        approve_.insert(get2)
        approve_.row(get4)
        return approve_

    @staticmethod
    def client_subscribe_promo():
        approve_ = InlineKeyboardMarkup(row_width=2)
        get1 = InlineKeyboardButton(text=f'Банковская карта',
                                    callback_data='client_subscribe_promo_yookassa')
        get4 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Вернуться в главное меню',
                                    callback_data='client_main_menu')
        approve_.insert(get1)
        approve_.row(get4)
        return approve_

    @staticmethod
    def client_bind_start_preferences():
        approve_ = InlineKeyboardMarkup(row_width=2)
        get = InlineKeyboardButton(text=f'Перейти к настройкам',
                                   callback_data='client_bind_start_preferences')
        get1 = InlineKeyboardButton(text=f'Настроить позже',
                                    callback_data='client_main_menu')
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def client_promo(money):
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text=f'Заплатить {money} рублей',
                                   callback_data=f'client_first_paid_{money}')
        get4 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Назад',
                                    callback_data='client_subscribe')
        approve_.insert(get)
        approve_.row(get4)
        return approve_

    @staticmethod
    def client_paid(money):
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text=f'Заплатить {money} рублей',
                                   callback_data=f'client_paid_{money}')
        get4 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Назад',
                                    callback_data='client_subscribe')
        approve_.insert(get)
        approve_.row(get4)
        return approve_

    @staticmethod
    def client_paid_additional_binds(money, amount_binds):
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text=f'Заплатить {money} рублей',
                                   callback_data=f'{amount_binds}_additional_binds_{money}')
        get4 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Назад',
                                    callback_data='client_subscribe')
        approve_.insert(get)
        approve_.row(get4)
        return approve_

    @staticmethod
    def client_subscribe():
        approve_ = InlineKeyboardMarkup(row_width=2)
        get2 = InlineKeyboardButton(text=f'Добавить кол-во связей',
                                    callback_data='client_add_limit_binds')
        get1 = InlineKeyboardButton(text="Оплатить +1 месяц",
                                    callback_data='client_subscribe_yookassa')
        get4 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Вернуться в главное меню',
                                    callback_data='client_main_menu')
        approve_.insert(get2)
        approve_.insert(get1)
        approve_.row(get4)
        return approve_

    @staticmethod
    def client_end_subscribe():
        approve_ = InlineKeyboardMarkup(row_width=2)
        get1 = InlineKeyboardButton(text=f'Банковская карта',
                                    callback_data='client_subscribe_yookassa')
        get4 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Вернуться в главное меню',
                                    callback_data='client_main_menu')
        approve_.insert(get1)
        approve_.row(get4)
        return approve_

    @staticmethod
    def client_add_limit_binds():
        approve_ = InlineKeyboardMarkup(row_width=2)
        get1 = InlineKeyboardButton(text=f'2',
                                    callback_data='client_add_limit_binds_2')
        get2 = InlineKeyboardButton(text=f'3',
                                    callback_data='client_add_limit_binds_3')
        get3 = InlineKeyboardButton(text=f'4',
                                    callback_data='client_add_limit_binds_4')
        get4 = InlineKeyboardButton(text=f'5',
                                    callback_data='client_add_limit_binds_5')
        get5 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Назад',
                                    callback_data='client_subscribe')
        approve_.insert(get1)
        approve_.insert(get2)
        approve_.insert(get3)
        approve_.insert(get4)
        approve_.row(get5)
        return approve_

    @staticmethod
    def client_delete_limit_binds():
        approve_ = InlineKeyboardMarkup(row_width=3)
        get = InlineKeyboardButton(text=f'1',
                                   callback_data='client_delete_limit_binds_1')
        get1 = InlineKeyboardButton(text=f'2',
                                    callback_data='client_delete_limit_binds_2')
        get5 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Назад',
                                    callback_data='client_subscribe')
        approve_.insert(get)
        approve_.insert(get1)
        approve_.row(get5)
        return approve_

    @staticmethod
    def client_back_main_menu():
        approve_ = InlineKeyboardMarkup(row_width=2)
        get = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                        f'Вернуться в главное меню',
                                   callback_data='client_main_menu')
        approve_.insert(get)
        return approve_

    @staticmethod
    def client_back_main_menu_with_caption():
        approve_ = InlineKeyboardMarkup(row_width=2)
        get = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                        f'Вернуться в главное меню',
                                   callback_data='client_main_menu_with_caption')
        approve_.insert(get)
        return approve_

    @staticmethod
    def client_no_channels():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text=f'{KEYBOARD.get("UPWARDS_BUTTON")} '
                                        f'Добавить канал',
                                   callback_data='client_add_channel')
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Вернуться в главное меню',
                                    callback_data='client_main_menu')
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def client_approve():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text='Все верно!',
                                   callback_data='client_add_bind_final')
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Вернуться в главное меню',
                                    callback_data='client_main_menu')
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def client_list_binds(ids: list):
        approve_ = InlineKeyboardMarkup(row_width=3)
        v = 1
        for i in ids:
            get = InlineKeyboardButton(text=f'{v}',
                                       callback_data=f'client_enter_bind_{i}')
            approve_.insert(get)
            v += 1
        get2 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Вернуться в главное меню',
                                    callback_data='client_main_menu')
        approve_.row(get2)
        return approve_

    @staticmethod
    def client_enter_to_bind(on):
        approve_ = InlineKeyboardMarkup(row_width=2)
        tg = InlineKeyboardButton(text='Добавить ТГ канал',
                                  callback_data='client_add_one_more_tg_channel')
        tg0 = InlineKeyboardButton(text='Удалить ТГ канал',
                                   callback_data='client_delete_one_more_tg_channel')
        vk = InlineKeyboardButton(text='Добавить группу ВК',
                                  callback_data='client_add_one_more_vk_group')
        vk0 = InlineKeyboardButton(text='Удалить группу ВК',
                                   callback_data='client_delete_one_more_vk_group')
        opt = InlineKeyboardButton(text=f'{KEYBOARD.get("DIAMOND_WITH_A_DOT")} '
                                        f'Изменить опции',
                                   callback_data='client_change_options')
        get4 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Назад',
                                    callback_data='client_list_binds')
        approve_.insert(tg)
        approve_.insert(tg0)
        approve_.insert(vk)
        approve_.insert(vk0)
        approve_.insert(opt)
        if on:
            off = InlineKeyboardButton(text=f"{KEYBOARD.get('CROSS_MARK')} "
                                            "Отключить",
                                       callback_data=f"client_off_change")
            approve_.insert(off)
        else:
            on = InlineKeyboardButton(text=f"{KEYBOARD.get('CHECK_MARK_BUTTON')} "
                                           f"Включить",
                                      callback_data=f"client_on_change")
            approve_.insert(on)
        approve_.row(get4)
        return approve_

    @staticmethod
    def client_change_optionals(bind_id):
        approve_ = InlineKeyboardMarkup(row_width=2)
        get0 = InlineKeyboardButton(text='Изменить огр. символов',
                                    callback_data='client_qty_change')
        get1 = InlineKeyboardButton(text='Изменить хэштэги',
                                    callback_data='client_tags_change')
        get2 = InlineKeyboardButton(text='Изменить доп. текст',
                                    callback_data='client_opt_text_change')
        get3 = InlineKeyboardButton(text='Изменить искл. тэги',
                                    callback_data='client_excl_tags_change')
        url = InlineKeyboardButton(text="URL-ссылка на пост",
                                   callback_data=f"client_url_change")
        del_bind = InlineKeyboardButton(text="Удалить данную связь",
                                        callback_data=f"delete_this_bind")
        back = InlineKeyboardButton(text=f"{KEYBOARD.get('RIGHT_ARROW_CURVING_LEFT')} "
                                         f"Назад",
                                    callback_data=f"client_enter_bind_{bind_id}")
        approve_.insert(get0)
        approve_.insert(get1)
        approve_.insert(get2)
        approve_.insert(get3)
        approve_.insert(url)
        approve_.insert(del_bind)
        approve_.row(back)
        return approve_

    @staticmethod
    def client_back_to_bind(bind_id):
        approve_ = InlineKeyboardMarkup(row_width=1)
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Назад',
                                    callback_data=f'client_enter_bind_{bind_id}')
        approve_.insert(get1)
        return approve_

    @staticmethod
    def client_back_to_bind_options():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Назад',
                                    callback_data=f'client_change_options')
        approve_.insert(get1)
        return approve_

    @staticmethod
    def client_approve_new_vk_group_name(bind_id):
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text="Следующий этап",
                                   callback_data="client_approve_new_vk_group_name")
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Назад',
                                    callback_data=f'client_enter_bind_{bind_id}')
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def client_approve_new_tg_channel(bind_id):
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text="Добавить ТГ канал",
                                   callback_data="client_add_one_more_tg_channel_approve")
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Назад',
                                    callback_data=f'client_enter_bind_{bind_id}')
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def client_delete_tg_channel(tg_channels_ids, bind_id):
        approve_ = InlineKeyboardMarkup(row_width=1)
        for tg_channel_id in tg_channels_ids:
            get = InlineKeyboardButton(text=f'{tg_channel_id}',
                                       callback_data=f'client_delete_tg_channel_{tg_channel_id}')
            approve_.insert(get)
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Назад',
                                    callback_data=f'client_enter_bind_{bind_id}')
        approve_.row(get1)
        return approve_

    @staticmethod
    def client_delete_tg_channel_approve():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text='Удалить',
                                   callback_data=f'client_approve_delete_tg_channel')
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Назад',
                                    callback_data=f'client_delete_one_more_tg_channel')
        approve_.row(get)
        approve_.row(get1)
        return approve_

    @staticmethod
    def client_change_qty(qty):
        approve_ = InlineKeyboardMarkup(row_width=1)
        if qty:
            get = InlineKeyboardButton(text='Удалить огр. символов',
                                       callback_data=f'client_delete_qty')
            approve_.insert(get)
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Назад',
                                    callback_data=f'client_change_options')
        approve_.insert(get1)
        return approve_

    @staticmethod
    def client_change_tags(tags):
        approve_ = InlineKeyboardMarkup(row_width=1)
        if tags:
            get = InlineKeyboardButton(text='Удалить хэштэги',
                                       callback_data=f'client_delete_tags')
            approve_.insert(get)
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Назад',
                                    callback_data=f'client_change_options')
        approve_.insert(get1)
        return approve_

    @staticmethod
    def client_change_opt_text(opt_text):
        approve_ = InlineKeyboardMarkup(row_width=1)
        if opt_text:
            get = InlineKeyboardButton(text='Удалить доп. текст',
                                       callback_data=f'client_delete_opt_text')
            approve_.insert(get)
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Назад',
                                    callback_data=f'client_change_options')
        approve_.insert(get1)
        return approve_

    @staticmethod
    def client_change_excl_tags(excl_tags):
        approve_ = InlineKeyboardMarkup(row_width=1)
        if excl_tags:
            get = InlineKeyboardButton(text='Удалить искл. хэштэги',
                                       callback_data=f'client_delete_excl_tags')
            approve_.insert(get)
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Назад',
                                    callback_data=f'client_change_options')
        approve_.insert(get1)
        return approve_

    @staticmethod
    def client_add_new_group(bind_id):
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text="Всё верно!",
                                   callback_data=f"client_set_new_vk_group")
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Назад',
                                    callback_data=f'client_enter_bind_{bind_id}')
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def client_delete_group(vk_groups_ids, bind_id):
        approve_ = InlineKeyboardMarkup(row_width=1)
        for group_id in vk_groups_ids:
            get = InlineKeyboardButton(text=f'{group_id}',
                                       callback_data=f'client_delete_group_id_{group_id}')
            approve_.insert(get)
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Назад',
                                    callback_data=f'client_enter_bind_{bind_id}')
        approve_.row(get1)
        return approve_

    @staticmethod
    def client_delete_group_approve():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text='Удалить',
                                   callback_data=f'client_approve_delete_group_id')
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Назад',
                                    callback_data=f'client_delete_one_more_vk_group')
        approve_.row(get)
        approve_.row(get1)
        return approve_

    @staticmethod
    def client_delete_bind_approve(bind_id):
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text='Удалить',
                                   callback_data=f'client_approve_delete_bind_{bind_id}')
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Назад',
                                    callback_data=f'client_change_options')
        approve_.row(get)
        approve_.row(get1)
        return approve_

    @staticmethod
    def client_add_new_tags():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text="Всё верно!",
                                   callback_data=f"client_set_new_tags")
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Назад',
                                    callback_data=f'client_change_options')
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def client_add_new_opt_text():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text="Всё верно!",
                                   callback_data=f"client_set_new_opt_text")
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Назад',
                                    callback_data=f'client_change_options')
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def client_add_new_excl_tags():
        approve_ = InlineKeyboardMarkup(row_width=1)
        get = InlineKeyboardButton(text="Всё верно!",
                                   callback_data=f"client_set_new_excl_tags")
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Назад',
                                    callback_data=f'client_change_options')
        approve_.insert(get)
        approve_.insert(get1)
        return approve_

    @staticmethod
    def client_add_url():
        approve_ = InlineKeyboardMarkup(row_width=2)
        get = InlineKeyboardButton(text="Добавить",
                                   callback_data=f"client_set_url")
        get0 = InlineKeyboardButton(text="Удалить",
                                    callback_data=f"client_delete_url")
        get1 = InlineKeyboardButton(text=f'{KEYBOARD.get("RIGHT_ARROW_CURVING_LEFT")} '
                                         f'Назад',
                                    callback_data=f'client_change_options')
        approve_.insert(get)
        approve_.insert(get0)
        approve_.insert(get1)
        return approve_
