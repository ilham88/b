import config
import urllib
import dotenv
import urbandict
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

def urban(msg):
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
                
