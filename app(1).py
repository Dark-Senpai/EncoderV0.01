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
from telethon import events, Button 
from config import bot 
from datetime import datetime as dt
from FastTelethon import download_file, upload_file 
from manage import * 


#_______________ Startup _________________#

async def start(event):
  xx = """
  Hi ! I am one powerful video encoder/compressor.\nI can compress your files in very less size with a slight quality change !\nJust send me video file or a document and wait for it to he **compressed**\n\nPowered By - @Animes_Encoded . 
  """
  # dont kang 
  ihelp = """
  Just send a video file or video document.\nYou should consider sending files or videos with extension .mp4 , .mkv and .webm\n\n**+This bot uses a poweful ffmpeg code that encodes animes/news of 25 minutes in 40 to 50mb\n+U will get a good, satisfactory quality in the encoded file\n-The bot repo is private and u cant acess it or deploy the bot for private use\n-The ffmpeg code cant be revealed as it is used by our encoderz team.**\n\nBy - @Animes_Encoded. 
  """
  # dont kang 
  iabout = """
  **Dev** - [Dark](https://t.me/Bro_isDarkal)
  **Repo** - [Source Code](https://t.me/shity_man)
  **Python** - [Python 3](https://python.org)
  **Library** - [Telethon](https://docs.telethon.dev)
  **Powered By** - [Press Me](https://t.me/Animes_Encoded)
  """
  # dont change , must give us credits 
  await event.reply(
    xx,
    buttons=[
      [
        Button.inline("HELP", data="ihelp"),
        Button.inline("ABOUT", data="iabout"),
      ],
    ],
  )

#_______________ ls _______________________#

#async def list_files(event):
 # p = subprocess.Popen(f'ls -lh downloads', stdout=subprocess.PIPE, shell=True)
  #x = await event.reply(p.communicate()[0].decode("utf-8", "replace").strip())
 # await asyncio.sleep(15)
 ##await x.delete()
#________________ Encode __________________#
async def encoding(event):
  if event.is_private 
  return await event.reply("Bruh! u cant use me here ! I am made for groups only \n\nBy @Animes_Encoded")
  if not event.media:
    return await event.reply("I cant work on this format\nPlease check the available [format](https://t.me/omg_wtf_lol) ")
  if hasattr(event.media, "document"):
    if not event.media.document.mime_type.startswith("video", "application/octet-stream")
    ):
      return await event.reply("I cant work on this format\nPlease Check the available [format](https://t.me/omg_wtf)")
      else:
        return 
  show_dl = await event.reply("📥 Downloading ....")
  dt_kid = dt.now()
  tame = time.now()
  dir = f"downloads/"
  try:
    if hasattr(event.media, "document"):
      file = event.media.document
      filename = event.file.name
      if not filename:
        filename = "video_" + dt.now().isoformat("_", "seconds") + ".mp4"
      dl = dir + filename 
      with open(dl, "wb") as wtf:
        dl = await download_file(
          client=event.client,
          location=file,
          out=wtf,
          progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(
              d,
              t,
              dl,
              tame,
              "Downlaoding",
              )
            ),
        )
      else:
        dl = await event.client.download_media(
          event.media,
          dir,
          progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, dl, tame, "Downloading")
            ),
          )
  except Exception as er:
    LOGS.info(er)
    return os.remove(dl)
  e = show_dl 
  es = dt.now()
  kk = dl.split("/")[-1]
  aa = kk.split(".")[-1]
  thum = "thumb.jpg"
  rr = f"encode"
  bb = kk.replace(f".{aa}", " (480p).mkv")
  end_dl = f"{rr}/{bb}"
  show_me = await e.edit("⏰ Compressing the video file .....")
  cmd = f'ffmpeg -i "{dl}" -c:v libx265 -s 854x480 -pix_fmt yuv420p  -preset veryfast -map 0 -crf 32 -c:a libopus -ab 32k "{end_dl}" -y'
  
  process = await asyncio.create_subprocess_shell(
    cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE 
    )
  stdout, stderr = await process.communicate()
  er = stderr.decode()
  if er:
    await e.edit(str(er))
    os.remove(dl)
    return os.remove(end_dl)
  
  #except BaseException:
   #   pass
# wtf? i will get a error here ??
  ees = dt.now()
  ttt = time.time()
  await show_me.delete()
  show_me_ul = await e.client.send_message(e.chat_id, "📤 Uploading...")
  with open(end_dl, "rb") as wtf:
    final_file = await upload_file(
      client=e.client,
      file=wtf,
      name=end_dl,
      progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
        progress(d, t, show_me_ul, ttt,
        "uploading..")
        ),
    )
  ds = await e.client.send_file(
    e.chat_id, file=final_file, force_document=True, thumb=thum
  )
  await show_me_ul.delete()
  # i messed up with this logic !
  os.remove(dl)
  os.remove(end_dl)
