import config
import requests
import dotenv
import os



url = 'https://api.github.com/users/{}'
bot = config.bot

def github(msg):
    if msg.get('text'):
        if msg['text'].startswith('/gith'):
            if msg['text'][6:] == '':
                res = '*Uso:* `/gith <cidade>` - _Obtem informações meteorológicas da cidade._'
            else:
                json = requests.post(url.format(msg['text'][6:])).json()
                if json.status_code != 404:
                    print(json)
                    res = json['message']
                else:
                    res = """[\u2063]({})Name: [{}]({})
Type: {}
Company: {}
Blog: {}
Location: {}
Bio: {}
Profile Created: {}""".format(json['avatar_url'], json['name'], json['html_url']['gh_type'],
                              json['company']['blog'], json['location'], json['bio'], json['created_at'])
            bot.sendMessage(msg['chat']['id'], res, 'Markdown', reply_to_message_id=msg['message_id'])
            return True

