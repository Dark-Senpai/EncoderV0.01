# @dark-senpai

#_______________ Import Vital items ________________#

from telethon import events, Button
from config import bot, bot_username
from TelethonDownloader.TelethonLibrary.fast_download import(
  progress_upload, 
  progress_download,
  bash
)
import subprocess
import asyncio
import os

#_______________ Startup _________________#
@bot.on(events.NewMessage(pattern=f"/start{bot_username}"))
async def _(event):
  xx = f"""
  Hello, {event.sender.first_name}, Its nice to meet ya!
  This is a **Video Encoder** Bot Which encodes your video files (animes/movies/series/news)
  in low size ( 480p ) with good quality.
  Encode videos in 480p resolution.
  This bot takes a bit time than other telegram video compressing bots due to encoding settings.
  (c) @Animes_Encoded 
  """
  await event.reply(
    xx,
    buttons=[
      [Button.url("Boss", url="https://t.me/Bro_isDarkal")]
      )]
    )
#_______________ ls _______________________#
async def _(event):
#________________ Encode __________________#
@bot.on(events.NewMessage(pattern=f"/encode{bot_username}"))
async def _(event):
  mesh = await event.get_reply_message()
  fuk = await event.reply("📥 Downloading 📥")
  file = await progress_download(bot, mesh, fuk, "./downloads/")
  file = file.split("/")[-1]
  print(file)
  await fuk.edit("⏰ Encoding In **Progress**")
  await bash(f'ffmpeg -i "{file}" -map 0 -c:v libx265 -crf 30 -c:a libopus -ab 40k  -s 854x480 -pix_fmt yuv420p -preset veryfast "[ENCODED] {file}"'
  final_file = await progress_upload(bot, f"./downloads/[ENCODED] {file}", fuk)
  os.remove(f"./downloads/{file}")
  os.remove(f"./downloads/[ENCODED] {file}")
  await event.reply(f"./downloads/[ENCODED] {file}", file=final_file, force_document=True)
  await asyncio.sleep(5)
             

             

             
             
             
             
       
  
  
  
  
        
        
      
    
                  
       
       
      
  
  



