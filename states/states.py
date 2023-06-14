from aiogram.dispatcher.filters.state import State, StatesGroup


class ClientAddBind(StatesGroup):
    add_bind: State = State()
    add_bind_name_vk_group: State = State()
    new_vk_token: State = State()
    add_vk_channel: State = State()
    add_new_vk_group: State = State()


class ClientAddChannels(StatesGroup):
    new_tg_channel: State = State()
    new_vk_group_name: State = State()
    new_vk_group: State = State()


class ClientOptions(StatesGroup):
    qty: State = State()
    tags: State = State()
    opt_text: State = State()
    excl_tags: State = State()


class AdminLimits(StatesGroup):
    standard_pay: State = State()
    add_pay: State = State()
    bind_limit: State = State()


class AdminFind(StatesGroup):
    find_id: State = State()
    find_username: State = State()
    change_month_payment: State = State()


class AdminAdvert(StatesGroup):
    advert: State = State()
