__all__ = ["register_client_handler", "register_admin_handler"]

from aiogram import Dispatcher
from aiogram.types import ContentType

from .client import ClientMain, ClientBinds, ClientAddBinds, ClientSubscribe
from .admin import AdminMain, AdminLimits, AdminUserList, AdminBindList, AdminFindUser, AdminAdvert
from states import states


def register_client_handler(disp: Dispatcher):

    """Client Main"""

    disp.register_callback_query_handler(ClientMain.client_start,
                                         state=["*"],
                                         text="client_start")
    disp.register_callback_query_handler(ClientMain.client_main,
                                         state=["*"],
                                         text="client_main_menu")
    disp.register_callback_query_handler(ClientMain.client_main_menu_with_caption,
                                         state=["*"],
                                         text="client_main_menu_with_caption")
    disp.register_callback_query_handler(ClientMain.client_need_support,
                                         state=["*"],
                                         text="client_need_support")
    disp.register_message_handler(ClientMain.client_add_new_vk_token,
                                  state=states.ClientAddBind.new_vk_token,
                                  content_types=['text', 'audio', 'document', 'photo', 'video', 'animation'])

    """Client Subscribe"""

    disp.register_callback_query_handler(ClientSubscribe.subscribe_main,
                                         state=["*"],
                                         text="client_subscribe")
    disp.register_callback_query_handler(ClientSubscribe.client_subscribe_promo,
                                         state=["*"],
                                         text="client_subscribe_promo")
    disp.register_callback_query_handler(ClientSubscribe.client_subscribe_paid,
                                         state=["*"],
                                         text="client_subscribe_paid")
    disp.register_callback_query_handler(ClientSubscribe.qiwi_promo,
                                         state=["*"],
                                         text="client_subscribe_promo_qiwi")
    disp.register_callback_query_handler(ClientSubscribe.yookassa_promo,
                                         state=["*"],
                                         text="client_subscribe_promo_yookassa")
    disp.register_callback_query_handler(ClientSubscribe.client_first_paid,
                                         state=["*"],
                                         text_contains="client_first_paid_")
    disp.register_pre_checkout_query_handler(ClientSubscribe.checkout_handler)
    disp.register_message_handler(ClientSubscribe.client_first_paid_1,
                                  content_types=[ContentType.SUCCESSFUL_PAYMENT])
    disp.register_callback_query_handler(ClientSubscribe.qiwi_paid,
                                         state=["*"],
                                         text="client_subscribe_qiwi")
    disp.register_callback_query_handler(ClientSubscribe.yookassa_paid,
                                         state=["*"],
                                         text="client_subscribe_yookassa")
    disp.register_callback_query_handler(ClientSubscribe.client_paid,
                                         state=["*"],
                                         text_contains="client_paid_")
    disp.register_callback_query_handler(ClientSubscribe.client_add_limit_binds,
                                         state=["*"],
                                         text="client_add_limit_binds")
    disp.register_callback_query_handler(ClientSubscribe.client_add_limit_binds_1,
                                         state=["*"],
                                         text_contains="client_add_limit_binds_")
    disp.register_callback_query_handler(ClientSubscribe.client_add_limit_binds_2,
                                         state=["*"],
                                         text_contains="_additional_binds_")
    disp.register_callback_query_handler(ClientSubscribe.client_delete_limit_binds,
                                         state=["*"],
                                         text="client_delete_limit_binds")
    disp.register_callback_query_handler(ClientSubscribe.client_delete_limit_binds_1,
                                         state=["*"],
                                         text_contains="client_delete_limit_binds_")

    """Client Binds"""

    disp.register_callback_query_handler(ClientBinds.client_binds,
                                         state=["*"],
                                         text="client_list_binds")
    disp.register_callback_query_handler(ClientBinds.client_enter_bind,
                                         state=["*"],
                                         text_contains="client_enter_bind_")
    disp.register_callback_query_handler(ClientBinds.client_on_bind,
                                         state=["*"],
                                         text="client_on_change")
    disp.register_callback_query_handler(ClientBinds.client_off_bind,
                                         state=["*"],
                                         text="client_off_change")
    disp.register_callback_query_handler(ClientBinds.client_add_one_more_tg_channel,
                                         state=["*"],
                                         text="client_add_one_more_tg_channel")
    disp.register_message_handler(ClientBinds.client_add_one_more_tg_channel_1,
                                  state=states.ClientAddChannels.new_tg_channel,
                                  content_types=['text', 'audio', 'document', 'photo', 'video', 'animation'])
    disp.register_callback_query_handler(ClientBinds.client_add_one_more_tg_channel_2,
                                         state=["*"],
                                         text="client_add_one_more_tg_channel_approve")
    disp.register_callback_query_handler(ClientBinds.client_delete_tg_channel,
                                         state=["*"],
                                         text="client_delete_one_more_tg_channel")
    disp.register_callback_query_handler(ClientBinds.client_delete_tg_channel_1,
                                         state=["*"],
                                         text_contains="client_delete_tg_channel_")
    disp.register_callback_query_handler(ClientBinds.client_delete_tg_channel_2,
                                         state=["*"],
                                         text="client_approve_delete_tg_channel")
    disp.register_callback_query_handler(ClientBinds.client_add_one_more_vk_group,
                                         state=["*"],
                                         text="client_add_one_more_vk_group")
    disp.register_message_handler(ClientBinds.client_add_one_more_vk_group_1,
                                  state=states.ClientAddChannels.new_vk_group_name)
    disp.register_callback_query_handler(ClientBinds.client_add_one_more_vk_group_2,
                                         state=["*"],
                                         text="client_approve_new_vk_group_name")
    disp.register_message_handler(ClientBinds.client_add_one_more_vk_group_3,
                                  state=states.ClientAddChannels.new_vk_group)
    disp.register_callback_query_handler(ClientBinds.client_add_one_more_vk_group_4,
                                         state=["*"],
                                         text="client_set_new_vk_group")
    disp.register_callback_query_handler(ClientBinds.client_delete_vk_group,
                                         state=["*"],
                                         text="client_delete_one_more_vk_group")
    disp.register_callback_query_handler(ClientBinds.client_delete_vk_group_1,
                                         state=["*"],
                                         text_contains="client_delete_group_id_")
    disp.register_callback_query_handler(ClientBinds.client_delete_vk_group_2,
                                         state=["*"],
                                         text="client_approve_delete_group_id")
    disp.register_callback_query_handler(ClientBinds.client_delete_bind,
                                         state=["*"],
                                         text="delete_this_bind")
    disp.register_callback_query_handler(ClientBinds.client_approve_delete_bind,
                                         state=["*"],
                                         text_contains="client_approve_delete_bind_")
    disp.register_callback_query_handler(ClientBinds.client_options,
                                         state=["*"],
                                         text="client_change_options")
    disp.register_callback_query_handler(ClientBinds.client_change_qty,
                                         state=["*"],
                                         text="client_qty_change")
    disp.register_message_handler(ClientBinds.client_change_qty_1,
                                  state=states.ClientOptions.qty)
    disp.register_callback_query_handler(ClientBinds.client_delete_qty,
                                         state=["*"],
                                         text="client_delete_qty")
    disp.register_callback_query_handler(ClientBinds.client_change_tags,
                                         state=["*"],
                                         text="client_tags_change")
    disp.register_message_handler(ClientBinds.client_change_tags_1,
                                  state=states.ClientOptions.tags)
    disp.register_callback_query_handler(ClientBinds.client_change_tags_2,
                                         state=["*"],
                                         text="client_set_new_tags")
    disp.register_callback_query_handler(ClientBinds.client_delete_tags,
                                         state=["*"],
                                         text="client_delete_tags")
    disp.register_callback_query_handler(ClientBinds.client_change_opt_text,
                                         state=["*"],
                                         text="client_opt_text_change")
    disp.register_message_handler(ClientBinds.client_change_opt_text_1,
                                  state=states.ClientOptions.opt_text)
    disp.register_callback_query_handler(ClientBinds.client_change_opt_text_2,
                                         state=["*"],
                                         text="client_set_new_opt_text")
    disp.register_callback_query_handler(ClientBinds.client_delete_opt_text,
                                         state=["*"],
                                         text="client_delete_opt_text")
    disp.register_callback_query_handler(ClientBinds.client_change_excl_tags,
                                         state=["*"],
                                         text="client_excl_tags_change")
    disp.register_message_handler(ClientBinds.client_change_excl_tags_1,
                                  state=states.ClientOptions.excl_tags)
    disp.register_callback_query_handler(ClientBinds.client_change_excl_tags_2,
                                         state=["*"],
                                         text="client_set_new_excl_tags")
    disp.register_callback_query_handler(ClientBinds.client_delete_excl_tags,
                                         state=["*"],
                                         text="client_delete_excl_tags")
    disp.register_callback_query_handler(ClientBinds.client_url,
                                         state=["*"],
                                         text="client_url_change")
    disp.register_callback_query_handler(ClientBinds.client_url_add,
                                         state=["*"],
                                         text="client_set_url")
    disp.register_callback_query_handler(ClientBinds.client_url_delete,
                                         state=["*"],
                                         text="client_delete_url")

    """Client Add Binds"""

    disp.register_callback_query_handler(ClientAddBinds.client_add_bind_1,
                                         state=["*"],
                                         text="client_add_binds")
    disp.register_message_handler(ClientAddBinds.client_add_bind_2,
                                  state=states.ClientAddBind.add_bind,
                                  content_types=['text', 'audio', 'document', 'photo', 'video', 'animation'])
    disp.register_message_handler(ClientAddBinds.client_add_bind_3,
                                  state=states.ClientAddBind.add_vk_channel)
    disp.register_message_handler(ClientAddBinds.client_add_bind_4,
                                  state=states.ClientAddBind.add_bind_name_vk_group)
    disp.register_callback_query_handler(ClientAddBinds.client_add_bind_5,
                                         state=["*"],
                                         text="client_add_bind_final")
    disp.register_callback_query_handler(ClientAddBinds.client_add_bind_6,
                                         state=["*"],
                                         text="client_bind_start_preferences")


def register_admin_handler(disp: Dispatcher):

    """Admin Main"""

    disp.register_callback_query_handler(AdminMain.admin_main,
                                         state=["*"],
                                         text="admin_main")

    """Admin Limits"""

    disp.register_callback_query_handler(AdminLimits.admin_limits,
                                         state=["*"],
                                         text="admin_limits_changes")
    disp.register_callback_query_handler(AdminLimits.admin_change_standard,
                                         state=["*"],
                                         text="admin_change_standard_payment")
    disp.register_message_handler(AdminLimits.admin_change_standard_1,
                                  state=states.AdminLimits.standard_pay)
    disp.register_callback_query_handler(AdminLimits.admin_change_add,
                                         state=["*"],
                                         text="admin_change_add_payment")
    disp.register_message_handler(AdminLimits.admin_change_add_1,
                                  state=states.AdminLimits.add_pay)
    disp.register_callback_query_handler(AdminLimits.admin_change_bind_limit,
                                         state=["*"],
                                         text="admin_change_limit_payment")
    disp.register_message_handler(AdminLimits.admin_change_bind_limit_1,
                                  state=states.AdminLimits.bind_limit)

    """Admin User List"""

    disp.register_callback_query_handler(AdminUserList.admin_user_list,
                                         state=["*"],
                                         text="admin_user_list")
    disp.register_callback_query_handler(AdminUserList.admin_user_list_next,
                                         state=["*"],
                                         text="admin_user_list_next")

    """Admin Bind List"""

    disp.register_callback_query_handler(AdminBindList.admin_bind_list,
                                         state=["*"],
                                         text="admin_bind_list")
    disp.register_callback_query_handler(AdminBindList.admin_bind_list_next,
                                         state=["*"],
                                         text="admin_user_list_next")

    """Admin Advert"""

    disp.register_callback_query_handler(AdminAdvert.admin_advert,
                                         state=["*"],
                                         text="admin_advert")
    disp.register_message_handler(AdminAdvert.admin_advert_1,
                                  state=states.AdminAdvert.advert)

    """Admin Find User"""

    disp.register_callback_query_handler(AdminFindUser.admin_find_user,
                                         state=["*"],
                                         text="admin_find_user")
    disp.register_callback_query_handler(AdminFindUser.admin_find_id,
                                         state=["*"],
                                         text="admin_find_user_id")
    disp.register_message_handler(AdminFindUser.admin_find_id_1,
                                  state=states.AdminFind.find_id)
    disp.register_callback_query_handler(AdminFindUser.admin_find_username,
                                         state=["*"],
                                         text="admin_find_user_username")
    disp.register_message_handler(AdminFindUser.admin_find_username_1,
                                  state=states.AdminFind.find_username)
    disp.register_callback_query_handler(AdminFindUser.admin_bind_list_user,
                                         state=["*"],
                                         text="admin_bind_list_user")
    disp.register_callback_query_handler(AdminFindUser.admin_bind_list_user_next,
                                         state=["*"],
                                         text="admin_bind_list_user_next")
    disp.register_callback_query_handler(AdminFindUser.admin_back_user,
                                         state=["*"],
                                         text="admin_back_user")
    disp.register_callback_query_handler(AdminFindUser.admin_change_user_month_payment,
                                         state=["*"],
                                         text="admin_find_user_change_month_payment")
    disp.register_message_handler(AdminFindUser.admin_change_user_month_payment_1,
                                  state=states.AdminFind.change_month_payment)
    disp.register_callback_query_handler(AdminFindUser.admin_delete_user,
                                         state=["*"],
                                         text="admin_find_user_delete_user")
    disp.register_callback_query_handler(AdminFindUser.admin_delete_user_1,
                                         state=["*"],
                                         text="admin_delete_user")
    disp.register_callback_query_handler(AdminFindUser.admin_block_user,
                                         state=["*"],
                                         text="admin_find_user_block_user")
    disp.register_callback_query_handler(AdminFindUser.admin_block_user_1,
                                         state=["*"],
                                         text="admin_block_user")
    disp.register_callback_query_handler(AdminFindUser.admin_unlock_user,
                                         state=["*"],
                                         text="admin_find_user_unlock_user")
    disp.register_callback_query_handler(AdminFindUser.admin_unlock_user_1,
                                         state=["*"],
                                         text="admin_unlock_user")
    disp.register_callback_query_handler(AdminFindUser.admin_appoint_admin,
                                         state=["*"],
                                         text="admin_find_user_admin_appoint")
    disp.register_callback_query_handler(AdminFindUser.admin_appoint_admin_1,
                                         state=["*"],
                                         text="admin_appoint_admin")
    disp.register_callback_query_handler(AdminFindUser.admin_add_days,
                                         state=["*"],
                                         text="admin_find_user_add_days")
    disp.register_callback_query_handler(AdminFindUser.admin_add_days_1,
                                         state=["*"],
                                         text_contains="admin_add_days_")
    disp.register_callback_query_handler(AdminFindUser.admin_see_payments,
                                         state=["*"],
                                         text="admin_find_user_see_payments")
    disp.register_callback_query_handler(AdminFindUser.admin_see_payments_next,
                                         state=["*"],
                                         text="admin_list_payments_next")
