import config
import requests

bot = config.bot

def shorten(msg):
    if msg.get('text'):
        if msg['text'].startswith('!sh'):
            text = msg['text'][3:]
            if text == '':
                bot.sendMessage(msg['chat']['id'], '*Uso:* `/shorten google.com` - _Encurta uma URL. Powered by_ 🇧🇷.ml', 'Markdown', reply_to_message_id=msg['message_id'])
            else:
                r = requests.post('http://trimit.gq/api?create&key=NjwzV39FqhKnumcX5gpBasObWYSZie4Adl7&link=', data=dict(url=text))
                tr = r.json()
                print(tr)
                bot.sendMessage(msg['chat']['id'], '*Resultado:* {}'.format(r.json()['Link']), 'Markdown',
                                reply_to_message_id=msg['message_id'])
