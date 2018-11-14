import config
import urllib
import dotenv
from gsearch import *
from gsearch.googlesearch import search
import wikipedia
from google_images_download import google_images_download
import urbandict
import logger
from bs4 import BeautifulSoup
from datetime import datetime
import os
import re
from amanobot.namedtuple import InlineKeyboardMarkup
import config
import requests
import re
import html

bot = config.bot
bot_username = config.bot_username
GLOBAL_LIMIT = 9
# TG API limit. An album can have atmost 10 media!
TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./../DOWNLOADS/")


def progress(current, total):
    print("Downloaded {} of {}\nCompleted {}".format(current, total, (current / total) * 100))
def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def escape_definition(definition):
    for key, value in definition.items():
        if isinstance(value, str):
            definition[key] = html.escape(cleanhtml(value))
    return definition

def prints(msg):
    if msg.get('text'):
        if msg['text'].startswith('/g') or msg['text'].startswith('!g'):
            text = msg['text'][2:]
            input_str = msg['text'][2:]
            if text == '':
                bot.sendMessage(msg['chat']['id'], '*Uso:* `/ip IP/endereço`',
                                parse_mode='Markdown',
                                reply_to_message_id=msg['message_id'])
            else:
                req = search(input_str, num_results=GLOBAL_LIMIT)
                x = ''
                for i in req:
                    x += "*{}*: `{}`\n".format(i.title(), req[i])
                bot.sendMessage(msg['chat']['id'], x, 'Markdown',
                                reply_to_message_id=msg['message_id'])
                try:
                    bot.sendLocation(msg['chat']['id'],
                                     latitude=req['lat'],
                                     longitude=req['lon'],
                                     reply_to_message_id=msg['message_id'])
                except KeyError:
                    pass
