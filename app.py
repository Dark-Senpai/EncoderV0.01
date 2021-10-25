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


import subprocess 
import asyncio 
import os 
from telethon import events, Button 
from config import bot 
from tools import downloader, uploader, bash 

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

async def encodee(e):
  sec = e.pattern_match.group(1)
  if sec and sec.isdigit():
    stime = int(sec)
  vido = await e.get_reply_message()
  name = vido.file.name
  if not name:
    name = "video_" + dt.now().isoformat("_", "seconds") + ".mp4"
  
  c_time = time.time()
  file = await downloader(
    "resources/downloads/" + name,
    vfile,
    c_time,
    "Downloading " + name + "..."
  )
  d_time = time.time()
  diff = time_formatter((d_time - c_time) * 1000)
  file_name = (file.name).split("/")[-1]
  out = file_name.replace(file_name.split(".")[-1], "_[Animes_Encoded].mkv")
  xxx = await xxx.edit(
    f"Downloaded `{file.name}` of `{humanbytes(o_sizs)}` in `{diff}`.\n\nNow encoding ......"
  )
  ss, dd = duration_s(file.name, stime)
  cmd = f'ffmpeg -i "{file.name}" -preset veryfast -crf 32 -c:a libopus -ab 32k  -c:v libx265 -s 800x400  -map 0 "{out}" -y'
  await bash(cmd)
  os.remove(file.name)
  f_time = time.time()
  mmmm = await uploader(
    out,
    out,
    f_time,
    xxx,
    "Uploading " + out + "...",
  )
  data = await metadata(out)
  width = data["width"]
  height = data["height"]
  duration = data["duration"]
  attributes = [
    DocumentAttributeVideo(
      duration=duration, w=width, h=height, supports_streaming=True
    )
  ]
  caption = "@Animes_Encoded"
  await e.client.send_file(
    e.chat_id,
    mmmm,
    caption=caption,
    attributes=attributes,
    force_document=False,
    reply_to=e.reply_to_msg_id,
  )
