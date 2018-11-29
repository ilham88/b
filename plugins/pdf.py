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
def pdf(msg):
    if msg.get('text'):
        if msg['text'].startswith('.quote'):
            text = msg['text'][6:]
            if text == '':
                bot.sendMessage(msg['chat']['id'], '*Uso:* `.trim http://google.com` - _Encurta uma URL. Powered by_ 🇧🇷.ml', 'Markdown', reply_to_message_id=msg['message_id'])
            else:
                url = "http://trimit.gq/api"
                remove_spacec = url.split(' ')
                final_namec = ''.join(remove_spacec)
                query = "https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous"
                headers={"X-Mashape-Key": "kAvkvpaPUJmshT7QBh0JDUC35d5Jp137h8djsn7GvDlBT3Gj8K", "Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"}
                r = requests.get(query, headers=headers)
                if r.status_code != 404:
                        b = r.json()
                        print(b)
                        extractedDomain = tldextract.extract(final_namec)
                        domainSuffix = extractedDomain.domain + '.' + extractedDomain.suffix
                        print(domainSuffix)    
                        dlb = InlineKeyboardMarkup(inline_keyboard=[[dict(text='↗️ Visit', url='https://ddhdhd.deddd')]])
                        bot.sendMessage(msg['chat']['id'], "This is just a test", 
                            parse_mode='Markdown', reply_to_message_id=msg['message_id'], reply_markup=dlb)

