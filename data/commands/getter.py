from sqlalchemy import asc

from data.models.admins import Admins
from data.models.clients import Clients
from data.models.binds import Binds
from data.models.posts_media_group import PostsMediaGroup
from data.models.limits import Limits
from data.models.payments import Payments


async def all_clients():
    clients = await Clients.query.gino.all()
    return clients


async def all_binds():
    binds = await Binds.query.gino.all()
    return binds


async def all_payments():
    payments = await Payments.query.gino.all()
    return payments


async def client_select(user_id):
    client = await Clients.query.where(Clients.user_id == user_id).gino.first()
    return client


async def admin_select(user_id):
    admin = await Admins.query.where(Admins.user_id == user_id).gino.first()
    return admin


async def admin_select_all():
    admins = await Admins.query.gino.all()
    return admins


async def client_select_bind(bind_id):
    bind = await Binds.query.where(Binds.id == bind_id).gino.first()
    return bind


async def client_select_all_binds(user_id):
    binds = await Binds.query.order_by(asc(Binds.id)).where(Binds.owner_id == user_id).gino.all()
    return binds


async def client_select_bind_with_tg_channel_id(tg_channel_id):
    binds = await all_binds()
    for bind in binds:
        for tg_id in bind.tg_channels_ids:
            if tg_id == tg_channel_id:
                return bind


async def client_bind(user_id):
    bind = await Binds.query.order_by(asc(Binds.id)).where(Binds.owner_id == user_id).gino.all()
    return bind


async def get_post_with_media_group(media_group_id):
    media_group = await PostsMediaGroup.query.where(PostsMediaGroup.media_group_id == media_group_id).gino.first()
    return media_group


async def get_limits():
    limits = await Limits.query.where(Limits.id == 1).gino.first()
    return limits


async def get_all_clients():
    clients = await Clients.query.order_by(asc(Clients.id)).gino.all()
    return clients


async def get_all_binds():
    binds = await Binds.query.order_by(asc(Binds.id)).gino.all()
    return binds


async def admin_select_username(username):
    client = await Clients.query.where(Clients.username == username).gino.first()
    return client


async def check_subscribe():
    check = await Clients.query.gino.all()
    return check


async def admin_select_all_payments(user_id):
    payments = await Payments.query.order_by(asc(Payments.id)).where(Payments.user_id == user_id).gino.all()
    return payments
