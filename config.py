import amanobot
import dotenv
import os
bot_key = os.environ["TOKEN"]
bot = amanobot.Bot(os.environ.get("TOKEN")) #Token do bot
# ''
me = bot.getMe()
bot_username = me['username']
bot_id = me['id']


git_repo = os.environ["git_repo"] #Repositório onde seu bot está

max_time = 60

version = os.environ["version"]
logs = os.environ["logs"]

sudoers = [197005208]
keys = ['abdf158215d05e1a973510c5c81d9a2cdd99ad2c7cd8']
class Config(object):
    # get a token from https://chatbase.com
    CHAT_BASE_TOKEN = os.environ["CHAT_BASE_TOKEN"]
    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ["TG_BOT_TOKEN"]
    # your domain to show when download file is greater than MAX_FILE_SIZE
    HTTP_DOMAIN = os.environ["HTTP_DOMAIN"]
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = os.environ["DOWNLOAD_LOCATION"]
    # Telegram maximum file upload size
    MAX_FILE_SIZE = os.environ["MAX_FILE_SIZE"]
    TG_MAX_FILE_SIZE = os.environ["TG_MAX_FILE_SIZE"]
    # The Telegram API things
    APP_ID = os.environ["APP_ID"]
    API_HASH = os.environ["API_HASH"]
    # Get these values from my.telegram.org
    # for storing the Telethon session
    TL_SESSION = os.environ["TL_SESSION"]
enabled_plugins = [
    'processamsg',
    'start',
    'shorten',
    'kibe',
    'wiki',
    'urban',
    'traduzir',
    'inlines',
    'admins',
    'google',
    'pypi',
    'clima',
    'youtube',
    'ping',
    'gif',
    'reddit',
    'coub',
    'sudos',
    'id',
    'ip',
    'jsondump',
    'dados',
    'diversos',
    'github'
]
