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

from tools import (
    bash,
    downloader,
    eor,
    humanbytes,
    mediainfo,
    time_formatter,
    uploader
)

#_______________ Startup _________________#

async def start(event):
  xx = f"""
  Hi, {event.sender.first_name}, Its nice to meet ya!\n This is a **Video Encoder** Bot Which encodes your video files (animes/movies/series/news)in low size ( 480p ) with good quality.\n Encode videos in 480p resolution.\nThis bot takes a bit time than other telegram video compressing bots due to encoding settings.\n\n(c) @Animes_Encoded 
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
    vido = await e.get_reply_message()
    if vido and vido.media and "video" in mediainfo(vido.media):
        if hasattr(vido.media, "document"):
            vfile = vido.media.document
            name = vido.file.name
        else:
            vfile = vido.media
            name = ""
        if not name:
            name = "video_" + dt.now().isoformat("_", "seconds") + ".mp4"
        xxx = await eor(e, get_string("audiotools_5"))
        c_time = time.time()
        file = await downloader(
            "resources/downloads/" + name,
            vfile,
            xxx,
            c_time,
            "Downloading " + name + "...",
        )
        o_size = os.path.getsize(file.name)
        d_time = time.time()
        diff = time_formatter((d_time - c_time) * 1000)
        file_name = (file.name).split("/")[-1]
        out = file_name.replace(file_name.split(".")[-1], "compressed.mkv")
        await xxx.edit(
            f"**Downloaded** `{file.name}` of `{humanbytes(o_size)}` in `{diff}`.\n\nNow Encoding ⏰..."
        )
        x, y = await bash(
            f'mediainfo --fullscan """{file.name}""" | grep "Frame count"'
        )
        total_frames = x.split(":")[1].split("\n")[0]
        progress = f"progress-{c_time}.txt"
        with open(progress, "w") as fk:
            pass
        proce = await asyncio.create_subprocess_shell(
            f'ffmpeg -hide_banner -loglevel quiet -progress {progress} -i """{file.name}""" -preset veryfast -map 0 -c:v libx265 -crf 32 -s 854x480 -pix_fmt yuv420p -c:a libopus -ab 32k """{out}""" -y',
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        while proce.returncode != 0:
            await asyncio.sleep(3)
            with open(progress, "r+") as fil:
                text = fil.read()
                frames = re.findall("frame=(\\d+)", text)
                size = re.findall("total_size=(\\d+)", text)
                speed = 0
                if len(frames):
                    elapse = int(frames[-1])
                if len(size):
                    size = int(size[-1])
                    per = elapse * 100 / int(total_frames)
                    time_diff = time.time() - int(d_time)
                    speed = round(elapse / time_diff, 2)
                if int(speed) != 0:
                    some_eta = ((int(total_frames) - elapse) / speed) * 1000
                    text = f"`Compressing {file_name} at {crf} CRF.\n`"
                    progress_str = "`[{0}{1}] {2}%\n\n`".format(
                        "".join("●" for i in range(math.floor(per / 5))),
                        "".join("" for i in range(20 - math.floor(per / 5))),
                        round(per, 2),
                    )

                    e_size = humanbytes(size) + " of ~" + humanbytes((size / per) * 100)
                    eta = "~" + time_formatter(some_eta)
                    try:
                        await xxx.edit(
                            text
                            + progress_str
                            + "`"
                            + e_size
                            + "`"
                            + "\n\n`"
                            + eta
                            + "`"
                        )
                    except MessageNotModifiedError:
                        pass
        os.remove(file.name)
        c_size = os.path.getsize(out)
        f_time = time.time()
        difff = time_formatter((f_time - d_time) * 1000)
        await xxx.edit(
            f"`Compressed {humanbytes(o_size)} to {humanbytes(c_size)} in {difff}\nTrying to Upload...`"
        )
        differ = 100 - ((c_size / o_size) * 100)
        caption = f"**Original Size: **`{humanbytes(o_size)}`\n"
        caption += f"**Compressed Size: **`{humanbytes(c_size)}`\n"
        caption += f"**Compression Ratio: **`{differ:.2f}%`\n"
        caption += f"\n**Time Taken To Compress: **`{difff}`"
        mmmm = await uploader(
            out,
            out,
            f_time,
            xxx,
            "Uploading " + out + "...",
        )
        await e.client.send_file(
            e.chat_id,
            mmmm,
            caption=caption,
            force_document=True,
            reply_to=e.reply_to_msg_id,
        )
        await xxx.delete()
        os.remove(out)
        os.remove(progress)
      
        
            
