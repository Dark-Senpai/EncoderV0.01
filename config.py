#      This file is part of the EncoderV0.01 distribution.
#    Copyright (c) 2021 Dark-Senpai
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/Dark-Senpai/EncoderV0.01/blob/main/License> .

from telethon import TelegramClient
import os
import logging
import time
from telethon import TelegramClient

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT_USERNAME = os.environ.get('BOT_USERNAME')

#APP_ID = config("APP_ID", default=None, cast=int)
#API_HASH = config("API_HASH", default=None)
#BOT_TOKEN = config("BOT_TOKEN", default=None)
#BOT_USERNAME = config("BOT_USERNAME", default=None)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
API_ID = 3281305
API_HASH = "a9e62ec83fe3c22379e3e19195c8b3f6" 
BOT_TOKEN = "2011046095:AAEBBAkwF9UVvxgPqPWh5bdlWaJEU_OhnFk" 
BOT_USERNAME = "telethonBot_bot"
