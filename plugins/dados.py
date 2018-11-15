#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function
from bs4 import BeautifulSoup
import progressbar
import requests
import sys
import config
import requests
import re
try:
    import urllib.request
    python3 = True
except ImportError:
    import urllib2
    python3 = False
bot = config.bot
bot_username = config.bot_username
### XXX: hack to skip some stupid beautifulsoup warnings that I'll fix when refactoring
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='bs4')


 

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

def download_apk(app_name, download_link):
    print("{+} downloading %s" %(app_name))
    output_file = "output/" + app_name + ".apk"
    r = requests.get(url=download_link, stream=True)
    with open(output_file, 'wb') as f:
        total_length = int(r.headers.get('content-length'))
        bar = make_progress_bar()
        bar.start(total_length)
        readsofar = 0
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                readsofar += len(chunk)
                bar.update(readsofar)
                f.write(chunk)
                f.flush()
        bar.finish()
    print("{+} done. file saved to %s" %(output_file))

def dados(msg):
    if msg.get('text'):
        if msg['text'].startswith('/dl') or msg['text'].startswith('!dl'):
            input_str = msg['text'][3:]
            if input_str == '':
                bot.sendMessage(msg['chat']['id'], '*Use:* `/dl or !dl <url/link>`',
                                parse_mode='Markdown',
                                reply_to_message_id=msg['message_id'])
            else:
                app_name = input_str.split('/')[-1]
                sent = bot.sendMessage(msg['chat']['id'], "{+} getting download link for {}".format(app_name), 'Markdown', reply_to_message_id=msg['message_id'])['message_id']
                site = "https://apkpure.com"
                url = "https://apkpure.com/search?q=%s" %(app_name)
                html = requests.get(url)
                parse = BeautifulSoup(html.text)
                for i in parse.find("p"):
                    a_url = i["href"]
                    app_url = site + a_url + "/download?from=details"
                    html2 = requests.get(app_url)
                    parse2 = BeautifulSoup(html2.text)
                    for link in parse2.find_all("a",id="download_link"):
                        download_link = link["href"]
                        bot.editMessageText((msg['chat']['id'], sent), "{+} downloading {}".format(app_name), 'Markdown', disable_web_page_preview=True)
                        bot.sendChatAction(msg['chat']['id'], 'upload_document')
                        bot.sendDocument(msg['chat']['id'], output_file, reply_to_message_id=msg['message_id'])
                        bot.editMessageText((msg['chat']['id'], sent), "done. file savede", 'Markdown', disable_web_page_preview=True)
                        return True     
    
def main(args):
    if len(args) != 2:
        sys.exit("use: %s com.blah.blah" %(args[0]))
    get_apk(args[1])

if __name__ == "__main__":
    main(args=sys.argv)


                
