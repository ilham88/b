import amanobot
import dotenv
import os
bot_key = os.environ["TOKEN"]
bot = amanobot.Bot(os.environ["TOKEN"]) #Token do bot
# ''
me = bot.getMe()
bot_username = me['username']
bot_id = me['id']
from dotenv import load_dotenv
# OR, the same with increased verbosity:
load_dotenv(verbose=True)

git_repo = 'https://github.com/AmanoTeam/EduuRobot' #Repositório onde seu bot está

max_time = 60

version = '1.1.0 BT'
logs = '-1001145151462'

sudoers = [197005208]

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
