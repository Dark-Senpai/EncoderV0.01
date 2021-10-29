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
import math
import time
import subprocess 
from telethon import events, Button 
from config import bot 
from datetime import datetime as dt
from FastTelethonhelper import download_with_progressbar, upload_with_progressbar 

helpx = """
  Just send a video file or video document.\nYou should consider sending files or videos with extension .mp4 , .mkv and .webm\n\n**+This bot uses a poweful ffmpeg code that encodes animes/news of 25 minutes in 40 to 50mb\n+U will get a good, satisfactory quality in the encoded file\n-The bot repo is private and u cant acess it or deploy the bot for private use\n-The ffmpeg code cant be revealed as it is used by our encoderz team.**\n\nBy - @Animes_Encoded. 
  """
aboutx = """
  **Developer** - [Dev](https://t.me/Bro_isDarkal)
  **Repo** - [Source Code](https://t.me/shity_man)
  **Python** - [Python 3](https://python.org)
  **Library** - [Telethon](https://docs.telethon.dev)
  **Powered By** - [Press Me](https://t.me/Animes_Encoded)
  """
xx = """
  Hi ! I am one powerful video encoder/compressor.\nI can compress your files in very less size with a slight quality change !\nJust send me video file or a document and wait for it to he **compressed**\n\nPowered By - @Animes_Encoded . 
  """
#_______________ Startup _________________#

async def start(event):
  await event.reply(
    xx,
    buttons=[
      [
        Button.inline("HELP", data="ihelp"),
        Button.inline("ABOUT", data="iabout")],
      [Button.url("BOSS", url="https://t.me/Bro_isDarkal")],
    ],
  )
  
  
async def ihelp(event):
  await event.edit(
    helpx,
    buttons=[Button.inline("BACK", data="beck")],
    )

    
async def iabout(event):
  await event.edit(
    aboutx,
    link_preview=False,
    buttons=[Button.inline("BACK", data="beck")],
    )

      
async def beck(event):
  await event.edit(
    xx,
    buttons=[
      [
        Button.inline("HELP", data="ihelp"),
        Button.inline("ABOUT", data="iabout")],
      [Button.url("BOSS", url="https://t.me/Bro_isDarkal")],
    ]
  )

#_____________ bash ______________#

async def bash(cmd):
  process = await asyncio.create_subprocess_shell(
    cmd,
    stdout=asyncio.subprocess.PIPE,
    stderr=asyncio.subprocess.PIPE,
    )
  stdout, stderr = await process.communate()
  err = stderr.decode().strip()
  out = stdout.decode().strip()
  return out, err 
  
    
  
    

#_______________ ls _______________________#

#async def list_files(event):
 # p = subprocess.Popen(f'ls -lh downloads', stdout=subprocess.PIPE, shell=True)
  #x = await event.reply(p.communicate()[0].decode("utf-8", "replace").strip())
 # await asyncio.sleep(15)
 ##await x.delete()
#________________ Encode __________________#
async def encoding(event):
  try:
    get_msg = await event.get_reply_message()
    send_msg = await bot.send_message(event.chat_id, "Downloading..")
  dl = await download_with_progressbar(bot, get_msg, send_msg)
  kk = dl.split("/")[-1]
  aa = kk.split(",")[-1]
  out = kk.replace(f".{aa}", "[480p].mkv")
  
  # this will add [480p] thing at last of evry video file this bot encodes 😀
  await bash(f"ffmpeg -i "{dl}" -c:v libx265 -s 856x480 -preset veryfast -pix_fmt yuv420p -c:a libopus -ab 40k -crf 29.7 "{out}" -y")
  except BaseException as er:
    LOGS.info(er) 
    return os.remove(dl)
  # now lets add upload part , its important lol 🤪
  
  await upload_with_progress_bar(bot, send_msg, out)
  os.remove(dl)
  os.remove(out)
  
  # its done , 🤫 
  
  
