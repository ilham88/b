import config
import requests
import dotenv
import os
import bs4 
import re
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
from urllib import request as urlrequest
try:
    import urllib.request
    python3 = True
except ImportError:
    import urllib2
    python3 = False


bot = config.bot
def pdf(msg):
    if msg.get('text'):
        if msg['text'].startswith('.q'):
            movie_name = msg['text'][2:]
            if msg['text'][2:] == '':
                res = '*Uso:* `.q <film title>` - _Otain film information from imdb db._'
            else:
                remove_space = movie_name.split(' ')
                final_name = '+'.join(remove_space)
                query = "https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous"
                r = urlrequest.Request(query,data=None,headers={
    "X-Mashape-Key": "kAvkvpaPUJmshT7QBh0JDUC35d5Jp137h8djsn7GvDlBT3Gj8K",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
  })
                print (r.body)
                t=r.body
                bot.sendMessage(msg['chat']['id'], t['quote'], 'Markdown', reply_to_message_id=msg['message_id'])
               
                return
                
