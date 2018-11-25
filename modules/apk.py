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
    input_st = event.pattern_match.group(1)
    app_name = input_st.split('/')[-1]
    await event.edit("🔁 getting download link for *{}*".format(app_name))
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    site = "https://apkpure.com"
    url = "https://apkpure.com/search?q=%s" %(app_name)
    html = requests.get(url)
    parse = BeautifulSoup(html.text)
    for i in parse.find("p"):
        a_url = i["href"]
        app_url = site + a_url + "/download?from=details"
        html2 = requests.get(app_url).text
        parse2 = BeautifulSoup(html2, features="lxml")
        links = []
        for link in parse2.find_all('a', {'id': 'download_link'})
            links.append(link.get('href'))
            downloadlink = link.get('href')
            word = "123456789abcdefgh-_"
            servers = shuffle(word)
            await event.edit("⬇️ downloading from [{}.apkpure.com]({}) in progress...".format(servers, downloadlink))
            required_file_name = TEMP_DOWNLOAD_DIRECTORY + "" + app_name + ".apk"
            start = datetime.now()
            chunk_size = 1024
            headers = {'Accept-Language': 'en-US,en;q=0.9,te;q=0.8'}
            r = requests.get(downloadlink,  allow_redirects=True, stream=True, headers=headers) 
            with open(required_file_name, "wb") as apk:
                total_length = r.headers.get('content-length')
                if total_length is None:
                    fd.write(r.content)
                else:
                    dl = 0
                    total_length = int(total_length)
                    for chunk in r.iter_content(chunk_size=chunk_size):
                        dl += len(chunk)
                        apk.write(chunk)
                        apk.flush()
                        done = int(100 * dl / total_length)
                        upload_progress_string = "Uploading [%s of %s]" % (str(dl), str(pretty_size(total_length)))
                        download_progress_string = "Downloading ... [%s%s]" % ('=' * done, ' ' * (50-done))
                        print(download_progress_string)
        await event.edit("⬇️ Downloading *{}* to My local server \n\n {}".format(app_name, download_progress_string))   
        end = datetime.now()
        ms = (end - start).seconds
        await event.edit("Downloaded to `{}` in {} seconds.".format(required_file_name, ms))
    else:
        await event.edit("Reply to a message to download to my local server.")
