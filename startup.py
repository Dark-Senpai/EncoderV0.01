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

from .app import *
from .config import *

LOGS.info("Starting...")

#________ CMD __________#

@bot.on(events.NewMessage(pattern="/start"))
async def _(e):
  await start(e)
    
@bot.on(events.NewMessage(pattern="/ls"))
async def _(e):
  await list_files(e)
 
 
@cbot.on(events.NewMessage(pattern="/request_new_job"))
async def _(e):
  await encode(e)
 
#________ Run The Bot __________#

LOGS.info("Bot has started.")
cbot.run_until_disconnected()
