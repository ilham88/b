import amanobot
import dotenv
import os
bot = amanobot.Bot(os.environ.get("TOKEN")) #Token do bot
# '777521418:AAF7wBnFBfZLmDp8ZqQXwALwLFsTe6igNdE'
me = bot.getMe()
bot_username = me['username']
bot_id = me['id']
from dotenv import load_dotenv
# OR, the same with increased verbosity:
load_dotenv(verbose=True)

git_repo = 'https://github.com/AmanoTeam/EduuRobot' #Repositório onde seu bot está

max_time = 60

VERSION = os.environ['VERSION']
LOGS = os.environ["LOGS"]

sudoers = [
    123892996, 200097591, 204807919,
    269122834, 276145711, 282809263,
    337730276, 398410916, 481445653,
    582005141
]

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
