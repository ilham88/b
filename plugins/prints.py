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
            text = msg['text'][6:]

            if text == '':
                bot.sendMessage(msg['chat']['id'], '*Uso:* /ytdl URL do vídeo ou nome', 'Markdown',
                                reply_to_message_id=msg['message_id'])
            else:
                sent_id = bot.sendMessage(msg['chat']['id'], 'Obtendo informações do vídeo...', 'Markdown',
                                          reply_to_message_id=msg['message_id'])['message_id']
                try:
                    bot.sendPhoto(msg['chat']['id'], f"https://api.thumbnail.ws/api/{papi}/thumbnail/get?url={urllib.parse.quote_plus(msg['text'][7:])}&width=1280",
                              reply_to_message_id=msg['message_id'])
                except Exception as e:
                    bot.sendMessage(msg['chat']['id'], f'Ocorreu um erro ao enviar a print, favor tente mais tarde.\nDescrição do erro: {e.description}',
                                reply_to_message_id=msg['message_id'])
            
                return True
