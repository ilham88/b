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
        if msg['text'].startswith('/pypi ') or msg['text'].startswith('!pypi '):
          text = msg['text'][6:]
          r = requests.get(f"https://pypi.python.org/pypi/{text}/json", headers={"User-Agent": "Eduu/v1.0_Beta"})
          if r.ok:
              pypi = escape_definition(r.json()["info"])
              MESSAGE = "<b>%s</b> by <i>%s</i> (%s)\n" \
                        "Platform: <b>%s</b>\n" \
                        "Version: <b>%s</b>\n" \
                        "License: <b>%s</b>\n" \
                        "Summary: <b>%s</b>\n" % (pypi["name"], pypi["author"], pypi["author_email"], pypi["platform"],
                                                  pypi["version"], pypi["platform"], pypi["summary"])
              return bot.sendMessage(msg['chat']['id'], MESSAGE, reply_to_message_id=msg['message_id'], parse_mode="HTML", disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(inline_keyboard=[
    [dict(text='Package home page', url='{}'.format(pypi['home_page']))]]))
          else:
              return bot.sendMessage(msg['chat']['id'], f"Cant find *{text}* in pypi", reply_to_message_id=msg['message_id'], parse_mode="Markdown", disable_web_page_preview=True)           
