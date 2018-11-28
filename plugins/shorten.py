import config
import requests
import urllib.request
bot = config.bot

def shorten(msg):
    if msg.get('text'):
        if msg['text'].startswith('!sh'):
            text = msg['text'][3:]
            if text == '':
                bot.sendMessage(msg['chat']['id'], '*Uso:* `/shorten google.com` - _Encurta uma URL. Powered by_ 🇧🇷.ml', 'Markdown', reply_to_message_id=msg['message_id'])
            else:
                url = urllib.request.urlopen("http://trimit.gq/api?create&key=NjwzV39FqhKnumcX5gpBasObWYSZie4Adl7&link={}").format(msg['text'][3:])
                print(url.read())
                #bot.sendMessage(msg['chat']['id'], '*Resultado:* {}'.format(r.json()['Link']), 'Markdown', reply_to_message_id=msg['message_id'])
