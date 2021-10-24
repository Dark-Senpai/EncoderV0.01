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
from configure import vars 

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#___________________ Basics __________________# 
# ADD VALUE BELOW FOR API_ID , DONT USE " " or ' ' 
API_ID = 
# ADD VALUE BELOW FOR API_HASH , DONT REMOVE " " 
API_HASH = " " 
# ADD VALUE BELOW FOR BOT_TOKEN , DONT REMOVE " " 
BOT_TOKEN = " "
# ADD VALUE FOR BOT_USERNAME , DONT REMOVE " " 
BOT_USERNAME = " " 

#__________________ TelegramClient __________________#
bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
