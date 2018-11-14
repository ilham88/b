import config
import requests
import dotenv
from gsearch import *
from gsearch.googlesearch import search
import wikipedia
from google_images_download import google_images_download
import urbandict
import logger
import os




bot = config.bot

GLOBAL_LIMIT = 9
# TG API limit. An album can have atmost 10 media!
TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./../DOWNLOADS/")


def progress(current, total):
    print("Downloaded {} of {}\nCompleted {}".format(current, total, (current / total) * 100))


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

def github(msg):
    if msg.get('text'):
        if msg['text'].startswith('/g'):
            start = datetime.now()
            if msg['text'][3:] == '':
                res = '*Uso:* `/gith <cidade>` - _Obtem informações meteorológicas da cidade._'
            else:
                sent_id = bot.sendMessage(msg['chat']['id'], 'Obtendo informações do vídeo...', 'Markdown',
                                          reply_to_message_id=msg['message_id'])['message_id']
                
                search_results = search(msg['text'][3:], num_results=GLOBAL_LIMIT)
                output_str = " "
                for text, url in search_results:
                    output_str += "  🔎 [{}]({}) \n\n".format(text, url)
                end = datetime.now()
                ms = (end - start).seconds  
                res = "searched Google for {} in {} seconds. \n{}"
                bot.sendMessage(msg['chat']['id'], res.format(msg['text'][3:], ms, output_str), link_preview=False, 'Markdown', reply_to_message_id=msg['message_id'])
                return True
