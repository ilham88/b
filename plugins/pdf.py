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
        if msg['text'].startswith('.quote'):
            text = msg['text'][6:]
            if text == '':
                bot.sendMessage(msg['chat']['id'], '*Uso:* `.trim http://google.com` - _Encurta uma URL. Powered by_ 🇧🇷.ml', 'Markdown', reply_to_message_id=msg['message_id'])
            else:
                text = text.replace("http://","")
                text = text.replace("https://","")
                if not re.match(r'http(s?)\:', text):
                    url = 'http://' + text
                    parsed = urlsplit(url)
                    host = parsed.netloc
                    if host.startswith('www.'):
                        host = host[4:]
                    remove_spacec = url.split(' ')
                    final_namec = ''.join(remove_spacec)
                    r = requests.get('http://trimit.gq/api?create&key=NjwzV39FqhKnumcX5gpBasObWYSZie4Adl7&link={}'.format(final_namec))
                    query = "https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous"
                    rs = urlrequest.Request(query,data=None,headers={"X-Mashape-Key": "kAvkvpaPUJmshT7QBh0JDUC35d5Jp137h8djsn7GvDlBT3Gj8K", "Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"})
                    print(rs)
                 
