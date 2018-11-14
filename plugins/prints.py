import config
import urllib
import dotenv
from gsearch import *
from gsearch.googlesearch import search
import wikipedia
from google_images_download import google_images_download
import urbandict
import logger
from bs4 import BeautifulSoup
from datetime import datetime
import os
import re
from amanobot.namedtuple import InlineKeyboardMarkup
import config
import requests
import re
import html
import time
bot = config.bot
bot_username = config.bot_username
GLOBAL_LIMIT = 9
# TG API limit. An album can have atmost 10 media!
TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./../DOWNLOADS/")


def progress(current, total):
    print("Downloaded {} of {}\nCompleted {}".format(current, total, (current / total) * 100))
def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def escape_definition(definition):
    for key, value in definition.items():
        if isinstance(value, str):
            definition[key] = html.escape(cleanhtml(value))
    return definition

def prints(msg):
    if msg.get('text'):
        if msg['text'].startswith('/s') or msg['text'].startswith('!s'):
            input_str = msg['text'][3:]
            if input_str == '':
                bot.sendMessage(msg['chat']['id'], '*Use:* `/s or !g <search query>`',
                                parse_mode='Markdown',
                                reply_to_message_id=msg['message_id'])
            else:
                sent = bot.sendMessage(msg['chat']['id'], '*Processing your request..... 🔁*', 'Markdown', reply_to_message_id=msg['message_id'])[
                'message_id']
                start = datetime.now()
                req = search(input_str, num_results=GLOBAL_LIMIT)
                x = ''
                for text, url in req:
                    x += "  🔎 [{}]({}) \n\n".format(text, url)
                end = datetime.now()
                ms = (end - start).seconds
                bot.editMessageText((msg['chat']['id'], sent), "searched Google for {} in {} seconds. \n\n{}".format(input_str, ms, x), 'Markdown', disable_web_page_preview=True)
                
                
       
    
def prints(msg):
    if msg.get('text'):
        if msg['text'].startswith('/w') or msg['text'].startswith('!w'):
            match = msg['text'][3:]
            if match == '':
                bot.sendMessage(msg['chat']['id'], '*Use:* `/w or !w <search query>`',
                                parse_mode='Markdown',
                                reply_to_message_id=msg['message_id'])
            else:
                sents = bot.sendMessage(msg['chat']['id'], '*Processing wiki query..... 🔁*', 'Markdown', reply_to_message_id=msg['message_id'])[
                'message_id']
                result=wikipedia.summary(match)
                bot.editMessageText((msg['chat']['id'], sents), '**Search:**\n`' + match + '`\n\n**Result:**\n' + result, 'Markdown', disable_web_page_preview=True)
    

def prints(msg):
    if msg.get('text'):
        if msg['text'].startswith('/u') or msg['text'].startswith('!u'):
            str = msg['text'][3:]
            if str == '':
                bot.sendMessage(msg['chat']['id'], '*Use:* `/u or !u <search query>`',
                                parse_mode='Markdown',
                                reply_to_message_id=msg['message_id'])
            else:
                sents = bot.sendMessage(msg['chat']['id'], '*Performing dictionary query..... 🔁*', 'Markdown', reply_to_message_id=msg['message_id'])[
                'message_id']
                mean = urbandict.define(str)
                try:
                    return bot.editMessageText((msg['chat']['id'], sents), 'Text: **'+str+'**\n\nMeaning: **'+mean[0]['def']+'**\n\n'+'Example: \n__'+mean[0]['example']+'__', 'Markdown', disable_web_page_preview=True)
                except Exception as error:
                    return bot.editMessageText((msg['chat']['id'], sents), "Can't find *{str}* in the dictionary", parse_mode="Markdown", disable_web_page_preview=True)
                
def prints(msg):
    if msg.get('text'):
        if msg['text'].startswith('/screen') or msg['text'].startswith('!screen'):
            input_str = msg['text'][8:]
            if input_str == '':
                bot.sendMessage(msg['chat']['id'], '*Use:* `/s or !g <search query>`',
                                parse_mode='Markdown',
                                reply_to_message_id=msg['message_id'])
            else:
                sent = bot.sendMessage(msg['chat']['id'], '*Capturing website in progress..... 🔁*', 'Markdown', reply_to_message_id=msg['message_id'])[
                'message_id']
                start = datetime.now()
                sample_url = "https://api.screenshotlayer.com/api/capture?access_key={}&url={}"
    			# https://stackoverflow.com/a/23718458/4723940
    			contentType = response_api.headers['content-type']
    			if "image" in contentType:
        			temp_file_name = "screenshotlayer.jpg"
        			with open(temp_file_name, "wb") as fd:
            		for chunk in response_api.iter_content(chunk_size=128):
                		fd.write(chunk)
        			try:
            			bot.sendPhoto(
                				msg['chat']['id'],
                				temp_file_name,
                				caption=input_str,
                				reply_to_message_id=msg['message_id'])
            			bot.deleteMessage(msg['chat']['id'], sent)
        			except:
            			bot.editMessageText((msg['chat']['id'], sent), response_api.text, 'Markdown', disable_web_page_preview=True)
        				os.remove(temp_file_name)
    			else:
        				bot.editMessageText((msg['chat']['id'], sent), response_api.text, 'Markdown', disable_web_page_preview=True)
