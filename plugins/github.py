import config
import requests
import dotenv
import os


def github(msg):
    if msg.get('text'):
        if msg['text'].startswith('/gith ') or msg['text'].startswith('!gith '):
          text = msg['text'][6:]
          try:
            url = requests.get('https://api.github.com/users/{}".format(msg['text'][6:])
            r = requests.get(url)
            if r.status_code != 404:
                b = r.json()
                avatar_url = b["avatar_url"]
                html_url = b["html_url"]
                gh_type = b["type"]
                name = b["name"]
                company = b["company"]
                blog = b["blog"]
                location = b["location"]
                bio = b["bio"]
                created_at = b["created_at"]
                sent_id = bot.sendMessage(msg['chat']['id'], 'Obtendo informações do vídeo...', 'Markdown',
                                          reply_to_message_id=msg['message_id'])['message_id']
                bot.editMessageText((msg['chat']['id'],sent_id),
                                        """[\u2063]({})Name: [{}]({})
Type: {}
Company: {}
Blog: {}
Location: {}
Bio: {}
Profile Created: {}""".format(avatar_url, name, html_url, gh_type, company, blog, location, bio, created_at), 'Markdown')
                else:
                bot.editMessageText((msg['chat']['id'],sent_id), "`{}`: {}".format(input_str, r.text), 'Markdown')
