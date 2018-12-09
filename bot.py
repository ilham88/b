

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



@app.on_message(Filters.text & Filters.chat("Bfas237group"))
def move(client, message):
  if "Oft" in message.text:
      client.send_message("bfas237off", "[{}](tg://user?id={}) **wrote:**\n{}\n\n**⬇️ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛɪɴᴜᴇ ʜᴇʀᴇ ⬇️**".format(message.reply_to_message.from_user.first_name, message.reply_to_message.from_user.id, message.reply_to_message.text))
      message.reply("I moved this discussion to the [Offtopic Group ↗️](https://t.me/bfas237off/{})".format(message.reply_to_message.message_id, message.reply_to_message.text), reply_to_message_id=message.reply_to_message.message_id, quote=True)
      client.delete_messages(
    "Bfas237group",
    message_ids=message.message_id
)
@app.on_message(Filters.text & Filters.chat("bfas237off"))
def move(client, message):
    if "Ont" in message.text:
        client.send_message("Bfas237group", "[{}](tg://user?id={}) **wrote:**\n{}\n\n**⬇️ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛɪɴᴜᴇ ʜᴇʀᴇ ⬇️**".format(message.reply_to_message.from_user.first_name, message.reply_to_message.from_user.id, message.reply_to_message.text))
        message.reply("The Main group has been created for this discussion so why not join [Offtopic Group ↗️](https://t.me/bfas237off/{})".format(message.reply_to_message.message_id, message.reply_to_message.text), reply_to_message_id=message.reply_to_message.message_id, quote=True)
        client.delete_messages(
    "bfas237off",
    message_ids=message.message_id
)
 # Automatically start() and idle()
@app.on_message(Filters.text & Filters.chat("bfas237off"))
def dl(client, message):
    if "dt" in message.text:
        client.send_document("bfas237off", "config.ini", caption="test",  reply_to_message_id=message.reply_to_message.message_id)
        
        client.delete_messages(
    "bfas237off",
    message_ids=message.message_id
)
        
app.run() 
    
