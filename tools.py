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


import asyncio
import glob
import math
import os
import re
import sys
import time
import datetime as dt
import pathlib 

from FastTelethon import upload_file, download_file

# --------------------------------------------------------------------- #
async def bash(cmd):
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    err = stderr.decode().strip()
    out = stdout.decode().strip()
    return out, err

#_____________________ Fast Download / Fast Upload ____________________#

sys.path.insert(0, f"{pathlib.Path(__file__).parent.resolve()}")


class Timer:
    def __init__(self, time_between=5):
        self.start_time = time.time()
        self.time_between = time_between

    def can_send(self):
        if time.time() > (self.start_time + self.time_between):
            self.start_time = time.time()
            return True
        return False

def progress_bar_str(done, total):
    percent = round(done/total*100, 2)
    strin = "░░░░░░░░░░░░░░░░░░░░"
    strin = list(strin)
    for i in range(round(percent)//5):
        strin[i] = "█"
    strin = "".join(strin)
    final = f"Percent: {percent}%\n{human_readable_size(done)}/{human_readable_size(total)}\n{strin}"
    return final 

def human_readable_size(size, decimal_places=2):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB']:
        if size < 1024.0 or unit == 'PB':
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"

async def fast_download(client, msg, reply = None, download_folder = None, progress_bar_function = progress_bar_str):
    timer = Timer()

    async def progress_bar(downloaded_bytes, total_bytes):
        if timer.can_send():
            data = progress_bar_function(downloaded_bytes, total_bytes)
            await reply.edit(f"📥 Downloading 📥 ....\n{data}")

    file = msg.document
    filename = msg.file.name
    dir = "downloads/"

    try:
        os.mkdir("downloads/")
    except:
        pass

    if not filename:
        filename = (
            "video_" + dt.now().isoformat("_", "seconds") + ".mp4"
                    )
                    
    if download_folder == None:
        download_location = dir + filename
    else:
        download_location = download_folder + filename 

    with open(download_location, "wb") as f:
        if reply != None:
            await download_file(
                client=client, 
                location=file, 
                out=f,
                progress_callback=progress_bar
            )
        else:
            await download_file(
                client=client, 
                location=file, 
                out=f,
            )
    await reply.edit("♨️ Finished Downloading..")
    return download_location

async def fast_upload(client, file_location, reply=None, name=None, progress_bar_function = progress_bar_str):
    timer = Timer()
    if name == None:
        name = file_location.split("/")[-1]
    async def progress_bar(downloaded_bytes, total_bytes):
        if timer.can_send():
            data = progress_bar_function(downloaded_bytes, total_bytes)
            await reply.edit(f"📤 Uploading 📤...\n{data}")
    if reply != None:
        with open(file_location, "rb") as f:
            the_file = await upload_file(
                client=client,
                file=f,
                name=name,
                progress_callback=progress_bar
            )
    else:
        with open(file_location, "rb") as f:
            the_file = await upload_file(
                client=client,
                file=f,
                name=name,
            )
        
    await reply.edit("♨️ Finished uploading..")
    return the_file
#__________________ Done _________________#