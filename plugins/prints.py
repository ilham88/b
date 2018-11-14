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

bot = config.bot
papi = os.environ["screenshots"]

def prints(msg):
    if msg.get('text'):
        if msg['text'].startswith('/print ') or msg['text'].startswith('!print '):
            try:
                bot.sendPhoto(msg['chat']['id'], f"https://api.thumbnail.ws/api/{papi}/thumbnail/get?url={urllib.parse.quote_plus(msg['text'][7:])}&width=1280",
                              reply_to_message_id=msg['message_id'])
            except Exception as e:
                bot.sendMessage(msg['chat']['id'], f'Ocorreu um erro ao enviar a print, favor tente mais tarde.\nDescrição do erro: {e.description}',
                                reply_to_message_id=msg['message_id'])
             else:
                bot.sendMessage(msg['chat']['id'], 'Use: /tr <lang> text to translate (can also be used when replying to a message).',
                                reply_to_message_id=msg['message_id'])
            return True
