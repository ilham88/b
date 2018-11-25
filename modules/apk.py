#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function
from bs4 import BeautifulSoup
import progressbar
import subprocess
import requests
import sys
import requests
import re
import json
import os
import html
import time
import datetime
from datetime import datetime
from urllib.parse import urlparse
from os.path import splitext
from urllib.request import urlretrieve
from urllib.request import urlopen
from shutil import copyfileobj
from tempfile import NamedTemporaryFile
import threading
import pprint
import traceback
import urllib.request
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

from telethon.tl.types import DocumentAttributeVideo
from telethon.errors import MessageNotModifiedError

from PIL import Image
from random import randint
try:
    import urllib.request
    python3 = True
except ImportError:
    import urllib2
    python3 = False
    
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./downloads/")
def progress(current, total):
    print("Downloaded {} of {}\nCompleted {}".format(current, total, (current / total) * 100)) 
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



@bot.on(events.NewMessage(pattern=r".dl (.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Processing ...")
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        start = datetime.now()
        downloaded_file_name = await bot.download_media(
            await event.get_reply_message(),
            TEMP_DOWNLOAD_DIRECTORY,
            progress_callback=progress
        )
        end = datetime.now()
        ms = (end - start).seconds
        await event.edit("Downloaded to `{}` in {} seconds.".format(downloaded_file_name, ms))
    elif input_str:
        app_name = input_str.split('/')[-1]
        url = input_str.strip()
        # https://stackoverflow.com/a/761825/4723940
        file_name = app_name.strip()
        required_file_name = TEMP_DOWNLOAD_DIRECTORY + "" + file_name
        start = datetime.now()
        headers = {'Accept-Language': 'en-US,en;q=0.9,te;q=0.8'}
        r = requests.get(url, allow_redirects=True, stream=True, headers=headers)
        with open(required_file_name, "wb") as fd:
            
            total_length = r.headers.get('content-length')
            # https://stackoverflow.com/a/15645088/4723940
            if total_length is None: # no content length header
                fd.write(r.content)
            else:
                dl = 0
                total_length = int(total_length)
                for chunk in r.iter_content(chunk_size=1024):
                    dl += len(chunk)
                    fd.write(chunk)
                    done = int(100 * dl / total_length)
                    download_progress_string = "Downloading ... [%s%s]" % ('=' * done, ' ' * (50-done))
                    # download_progress_string = "Downloading ... [%s of %s]" % (str(dl), str(total_length))
                    # download_progress_string = "Downloading ... [%s%s]" % ('⬛️' * done, '⬜️' * (100 - done))
                    """try:
                        await event.edit(download_progress_string)
                    except MessageNotModifiedError as e:
                        print("__FLOODWAIT__: {} sleeping for 100seconds, before proceeding.".format(str(e)))
                    time.sleep(1)"""
                    print(download_progress_string)
        end = datetime.now()
        ms = (end - start).seconds
        await event.edit("Downloaded to `{}` in {} seconds.".format(required_file_name, ms))
    else:
        await event.edit("Reply to a message to download to my local server.")

    
    
    