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

from telethon import events, Button
from config import *
from tools import(
  Timer,
  fast_download,
  fast_upload,
  bash
)
import subprocess
import asyncio
import os

#_______________ Startup _________________#
@bot.on(events.NewMessage(pattern="/start"))
async def _(event):
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
@bot.on(events.NewMessage(pattern="/ls"))
async def _(event):
  p = subprocess.Popen(f'ls -lh downloads', stdout=subprocess.PIPE, shell=True)
  x = await event.reply(p.communicate()[0].decode("utf-8", "replace").strip())
  await asyncio.sleep(15)
  await x.delete()
#________________ Encode __________________#
@bot.on(events.NewMessage(pattern="/compress"))
async def _(event):
  mesh = await event.get_reply_message()
  fuk = await event.reply("📥 Downloading 📥")
  file = await fast_download(bot, mesh, fuk, "./downloads/")
  file = file.split("/")[-1]
  print(file)
  await fuk.edit("⏰ Encoding In **Progress**")
  await bash(f'ffmpeg -i "{file}" -map 0 -c:v libx265 -crf 30 -c:a libopus -ab 40k  -s 854x480 -pix_fmt yuv420p -preset veryfast "[ENCODED] {file}"')
  final_file = await fast_upload(bot, f"./downloads/[ENCODED] {file}", fuk)
  os.remove(f"./downloads/{file}")
  os.remove(f"./downloads/[ENCODED] {file}")
  await event.reply(f"./downloads/[ENCODED] {file}", file=final_file, force_document=True)
  await asyncio.sleep(5)
             
#____________________ Run The Bot ________________#

bot.start()

bot.run_until_disconnected()
