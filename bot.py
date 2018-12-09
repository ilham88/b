

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

from tqdm import tqdm

import warnings
from random import randint

try:
    import urllib.request
    python3 = True
except ImportError:
    import urllib2
    python3 = False
from os import environ
from pyrogram import Client, Filters
app = Client(environ['TOKEN'])
from hurry.filesize import size, alternative
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./downloads/")
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


@app.on_message(Filters.text & Filters.chat("Bfas237group"))
def move(client, message):
  if "Oft" in message.text:
      client.send_message("bfas237off", "[{}](tg://user?id={}) **wrote:**\n{}\n\n**⬇️ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛɪɴᴜᴇ ʜᴇʀᴇ ⬇️**".format(message.reply_to_message.from_user.first_name, message.reply_to_message.from_user.id, message.reply_to_message.text))
      message.reply("I moved this discussion to the [Offtopic Group ↗️](https://t.me/bfas237off/{})".format(message.reply_to_message.message_id, message.reply_to_message.text), reply_to_message_id=message.reply_to_message.message_id, quote=True)
      client.delete_messages(
    "Bfas237group",
    message_ids=message.message_id
)
@app.on_message(Filters.chat("bfas237off"))
def move(client, message):
    if "Ont" in message.text:
        client.send_message("Bfas237group", "[{}](tg://user?id={}) **wrote:**\n{}\n\n**⬇️ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛɪɴᴜᴇ ʜᴇʀᴇ ⬇️**".format(message.reply_to_message.from_user.first_name, message.reply_to_message.from_user.id, message.reply_to_message.text))
        message.reply("The Main group has been created for this discussion so why not join [Offtopic Group ↗️](https://t.me/bfas237off/{})".format(message.reply_to_message.message_id, message.reply_to_message.text), reply_to_message_id=message.reply_to_message.message_id, quote=True)
        client.delete_messages(
    "bfas237off",
    message_ids=message.message_id
)
 # Automatically start() and idle()
@app.on_message(Filters.chat("bfas237off") & Filters.command("jl", "!"))
def dl(client, message):
    if len(message.command) > 1:
        klk = str(message.text)[3:].lstrip()
        if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        	os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
        try:
        	app_name = klk.split('/')[-1]
        	client.send_message(message.chat.id, "🔁 getting download link for {}".format(app_name))
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
                    client.edit_message_text(message.chat.id, message.message_id, "⬇️ downloading from [{}.apkpure.com]({}) in progress...".format(servers, downloadlink), parse_mode="Markdown", disable_web_page_preview=True)
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
                
                client.edit_message_text(message.chat.id, message.message_id, "⬆️ Uploading *{}* to Telegram \n\n {}".format(app_name, human_readable_progress), parse_mode="Markdown", disable_web_page_preview=True)
                time.sleep(5)
                starts = datetime.now()
                if total_length < 52428800:
                	client..send_chat_action(message.chat.id, 'upload_document')
                	client.send_document(message.chat.id, open(required_file_name, 'rb'), caption="@" + bot_username, parse_mode='Markdown')
                	time.sleep(0.5)
                	ends = datetime.now()
                	mss = (ends - starts).seconds
                	os.remove(required_file_name)
                	client.delete_messages(
                	"bfas237off",
                	message_ids=message.message_id
                	)
                else:
                	client.edit_message_text(message.chat.id, message.message_id, "⚠️ There was an error\n\n *{}* is more than 50MB limit. Unfortunately, The current download job has ended unexpectedly.\n\n Try downloading something smaller than this".format(app_name), parse_mode="Markdown", disable_web_page_preview=True)
                	os.remove(required_file_name)
                	time.sleep(60)
                	client.delete_messages(
                	"bfas237off",
                	message_ids=message.message_id
                	)
                	return True

app.run() 
    
