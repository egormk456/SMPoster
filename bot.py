from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from settings import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML, disable_web_page_preview=True)
dp = Dispatcher(bot, storage=MemoryStorage())
