import config
import requests
import urllib.request
bot = config.bot

def shorten(msg):
    if msg.get('text'):
        if msg['text'].startswith('.trim'):
            text = msg['text'][3:]
            if text == '':
                res = bot.sendMessage(msg['chat']['id'], '*Uso:* `/shorten google.com` - _Encurta uma URL. Powered by_ 🇧🇷.ml', 'Markdown', reply_to_message_id=msg['message_id'])
            else:
                r = requests.get('http://trimit.gq/api?create&key=NjwzV39FqhKnumcX5gpBasObWYSZie4Adl7&link={}'.format(msg['text'][5:]))
                if r.status_code != 404:
                    b = r.json()
                    print(r.json())
                    Link = b["Link"]
                    ID = b["ID"]
                    Error = b["Error"]
                    u = requests.get('http://trimit.gq/api?stats&key=NjwzV39FqhKnumcX5gpBasObWYSZie4Adl7&id={}'.format(ID))
                    c = u.json()
                    print(c)
                    Clicks = c["Clicks"]
                    if Status != True:
                        Status = b["Error"]
                        icon = "❌"
                    else:
                        Status = b["Status"]
                        icon = "✅"
                        res = """That was a good trim. Details Below

*Trimmed Link:* {}

*🆔:* `{}`

*👀 Clicks:* {}

*{} Link Status:* {}""".format(Link, ID, Clicks, icon, Status)
                    bot.sendMessage(msg['chat']['id'], res, 'Markdown', reply_to_message_id=msg['message_id'])
                    
