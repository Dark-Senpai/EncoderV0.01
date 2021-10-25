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


#_______________ Import Vital items ________________#



import asyncio
import os
import re
import time
from telethon import events, Button 
from config import bot 
from datetime import datetime as dt

from pyUltroid.functions.tools import metadata
from telethon.errors.rpcerrorlist import MessageNotModifiedError
from telethon.tl.types import DocumentAttributeVideo

from . import (
    bash,
    downloader,
    eor,
    get_string,
    humanbytes,
    math,
    mediainfo,
    time_formatter,
    ultroid_cmd,
    uploader,
)

#_______________ Startup _________________#

async def start(event):
  xx = f"""
  Hi, {event.sender.first_name}, Its nice to meet ya!
  This is a **Video Encoder** Bot Which encodes your video files (animes/movies/series/news)
  in low size ( 480p ) with good quality.
  Encode videos in 480p resolution.
  This bot takes a bit time than other telegram video compressing bots due to encoding settings.
  (c) @Animes_Encoded 
  """
  await event.reply(
    xx,
    buttons=[
      [Button.url("Boss", url='t.me/Bro_isDarkal')]
      ]
    )
#_______________ ls _______________________#

async def list_files(event):
  p = subprocess.Popen(f'ls -lh downloads', stdout=subprocess.PIPE, shell=True)
  x = await event.reply(p.communicate()[0].decode("utf-8", "replace").strip())
  await asyncio.sleep(15)
  await x.delete()
#________________ Encode __________________#

async def encode(e):
