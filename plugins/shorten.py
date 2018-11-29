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
        if msg['text'].startswith('.trim'):
            text = msg['text'][5:]
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
                
                    extractedDomain = tldextract.extract(final_namec)
                    domainSuffix = extractedDomain.domain + '.' + extractedDomain.suffix
                
                    print(domainSuffix)
                    
                    smsg = 'Hello there! to know more about me, start me in private and understand how i work.'
                    if r.status_code != 404:
                        b = r.json()
                        print(b)
                        Link = b["Link"]
                        ID = b["ID"]
                        Error = b["Error"]
                        u = requests.get('http://trimit.gq/api?stats&key=NjwzV39FqhKnumcX5gpBasObWYSZie4Adl7&id={}'.format(ID))
                        c = u.json()
                        print(c)
                        Clicks = c["Clicks"]
                        if b["Status"] != True:
                            req = "😭 Your Link encountered a Glitch"
                            inf = "" 
                            Status = b["Error"]
                            icon = "❌"
                        else:
                            req = "ℹ️ Link Details Below"
                            inf = "(Used for stats)"
                            Status = b["Status"]
                            icon = "✅"
                            
                        teclado = keyboard.start
                        rstx = [dict(text='⭐ ↗️ Visit Now', url='#')]

                        bot.sendMessage(msg['chat']['id'], "\n\n*{}*\n\n*Trimmed Link:* {}\n\n*🆔:* `{}`\n\n*👀 Clicks:* {}\n\n*{} Link Status:* {}".format(req, Link, ID, Clicks, icon, Status), 
                            parse_mode='Markdown', reply_to_message_id=msg['message_id'], reply_markup=rstx)
