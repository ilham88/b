import config
import urllib
import dotenv
import wikipedia
import logger
import os
import re
from amanobot.namedtuple import InlineKeyboardMarkup
import config
import requests
import html
import time
bot = config.bot
bot_username = config.bot_username

def wiki(msg):
    if msg.get('text'):
        if msg['text'].startswith('/w') or msg['text'].startswith('!w') or msg['text'].startswith('#w'):
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
    
