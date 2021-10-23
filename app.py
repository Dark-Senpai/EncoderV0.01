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
#________________ Stats ___________________#
@bot.on(events.NewMessage(pattern=f"/stats{bot_username}"))
async def _(event):
  files = e.pattern_match.group(1)
  if not files:
    files = "*"
  elif files.endswith("/"):
    files = files + "*"
  elif "*" not in files:
    files = files + "*/*"
  files = glob.glob(files)
  if not files:
    return await eor(e, "No Encoding Process found !", time=5)
  encoded_files = []
  for file in sorted(files):
    if str(file).endswith((".mkv", ".mp4", ".avi", ".gif", "webm")):
            encoded_files.append("🎥 " + str(file))
 omk = [*sorted(encoded_files)]
text = ""
fls, fos = 0, 0
flc, foc = 0, 0
for i in omk:
  try:
    emoji = i.split()[0]
    name = i.split(maxsplit=1)[1]
    nam = name.split("/")[-1]
    if os.path.isdir(name):
      size = 0
      for path, dirs, files in os.walk(name):
        for f in files:
          fp = os.path.join(path, f)
          size = += os.path.join(path, f)
          size += os.path.getsize(fp)
    if hb(size):
      text += emoji + f"`{nam}`" + " `" + hb(size) + "`\n"
      fos += size 
    else:
      text += emoji + f" `{nam}
    
    fls, fos = 0, 0
    flc, foc = 0, 0
    for i in omk:
        try:
            emoji = i.split()[0]
            name = i.split(maxsplit=1)[1]
            nam = name.split("/")[-1]
            if os.path.isdir(name):
                size = 0
                for path, dirs, files in os.walk(name):
                    for f in files:
                        fp = os.path.join(path, f)
                        size += os.path.getsize(fp)
                if hb(size):
                    text += emoji + f" `{nam}`" + "  `" + hb(size) + "`\n"
                    fos += size
                else:
                    text += emoji + f" `{nam}`" + "\n"
                foc += 1
            else:
                if hb(int(os.path.getsize(name))):
                    text += (
                        emoji
                        + f" `{nam}`"
                        + "  `"
                        + hb(int(os.path.getsize(name)))
                        + "`\n"
                    )
                    fls += int(os.path.getsize(name))
                else:
                    text += emoji + f" `{nam}`" + "\n"
                flc += 1
        except BaseException:
            pass
    tfos, tfls, ttol = hb(fos), hb(fls), hb(fos + fls)
    if not hb(fos):
        tfos = "0 B"
    if not hb(fls):
        tfls = "0 B"
    if not hb(fos + fls):
        ttol = "0 B"
    text += f"\n\n`Folders` :  `{foc}` :   `{tfos}`\n`Files` :       `{flc}` :   `{tfls}`\n`Total` :       `{flc+foc}` :   `{ttol}`"
    try:
        await eor(e, text)
   
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
             

             

             
             
             
             
       
  
  
  
  
        
        
      
    
                  
       
       
      
  
  



