import sys, io
import traceback
from amanobot.loop import MessageLoop
from contextlib import redirect_stdout
from colorama import Fore
import config
import time
import threading
from amanobot.exception import TooManyRequestsError, NotEnoughRightsError
from urllib3.exceptions import ReadTimeoutError
import db_handler as db
from telegram_upload.exceptions import catch
from telegram_upload.management import manage
import asyncio
import difflib
import html
import logging
import os
import re
import sys
import time
import urllib.parse
import click
import subprocess
from datetime import datetime
from telethon.tl.types import DocumentAttributeVideo
from telethon.errors import MessageNotModifiedError
from telethon import TelegramClient, events, types, custom, utils
from telethon.extensions import markdown
bot = TelegramClient("telegram-upload", "256406", "31fd969547209e7c7e23ef97b7a53c37")





logging.basicConfig(level=logging.WARNING)
logging.getLogger('asyncio').setLevel(logging.ERROR)


bot = config.bot

ep = []
n_ep = []


for num, i in enumerate(config.enabled_plugins):
    try:
        print(Fore.RESET + 'Loading plugins... [{}/{}]'.format(num+1, len(config.enabled_plugins)), end='\r')
        exec('from plugins.{0} import {0}'.format(i))
        ep.append(i)
    except Exception as erro:
        n_ep.append(i)
        print('\n'+Fore.RED+'Error loading the plugin {}:{}'.format(i, Fore.RESET), erro)


def handle_thread(*args):
    t = threading.Thread(target=handle, args=args)
    t.start()


def handle(msg):
    try:
        for plugin in ep:
            p = globals()[plugin](msg)
            if p:
                break
    except (TooManyRequestsError, NotEnoughRightsError, ReadTimeoutError):
        pass
    except Exception as e:
        with io.StringIO() as buf, redirect_stdout(buf):
            traceback.print_exc(file=sys.stdout)
            res = buf.getvalue()
        bot.sendMessage(config.logs, '''There was an error in the plugin {}:

{}'''.format(plugin, res))



print('\n\nBot started! {}\n'.format(config.version))

MessageLoop(bot, handle_thread).run_as_thread()
bot.start(bot_token="671045549:AAH72sek9a9jPWHbBp8vRrWL_u68J9pRXYU")
bot.run_until_disconnected()

wr = db.get_restarted()

if wr: 
    try:
        bot.editMessageText(wr, 'Restart successfully')
    except:
        pass
    db.del_restarted()
else:
    bot.sendMessage(config.logs, '''Bot Details

Verion: {}
Plugins Loaded: {}
An error occured in {} plugin(s){}'''.format(config.version, len(ep), len(n_ep), ': '+(', '.join(n_ep)) if n_ep else ''))
while True:
    time.sleep(10)
