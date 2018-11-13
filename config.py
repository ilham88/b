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
enabled_plugins = [
    'processamsg',
    'start',
    'shorten',
    'kibe',
    'traduzir',
    'inlines',
    'admins',
    'prints',
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
    'diversos'
]
