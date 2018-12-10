
#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function
from bs4 import BeautifulSoup
import progressbar
import requests
import datetime
from urllib.parse import urlparse, quote_plus
from os.path import splitext
from urllib.request import urlretrieve
from urllib.request import urlopen
from shutil import copyfileobj
from pyaxmlparser import APK
from shutil import copyfile
from tempfile import NamedTemporaryFile
import threading
import pprint
import traceback
import urllib.request
import amanobot
import amanobot.namedtuple
from tqdm import tqdm
from amanobot.namedtuple import InlineKeyboardMarkup
import warnings
from random import randint
from telegram_upload.exceptions import catch
from telegram_upload.management import manage
import asyncio
import difflib
import html
import logging
import os
import re
import sys
import time
import urllib.parse
import click
import subprocess
from datetime import datetime
from telethon.tl.types import DocumentAttributeVideo
from telethon.errors import MessageNotModifiedError
from telethon import TelegramClient, events, types, custom, utils
from telethon.extensions import markdown

logging.basicConfig(level=logging.WARNING)
logging.getLogger('asyncio').setLevel(logging.ERROR)
try:
    import urllib.request
    python3 = True
except ImportError:
    import urllib2
    python3 = False
import config
import keyboard
from hurry.filesize import size, alternative
bots = config.bot
version = config.version
bot_username = config.bot_username
### XXX: hack to skip some stupid beautifulsoup warnings that I'll fix when refactoring
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./downloads/")

dlk = keyboard.restart_dl

def shuffle(word):
    wordlen = len(word)
    word = list(word)
    for i in range(0,wordlen-1):
        pos = randint(i+1,wordlen-1)
        word[i], word[pos] = word[pos], word[i]
    word = "".join(word)
    return word

def pretty_size(sizes):
    units = ['B', 'KB', 'MB', 'GB']
    unit = 0
    while sizes >= 1024:
        sizes /= 1024
        unit += 1
    return '%0.2f %s' % (sizes, units[unit])

APPS = []
 
def download(link):
    res = requests.get(link + '/download?from=details', headers={
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.5'
        }).text
    soup = BeautifulSoup(res, "html.parser").find('a', {'id':'download_link'})
    if soup['href']:
        r = requests.get(soup['href'], stream=True, headers={
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.5'
        })
        with open(link.split('/')[-1] + '.apk', 'wb') as file:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)

def search(query):
    res = requests.get('https://apkpure.com/search?q={}&region='.format(quote_plus(query)), headers={
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.5'
        }).text
    soup = BeautifulSoup(res, "html.parser")
    for i in soup.find('div', {'id':'search-res'}).findAll('dl', {'class':'search-dl'}):
        app = i.find('p', {'class':'search-title'}).find('a')
        APPS.append((app.text,
                    i.findAll('p')[1].find('a').text,
                    'https://apkpure.com' + app['href']))
try:
    import aiohttp
except ImportError:
    aiohttp = None
    logging.warning('aiohttp module not available; #haste command disabled')

def get_env(name, message, cast=str):
    if name in os.environ:
        return os.environ[name]
    while True:
        value = input(message)
        try:
            return cast(value)
        except ValueError as e:
            print(e, file=sys.stderr)
            time.sleep(1)


bot = TelegramClient("telegram-upload", "256406", "31fd969547209e7c7e23ef97b7a53c37")



@bot.on(events.NewMessage(pattern='#dl (.+)', forwards=False))
async def handler(event):
    """#search query: Searches for "query" in the method reference."""
    s = datetime.now()
    message = await event.reply('Let me download the specified file')
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    d = datetime.now() - s
    query = event.pattern_match.group(1)
    local_filename = query.split('/')[-1]
    required_file_name = TEMP_DOWNLOAD_DIRECTORY + "" + local_filename + ".zip"
    chunk_size = 1024
    r = requests.get(query, stream = True) 
    with open(required_file_name,"wb") as apk:
        for chunk in r.iter_content(chunk_size=chunk_size):
            total_length = r.headers.get('content-length')
            dl = 0
            shutil.copyfileobj(r.raw, apk)
            if chunk:
                dl += len(chunk)
                done = int(100 * dl / total_length)
                upload_progress_string = "... [%s of %s]" % (str(dl), str(pretty_size(total_length)))
                await message.edit('Download finished! __(Download '+upload_progress_string+' took {d:.2f}s)__')
                apk.write(chunk)
                apk.flush()
    
    await asyncio.sleep(5)
    await bot.send_file("bfas237off", required_file_name, reply_to=event.id, caption="`Here is your current status`")
    await asyncio.wait([event.delete()])






bot.start(bot_token="671045549:AAH72sek9a9jPWHbBp8vRrWL_u68J9pRXYU")
bot.run_until_disconnected()

def dados(msg):
    if msg.get('text'):
        teclado = keyboard.restart_dl
        if msg['text'].startswith('!dl '):
            input_str = msg['text'][4:]
            if input_str == '':
                bots.sendMessage(msg['chat']['id'], '*Use:* `!dl <app name>`',
                                parse_mode='Markdown',
                                reply_to_message_id=msg['message_id'])
            else:
                app_name = input_str.split('/')[-1]
                sent = bots.sendMessage(msg['chat']['id'], "🔁 getting download link for {}".format(app_name), 'Markdown', reply_to_message_id=msg['message_id'])['message_id']
                if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
                    os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
                site = "https://apkpure.com"
                url = "https://apkpure.com/search?q=%s" %(app_name)
                html = requests.get(url).text
                parse = BeautifulSoup(html, features="lxml")
                for i in parse.find("p"):
                    a_url = i["href"]
                    app_url = site + a_url + "/download?from=details"
                    html2 = requests.get(app_url).text
                    parse2 = BeautifulSoup(html2, features="lxml")
                    links = []
                    for link in parse2.find_all('a', {'id': 'download_link'}):
                        links.append(link.get('href'))
                        downloadlink = link.get('href')
                        word = "123456789abcdefgh-_"
                        servers = shuffle(word)
                        bots.editMessageText((msg['chat']['id'], sent), "⬇️ downloading from [{}.apkpure.com]({}) in progress...".format(servers, downloadlink), 'Markdown', disable_web_page_preview=True)
                        #bot.deleteMessage(chat_id, sent)
                        required_file_name = TEMP_DOWNLOAD_DIRECTORY + "" + app_name + ".apk"
                        start = datetime.now()
                        chunk_size = 128
                        r = requests.get(downloadlink, stream = True) 
                        with open(required_file_name,"wb") as apk:
                            for chunk in r.iter_content(chunk_size=chunk_size):
                                total_length = r.headers.get('content-length')
                                dl = 0
                                total_length = int(total_length)
                                if chunk:
                                    dl += len(chunk)
                                    done = int(100 * dl / total_length)
                                    apk.write(chunk)
                                    apk.flush()
                                    
                    
                                    output_file_size = os.stat(required_file_name).st_size
                                    human_readable_progress = size(output_file_size, system=alternative) + " / " + \
                    size(int(r.headers["Content-Length"]), system=alternative)
                    
                                    upload_progress_string = "... [%s of %s]" % (str(dl), str(pretty_size(total_length)))
                            bots.editMessageText((msg['chat']['id'], sent), "⬆️ Uploading *{}* to Telegram \n\n {}".format(app_name, human_readable_progress), 'Markdown')
                            time.sleep(5)
                            starts = datetime.now()
                            if total_length < 52428800:
                                bots.sendChatAction(msg['chat']['id'], 'upload_document')
                                tr = bot.sendDocument(msg['chat']['id'], open(required_file_name, 'rb'), caption="@" + bot_username, parse_mode='Markdown')
                                time.sleep(0.5)
                                ends = datetime.now()
                                mss = (ends - starts).seconds
                                os.remove(required_file_name)
                                bots.deleteMessage((msg['chat']['id'],sent))
                            else:
                                bots.editMessageText((msg['chat']['id'], sent), "⚠️ There was an error\n\n *{}* is more than 50MB limit. Unfortunately, The current download job has ended unexpectedly.\n\n Try downloading something smaller than this".format(app_name), 'Markdown')
                                os.remove(required_file_name)
                                time.sleep(60)
                                bots.deleteMessage((msg['chat']['id'],sent))
                                return True




