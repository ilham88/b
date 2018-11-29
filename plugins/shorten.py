import config
import requests
import urllib.request
from urllib.parse import urlparse, urlsplit
import http.client, sys, re
from os.path import splitext
bot = config.bot

def shorten(msg):
    if msg.get('text'):
        if msg['text'].startswith('.trim'):
            text = msg['text'][5:]
            if text == '':
                bot.sendMessage(msg['chat']['id'], '*Uso:* `.trim http://google.com` - _Encurta uma URL. Powered by_ 🇧🇷.ml', 'Markdown', reply_to_message_id=msg['message_id'])
            else:
                if not re.match(r'http(s?)\:', text):
                    try:
                        url_parts = urlparse(text)
                        request = requests.head("://".join([url_parts.scheme, url_parts.netloc]))
                        return request.status_code == HTTPStatus.OK
                        print(request)
                     except:
                        return False;
                        url = 'http://' + text
                        parsed = urlsplit(url)
                        host = parsed.netloc
                        if host.startswith('www.'):
                            host = host[4:]
                remove_spacec = url.split(' ')
                final_namec = ''.join(remove_spacec)
                rk = requests.head(text)
                r = requests.get('http://trimit.gq/api?create&key=NjwzV39FqhKnumcX5gpBasObWYSZie4Adl7&link={}'.format(final_namec))
                print(final_namec)
                if rk.status_code != 404:
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
                        
                    bot.sendMessage(msg['chat']['id'], "\n*{}*\n\n*Trimmed Link:* {}\n\n*🆔:* `{}`\n\n*👀 Clicks:* {}\n\n*{} Link Status:* {}".format(req, Link, ID, Clicks, icon, Status), 'Markdown', reply_to_message_id=msg['message_id'])
                else:
                    bot.sendMessage(msg['chat']['id'], "❌ There was an error with your link. Please check and try again", 'Markdown', reply_to_message_id=msg['message_id'])
