#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function
from bs4 import BeautifulSoup
import progressbar
import requests
import sys
import re
import json
import os
import html
import time
import datetime
from datetime import datetime
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
try:
    import urllib.request
    python3 = True
except ImportError:
    import urllib2
    python3 = False
import config
import keyboard

bot = config.bot
version = config.version
bot_username = config.bot_username
### XXX: hack to skip some stupid beautifulsoup warnings that I'll fix when refactoring
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./downloads/")
def progress(current, total):
    print("Downloaded {} of {}\nCompleted {}".format(current, total, (current / total) * 100))
def make_progress_bar():
    return progressbar.ProgressBar(
        redirect_stdout=True,
        redirect_stderr=True,
        widgets=[
            progressbar.Percentage(),
            progressbar.Bar(),
            ' (',
            progressbar.AdaptiveTransferSpeed(),
            ' ',
            progressbar.ETA(),
            ') ',
        ])
dlk = keyboard.restart_dl

def shuffle(word):
    wordlen = len(word)
    word = list(word)
    for i in range(0,wordlen-1):
        pos = randint(i+1,wordlen-1)
        word[i], word[pos] = word[pos], word[i]
    word = "".join(word)
    return word

def pretty_size(size):
    units = ['B', 'KB', 'MB', 'GB']
    unit = 0
    while size >= 1024:
        size /= 1024
        unit += 1
    return '%0.2f %s' % (size, units[unit])

APPS = []


def search(given_query):
    res = requests.get('https://apkpure.com/search?q={}&region='.format(quote_plus(given_query)), headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.5'
    }).text
    soup = BeautifulSoup(res, "html.parser")
    for i in soup.find('div', {'id': 'search-res'}).findAll('dl', {'class': 'search-dl'}):
        app = i.find('p', {'class': 'search-title'}).find('a')
        APPS.append((app.text,
                     i.findAll('p')[1].find('a').text,
                     'https://apkpure.com' + app['href']))


def download(link):
    res = requests.get(link + '/download?from=details', headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.5'
    }).text
    soup = BeautifulSoup(res, "html.parser").find('a', {'id': 'download_link'})
    if soup['href']:
        r = requests.get(soup['href'], stream=True, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.5 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.5'
        })
        with open(link.split('/')[-1] + '.apk', 'wb') as file:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
def dados(msg):
    if msg.get('text'):
        if msg['text'].startswith('!dl'):
            input_str = msg['text'][3:]
            if input_str == '':
                bot.sendMessage(msg['chat']['id'], '*Use:* `/dl or !dl <url/link>`',
                                parse_mode='Markdown',
                                reply_to_message_id=msg['message_id'])
            else:
                search(" ".join(input_str))
                if len(APPS) > 0:
                    print('Downloading {}.apk ...'.format(APPS[00][2].split('/')[-1]))
                    download(APPS[00][2])
                    print('Download completed!')
                    apk_file = format(APPS[00][2].split('/')[-1]) + '.apk'

                    with warnings.catch_warnings():
                        warnings.simplefilter("ignore")
                        apk = APK(apk_file)
                    # print(apk.package)
                    # print(apk.version_name)
                        apk_version_name = apk.version_name
                # print(apk.version_code)
                        apk_version_code = apk.version_code
                        print(apk.icon_info)
                        print(apk.icon_data)
                        apk_name = apk.application
                        print('Apk Name : '+apk_name)
                        print(apk_name + ' ' + apk_version_name + '_' + apk_version_code + '.apk')
                        os.rename(apk_file, apk_name+' '+apk_version_name+'_'+apk_version_code+'.apk')
                        copyfile(apk_file, apk_name + ' ' + apk_version_name + '_' + apk_version_code + '.apk')
                        os.remove(apk_file)
                        shutil.move(apk_file, apk_name+' '+apk_version_name+'_'+apk_version_code+'.apk')
        else:
            print('No results')
    else:
        print('Missing apk package name')
        print('apkdl_downloader apk_package_name')
