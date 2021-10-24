from val_cfg import get_config

#______________ Vars ________________#
class vars(object):
  try:
    # add api_id in config.py ( get from telegram.org )
    API_ID = get_config('API_ID')
    # add api_hash in config.py ( get from telegram.org)
    API_HASH = get_config('API_HASH')
    # array! add bot_token recieved from @botfather from telegram 
    BOT_TOKEN = get_config('BOT_TOKEN')
  except Exception as e:
    print(str(e))
    exit()

    
  
#_______________ Done ___________#
