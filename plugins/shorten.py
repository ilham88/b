import config
import requests
import urllib.request
from urllib.parse import urlparse, urlsplit
import http.client, sys, re
from os.path import splitext
bot = config.bot
import tldextract
from amanobot.namedtuple import InlineKeyboardMarkup
from amanobot.exception import TelegramError, NotEnoughRightsError
import keyboard
from tldextract import extract
def shorten(msg):
    if msg.get('text'):
        if msg['text'].split()[0] == '!q':
            query = "https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous"
            headers={"X-Mashape-Key": "kAvkvpaPUJmshT7QBh0JDUC35d5Jp137h8djsn7GvDlBT3Gj8K", "Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}
            r = requests.get(query, headers=headers)
            if r.status_code != 404:
                b = r.json()
                print(b)
                quote = b[0]["quote"]
                author = b[0]["author"]
                category = b[0]["category"]
                req = "ℹ️ Popular Quote"
                icon = "💬"
            bot.sendMessage(msg['chat']['id'], "\n\n*{}*\n\n*👤 Author:* `{}`\n\n*🔖 Category:* `{}`\n\n*{} Content:* {}".format(req, author, category, icon, quote), 
                            parse_mode='Markdown', reply_to_message_id=msg['message_id'])
