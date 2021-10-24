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
import pathlib 
from traceback import format_exc 
from datetime import datetime as dt
from FastTelethon import upload_file as uploadable 
from FastTelethon import download_file as downloadable 

# --------------------------------------------------------------------- #


# ---------------------------------------------------------------------


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


#~~~~~~~~~~~~~~~~ Fast Dl/Ul ~~~~~~~~~~~~~#
async def uploader(file, name, taime, event, msg):
    with open(file, "rb") as f:
        result = await uploadable(
            client=event.client,
            file=f,
            filename=name,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d,
                    t,
                    event,
                    taime,
                    msg,
                ),
            ),
        )
    return result


async def downloader(filename, file, event, taime, msg):
    with open(filename, "wb") as fk:
        result = await downloadable(
            client=event.client,
            location=file,
            out=fk,
            progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                progress(
                    d,
                    t,
                    event,
                    taime,
                    msg,
                ),
            ),
        )
    return result



# --------------------------Media Funcs-------------------------------- #


def make_html_telegraph(title, author, text):
    client = TelegraphPoster(use_api=True)
    client.create_api_token(title)
    page = client.post(
        title=title,
        author=author,
        author_url="https://t.me/TeamUltroid",
        text=text,
    )
    return page["url"]


def mediainfo(media):
    xx = str((str(media)).split("(", maxsplit=1)[0])
    m = ""
    if xx == "MessageMediaDocument":
        mim = media.document.mime_type
        if mim == "application/x-tgsticker":
            m = "sticker animated"
        elif "image" in mim:
            if mim == "image/webp":
                m = "sticker"
            elif mim == "image/gif":
                m = "gif as doc"
            else:
                m = "pic as doc"
        elif "video" in mim:
            if "DocumentAttributeAnimated" in str(media):
                m = "gif"
            elif "DocumentAttributeVideo" in str(media):
                i = str(media.document.attributes[0])
                if "supports_streaming=True" in i:
                    m = "video"
                m = "video as doc"
            else:
                m = "video"
        elif "audio" in mim:
            m = "audio"
        else:
            m = "document"
    elif xx == "MessageMediaPhoto":
        m = "pic"
    elif xx == "MessageMediaWebPage":
        m = "web"
    return m


# ------------------Some Small Funcs----------------


def time_formatter(milliseconds):
    minutes, seconds = divmod(int(milliseconds / 1000), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    tmp = (
        ((str(weeks) + "w:") if weeks else "")
        + ((str(days) + "d:") if days else "")
        + ((str(hours) + "h:") if hours else "")
        + ((str(minutes) + "m:") if minutes else "")
        + ((str(seconds) + "s") if seconds else "")
    )
    if tmp != "":
        if tmp.endswith(":"):
            return tmp[:-1]
        else:
            return tmp
    else:
        return "0 s"


def humanbytes(size):
    if size in [None, ""]:
        return "0 B"
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024:
            break
        size /= 1024
    return f"{size:.2f} {unit}"


def numerize(number):
    for unit in ["", "K", "M", "B", "T"]:
        if number < 1000:
            break
        number /= 1000
    return f"{number:.2f} {unit}"


async def progress(current, total, event, start, type_of_ps, file_name=None):
    diff = time.time() - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        time_to_completion = round((total - current) / speed) * 1000
        progress_str = "`[{0}{1}] {2}%`\n\n".format(
            "".join("●" for i in range(math.floor(percentage / 5))),
            "".join("" for i in range(20 - math.floor(percentage / 5))),
            round(percentage, 2),
        )

        tmp = (
            progress_str
            + "`{0} of {1}`\n\n`✦ Speed: {2}/s`\n\n`✦ ETA: {3}`\n\n".format(
                humanbytes(current),
                humanbytes(total),
                humanbytes(speed),
                time_formatter(time_to_completion),
            )
        )
        if file_name:
            await event.edit(
                "`✦ {}`\n\n`File Name: {}`\n\n{}".format(type_of_ps, file_name, tmp)
            )
        else:
            await event.edit("`✦ {}`\n\n{}".format(type_of_ps, tmp))


