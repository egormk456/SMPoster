import os
from dotenv import load_dotenv
from emoji import emojize
from urllib.parse import quote

load_dotenv()

VERSION = '1.0'
AUTHOR = 'Vasiliy Turtugeshev'

HOST = os.getenv('HOST')
POSTGRESQL_USER = os.getenv('POSTGRESQL_USER')
POSTGRESQL_PASSWORD = os.getenv('POSTGRESQL_PASSWORD')
DATABASE = os.getenv('DATABASE')

POSTGRES_URI = f"postgresql://{POSTGRESQL_USER}:" \
                    f"%s@{HOST}/{DATABASE}" % quote(f"{POSTGRESQL_PASSWORD}")

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = str(os.getenv('ADMIN_ID')).split(',')
PAY_TOKEN = os.getenv('PAY_TOKEN')

KEYBOARD = {
    "FAST_FORWARD_BUTTON": emojize(':fast-forward_button:'),
    "FAST_REVERSE_BUTTON": emojize(':fast_reverse_button:'),
    'INFORMATION': emojize(':information:'),
    'RIGHT_ARROW_CURVING_LEFT': emojize(':right_arrow_curving_left:'),
    'CROSS_MARK': emojize(':cross_mark:'),
    'CHECK_MARK_BUTTON': emojize(':check_mark_button:'),
    'STOPWATCH': emojize(':stopwatch:'),
    'RECYCLING_SYMBOL': emojize(':recycling_symbol:'),
    'SOS_BUTTON': emojize(':SOS_button:'),
    'UPWARDS_BUTTON': emojize(':upwards_button:'),
    'DOLLAR': emojize(':dollar_banknote:'),
    'DIAMOND_WITH_A_DOT': emojize(':diamond_with_a_dot:'),
    'LINKED_PAPERCLIPS': emojize(':linked_paperclips:'),
    'WARNING': emojize(':warning:'),
}
