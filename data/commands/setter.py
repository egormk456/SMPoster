import logging

from data.models.admins import Admins
from data.models.clients import Clients
from data.models.binds import Binds
from data.models.posts_media_group import PostsMediaGroup
from data.models.limits import Limits
from data.models.payments import Payments

from datetime import datetime, timedelta
from data.commands import getter


logger = logging.getLogger("bot.data.commands.setter")


async def client_add(user_id, username):
    logger.info(f'{user_id} Клиент добавляется в БД')
    limits = await getter.get_limits()
    user = Clients(user_id=user_id, username=username, limit_binds=limits.bind_limit, access=False,
                   subscribe_type="start", subscribe=datetime.now())
    await user.create()


async def admin_add(user_id, username):
    logger.info(f'{user_id} Админ добавляется в БД')
    admin = Admins(user_id=user_id, username=username)
    await admin.create()


async def client_add_vk_token(user_id, vk_token):
    logger.info(f'{user_id} Клиент добавляет vk token')
    client = await Clients.query.where(Clients.user_id == user_id).gino.first()
    await client.update(vk_token=vk_token).apply()


async def client_subscribe_promo(user_id):
    logger.info(f'{user_id} Клиент оформляет Промо подписку')
    client = await Clients.query.where(Clients.user_id == user_id).gino.first()
    await client.update(subscribe=datetime.now() + timedelta(hours=168),
                        access=True, subscribe_type="promo").apply()


async def client_add_new_bind(user_id, tg_channel_name, tg_channel_id, tg_channel_url,
                              vk_group_name, vk_group_id, vk_group_url):
    logger.info(f'{user_id} Клиент добавляет связь TG канал и VK группу')
    new_binds = Binds(owner_id=user_id, tg_channels_names=[tg_channel_name], tg_channels_ids=[tg_channel_id],
                      tg_channels_urls=[tg_channel_url], vk_groups_names=[vk_group_name], vk_groups_ids=[vk_group_id],
                      vk_groups_urls=[vk_group_url])
    await new_binds.create()
    return new_binds


async def client_add_new_bind_in_client_table(user_id):
    client = await Clients.query.where(Clients.user_id == user_id).gino.first()
    await client.update(binds=client.binds + 1).apply()


async def client_on_bind(user_id, bind_id):
    logger.info(f'{user_id} Клиент включает связь {bind_id}')
    bind = await Binds.query.where(Binds.id == bind_id).gino.first()
    await bind.update(on=True).apply()


async def client_off_bind(user_id, bind_id):
    logger.info(f'{user_id} Клиент выключает связь {bind_id}')
    bind = await Binds.query.where(Binds.id == bind_id).gino.first()
    await bind.update(on=False).apply()


async def client_add_new_tg_channel(user_id, bind_id, tg_channel_name, tg_channel_id, tg_channel_url):
    logger.info(f'{user_id} Клиент добавляет TG канал в связь {bind_id}')
    bind = await Binds.query.where(Binds.id == bind_id).gino.first()
    tg_channels_names = bind.tg_channels_names
    tg_channels_ids = bind.tg_channels_ids
    tg_channels_urls = bind.tg_channels_urls
    tg_channels_names.append(tg_channel_name)
    tg_channels_ids.append(tg_channel_id)
    tg_channels_urls.append(tg_channel_url)
    await bind.update(tg_channels_names=tg_channels_names,
                      tg_channels_ids=tg_channels_ids,
                      tg_channels_urls=tg_channels_urls).apply()


async def client_delete_tg_channel(user_id, bind_id, tg_channel_id):
    logger.info(f'{user_id} Клиент удаляет TG канал из связи {bind_id}')
    bind = await Binds.query.where(Binds.id == bind_id).gino.first()
    #  Находим индекс
    index_tg_channel_id = bind.tg_channels_ids.index(tg_channel_id)
    #  Записываем в список данные
    list_tg_channel_ids = bind.tg_channels_ids
    list_tg_channel_names = bind.tg_channels_names
    list_tg_channel_urls = bind.tg_channels_urls
    #  Удаляем по индексу данные
    list_tg_channel_ids.pop(index_tg_channel_id)
    list_tg_channel_names.pop(index_tg_channel_id)
    list_tg_channel_urls.pop(index_tg_channel_id)
    await bind.update(tg_channels_names=list_tg_channel_names,
                      tg_channels_ids=list_tg_channel_ids,
                      tg_channels_urls=list_tg_channel_urls).apply()


async def client_add_vk_group(bind_id, vk_group_name, vk_group_id, vk_group_url):
    """Клиент добавляет ВК-группу в связь"""
    bind = await Binds.query.where(Binds.id == bind_id).gino.first()
    list_vk_groups_names = bind.vk_groups_names
    list_vk_groups_ids = bind.vk_groups_ids
    list_vk_groups_urls = bind.vk_groups_urls
    list_vk_groups_names.append(vk_group_name)
    list_vk_groups_ids.append(vk_group_id)
    list_vk_groups_urls.append(vk_group_url)
    await bind.update(vk_groups_names=list_vk_groups_names,
                      vk_groups_ids=list_vk_groups_ids,
                      vk_groups_urls=list_vk_groups_urls).apply()


async def client_delete_vk_group(bind_id, vk_group_id):
    """Клиент удаляет ВК-группу из связи"""
    bind = await Binds.query.where(Binds.id == bind_id).gino.first()
    #  Находим индекс
    index_vk_group_id = bind.vk_groups_ids.index(vk_group_id)
    #  Записываем в список данные
    list_vk_groups_ids = bind.vk_groups_ids
    list_vk_groups_names = bind.vk_groups_names
    list_vk_groups_urls = bind.vk_groups_urls
    #  Удаляем по индексу данные
    list_vk_groups_ids.pop(index_vk_group_id)
    list_vk_groups_names.pop(index_vk_group_id)
    list_vk_groups_urls.pop(index_vk_group_id)
    await bind.update(vk_groups_names=list_vk_groups_names,
                      vk_groups_ids=list_vk_groups_ids,
                      vk_groups_urls=list_vk_groups_urls).apply()


async def client_delete_bind(bind_id):
    bind = await Binds.query.where(Binds.id == bind_id).gino.first()
    await bind.delete()


async def client_change_qty(bind_id, amount):
    bind = await Binds.query.where(Binds.id == bind_id).gino.first()
    await bind.update(qty=amount).apply()


async def client_change_delete_qty(bind_id):
    bind = await Binds.query.where(Binds.id == bind_id).gino.first()
    await bind.update(qty=None).apply()


async def client_change_tags(bind_id, tags):
    bind = await Binds.query.where(Binds.id == bind_id).gino.first()
    await bind.update(tags=tags).apply()


async def client_change_delete_tags(bind_id):
    bind = await Binds.query.where(Binds.id == bind_id).gino.first()
    await bind.update(tags=None).apply()


async def client_change_opt_text(bind_id, opt_text):
    bind = await Binds.query.where(Binds.id == bind_id).gino.first()
    await bind.update(opt_text=opt_text).apply()


async def client_change_delete_opt_text(bind_id):
    bind = await Binds.query.where(Binds.id == bind_id).gino.first()
    await bind.update(opt_text=None).apply()


async def client_change_excl_tags(bind_id, excl_tags):
    bind = await Binds.query.where(Binds.id == bind_id).gino.first()
    await bind.update(excl_tags=excl_tags).apply()


async def client_change_delete_excl_tags(bind_id):
    bind = await Binds.query.where(Binds.id == bind_id).gino.first()
    await bind.update(excl_tags=None).apply()


async def client_change_add_url(bind_id):
    bind = await Binds.query.where(Binds.id == bind_id).gino.first()
    await bind.update(url=1).apply()


async def client_change_delete_url(bind_id):
    bind = await Binds.query.where(Binds.id == bind_id).gino.first()
    await bind.update(url=None).apply()


async def bot_new_media_group_id(user_id, tg_channel_name, tg_channel_id, media_group_id):
    media_group = PostsMediaGroup(owner_id=user_id, tg_channel_name=tg_channel_name, tg_channel_id=tg_channel_id,
                                  media_group_id=media_group_id)
    await media_group.create()


async def bot_set_media_group_id_new_count(media_group_id):
    media_group = await PostsMediaGroup.query.where(PostsMediaGroup.media_group_id == media_group_id).gino.first()
    await media_group.update(count_files=media_group.count_files + 1).apply()


async def bot_set_media_group_id_decrease_count(media_group_id):
    media_group = await PostsMediaGroup.query.where(PostsMediaGroup.media_group_id == media_group_id).gino.first()
    await media_group.update(count_files=media_group.count_files - 1).apply()


async def create_limits():
    """Создается БД лимитов с дефолтными значениями"""
    limits = await Limits.query.where(Limits.id == 1).gino.first()
    if limits:
        return
    else:
        limits = Limits(standard_pay=199, add_pay=50, bind_limit=5)
        await limits.create()


async def admin_set_new_standard_payment(limit):
    limits = await Limits.query.where(Limits.id == 1).gino.first()
    await limits.update(standard_pay=limit).apply()


async def admin_set_new_add_payment(limit):
    limits = await Limits.query.where(Limits.id == 1).gino.first()
    await limits.update(add_pay=limit).apply()


async def admin_set_new_bind_limit(limit):
    limits = await Limits.query.where(Limits.id == 1).gino.first()
    all_client = await Clients.query.gino.all()
    for client in all_client:
        await client.update(limit_binds=limit).apply()
    await limits.update(bind_limit=limit).apply()


async def admin_set_new_month_payment_for_user(user_id, payment):
    client = await Clients.query.where(Clients.user_id == user_id).gino.first()
    await client.update(payment=payment).apply()


async def admin_delete_user(user_id):
    client = await Clients.query.where(Clients.user_id == user_id).gino.first()
    all_binds = await getter.client_select_all_binds(client.user_id)
    for i in all_binds:
        await i.delete()
    await client.delete()


async def admin_block_user(user_id):
    client = await Clients.query.where(Clients.user_id == user_id).gino.first()
    await client.update(block=True,
                        access=False).apply()


async def admin_unlock_user(user_id):
    client = await Clients.query.where(Clients.user_id == user_id).gino.first()
    timed = client.subscribe - datetime.now()
    if str(timed)[:1] == "-":
        await client.update(block=False,
                            access=False).apply()
    else:
        await client.update(block=False,
                            access=True).apply()


async def client_delete_limit_binds(user_id, limit):
    client = await Clients.query.where(Clients.user_id == user_id).gino.first()
    payments = await Limits.query.where(Limits.id == 1).gino.first()
    result = payments.add_pay * limit
    await client.update(limit_binds=client.limit_binds - limit,
                        payment=client.payment - int(result)).apply()


async def client_first_paid(user_id, payment: int):
    client = await Clients.query.where(Clients.user_id == user_id).gino.first()
    client_payment = Payments(user_id=user_id, date_p=datetime.now(),
                              type_p="standard", amount_p=payment)
    await client_payment.create()
    timed = datetime.now() + timedelta(days=30)
    await client.update(subscribe_type="paid",
                        subscribe=timed,
                        access=True,
                        payment=payment).apply()


async def client_paid(user_id, amount):
    client = await Clients.query.where(Clients.user_id == user_id).gino.first()
    payment = Payments(user_id=user_id, date_p=datetime.now(),
                       type_p="standard", amount_p=amount)
    await payment.create()
    timed = client.subscribe + timedelta(days=30)
    await client.update(subscribe=timed,
                        access=True).apply()


async def client_paid_additional_binds(user_id, money, binds):
    client = await Clients.query.where(Clients.user_id == user_id).gino.first()
    limits = await Limits.query.where(Limits.id == 1).gino.first()
    payment = Payments(user_id=user_id, date_p=datetime.now(),
                       type_p="additional", amount_p=money)
    await payment.create()
    await client.update(limit_binds=client.limit_binds + binds,
                        payment=client.payment + (limits.add_pay * binds)).apply()


async def admin_add_days(user_id, days):
    client = await Clients.query.where(Clients.user_id == user_id).gino.first()
    subscribe = client.subscribe + timedelta(days=days)
    await client.update(subscribe=subscribe).apply()
