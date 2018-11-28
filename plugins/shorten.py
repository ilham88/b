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
                    Status = b["Status"]
                    res = """*Original Link:* [Click Here ℹ️]({})
*Trimmed Link:* {}
*🆔:* `{}`
*❌ Error:* {}
*✅ Link Status:* {}""".format(text, Link, ID, Error, Status)
                    bot.sendMessage(msg['chat']['id'], res, 'Markdown', reply_to_message_id=msg['message_id'])
                    retrun true
