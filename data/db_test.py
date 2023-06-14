import asyncio
from datetime import datetime, timedelta

from sqlalchemy import and_, or_

from bot import dp
from data.commands import getter
from settings import config
from data.db_gino import db
from data import db_gino


async def db_test():
    await db_gino.on_startup(dp)
    client = await getter.client_select(351490585)
    timed = client.subscribe - datetime.now()
    print(type(timed))
    print(timed.days)


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(db_test())
