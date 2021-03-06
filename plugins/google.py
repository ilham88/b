import config
import urllib
import dotenv
from gsearch import *
from gsearch.googlesearch import search
import logger
from bs4 import BeautifulSoup
from datetime import datetime
import os
import re
import config
import requests
import time
bot = config.bot
bot_username = config.bot_username
GLOBAL_LIMIT = 9
# TG API limit. An album can have atmost 10 media!
TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./../DOWNLOADS/")



def google(msg):
    if msg.get('text'):
        if msg['text'].startswith('!s'):
            input_str = msg['text'][3:]
            if input_str == '':
                bot.sendMessage(msg['chat']['id'], '*Use:* `/s or !g <search query>`',
                                parse_mode='Markdown',
                                reply_to_message_id=msg['message_id'])
            else:
                sent = bot.sendMessage(msg['chat']['id'], '*Processing your request..... 🔁*', 'Markdown', reply_to_message_id=msg['message_id'])[
                'message_id']
                start = datetime.now()
                req = search(input_str, num_results=GLOBAL_LIMIT)
                x = ''
                for text, url in req:
                    x += "  🔎 [{}]({}) \n\n".format(text, url)
                end = datetime.now()
                ms = (end - start).seconds
                bot.editMessageText((msg['chat']['id'], sent), "searched Google for {} in {} seconds. \n\n{}".format(input_str, ms, x), 'Markdown', disable_web_page_preview=True)
                
            
