import config
import requests
import dotenv
import os




bot = config.bot



def github(msg):
    if msg.get('text'):
        if msg['text'].startswith('/gith'):
            if msg['text'][6:] == '':
                res = '*Uso:* `/gith <cidade>` - _Obtem informações meteorológicas da cidade._'
            else:
                url = 'https://api.github.com/users/{}'.format(msg['text'][6:])
                j = requests.get(url)
                if j.status_code != 404:
                    b = j.json()
                    print(b)
                    avatar_url = b["avatar_url"]
                    html_url = b["html_url"]
                    gh_type = b["type"]
                    name = b["name"]
                    company = b["company"]
                    blog = b["blog"]
                    location = b["location"]
                    bio = b["bio"]
                    created_at = b["created_at"]
                    res = """[\u2063]({})Name: [{}]({})
Type: {}
Company: {}
Blog: {}
Location: {}
Bio: {}
Profile Created: {}""".format(avatar_url, name, html_url, gh_type, company, blog, location, bio, created_at)
            bot.sendMessage(msg['chat']['id'], res, 'Markdown', reply_to_message_id=msg['message_id'])
            return True

