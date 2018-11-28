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
        if msg['text'].startswith('!imdc'):
            movie_name = msg['text'][6:]
            if msg['text'][6:] == '':
                res = '*Uso:* `!imdc <film title>` - _Otain film information from imdb db._'
            else:
                remove_space = movie_name.split(' ')
                final_name = '+'.join(remove_space)
                page = requests.get("https://www.imdb.com/find?ref_=nv_sr_fn&q={}&s=all".format(final_name))
                lnk = str(page.status_code)
                soup = bs4.BeautifulSoup(page.content,'lxml', from_encoding='utf-8')
                results = soup.findAll("td","result_text")
                mov_title = results[0].text
                mov_link = "http://www.imdb.com/"+results[0].a['href'] 
                page1 = requests.get(mov_link)
                soup = bs4.BeautifulSoup(page1.content,'lxml')
                story_line = soup.find('div', "inline canwrap")
                story_line = story_line.findAll("p")[0].text
                info = soup.findAll('div', "txt-block")
                for node in info:
                  a = node.findAll('a')
                  for i in a:
                    if "country_of_origin" in i['href']:
                      mov_country = i.string
                for node in info:
                  a = node.findAll('a')
                  for i in a:
                    if "primary_language" in i['href']:
                      mov_language = i.string
                rating = soup.findAll('div',"ratingValue")
                for r in rating:
                  mov_rating = r.strong['title']

                bot.sendMessage(msg['chat']['id'], "*Title : *`{}`\n*Rating : *`{}`\n*Country : *`{}`\n*Language : *`{}`\n*IMDB Url : *[Click HERE!]({})\n*Story Line : *_{}_".format(mov_title, mov_rating, mov_country, mov_language, mov_link, story_line), 'Markdown', disable_web_page_preview=True, reply_to_message_id=msg['message_id'])
                return True

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

def equivalent(data, nt):
    if type(data) is dict:
        keys = list(data.keys())

        # number of dictionary keys == number of non-None values in namedtuple?
        if len(keys) != len([f for f in nt._fields if getattr(nt, f) is not None]):
            return False

        # map `from` to `from_`
        fields = list([k+'_' if k in ['from'] else k for k in keys])

        return all(map(equivalent, [data[k] for k in keys], [getattr(nt, f) for f in fields]))
    elif type(data) is list:
        return all(map(equivalent, data, nt))
    else:
        return data==nt
def examine(result, type):
    try:
        print('Examining %s ......' % type)

        nt = type(**result)
        assert equivalent(result, nt), 'Not equivalent:::::::::::::::\n%s\n::::::::::::::::\n%s' % (result, nt)

        pprint.pprint(result)
        pprint.pprint(nt)
        print()
    except AssertionError:
        traceback.print_exc()
        answer = input('Do you want to continue? [y] ')
        if answer != 'y':
            exit(1)
def pretty_size(size):
    units = ['B', 'KB', 'MB', 'GB']
    unit = 0
    while size >= 1024:
        size /= 1024
        unit += 1
    return '%0.2f %s' % (size, units[unit])
def pdf(msg):
    content_type, chat_type, chat_id, msg_date, msg_id = amanobot.glance(msg, long=True)
    if msg.get('text'):
        teclado = keyboard.restart_dl
        if msg['text'].startswith('!pdf'):
            input_str = msg['text'][4:]
            if input_str == '':
                bot.sendMessage(msg['chat']['id'], '*Use:* `!pdf <book name ²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²²/ title>`',
                                parse_mode='Markdown',
                                reply_to_message_id=msg['message_id'])
            else:
                app_name = input_str.split('/')[-1]
                sent = bot.sendMessage(msg['chat']['id'], "🔁 getting download link for {}".format(app_name), 'Markdown', reply_to_message_id=msg['message_id'])['message_id']
                if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
                    os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
                url = "https://libgen.pw"
                surl = "http://www.allitebooks.com"
                booknam = quote_plus(' '.join(input_str))
                query = surl+"/?s="+booknam
                print (query)
                r = urlrequest.Request(query,data=None,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
                html = urlrequest.urlopen(r)
                soup = bs4.BeautifulSoup(html, "lxml")
                for i in soup.find_all('article'):
                    div_title = i.find('h2').find('a')
                    bookid =  print(div_title['href'])
                    lins = surl + "/download/book/" + bookid
                    print (lins)
                    print (bookid)
                    time.sleep(512)
                    required_file_name = TEMP_DOWNLOAD_DIRECTORY + "" + bookid + ".pdf"
                    start = datetime.now()
                    chunk_size = 1024
                    headers = {'Accept-Language': 'en-US,en;q=0.9,te;q=0.8'}
                    r = requests.get(lins,  allow_redirects=True, stream=True, headers=headers)
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
                                upload_progress_string = "... [%s of %s]" % (str(dl), str(pretty_size(total_length)))
                    bot.editMessageText((msg['chat']['id'], sent), "⬆️ Uploading *{}* to Telegram".format(required_file_name), 'Markdown')
                    time.sleep(5)
                    starts = datetime.now()
                    if total_length < 52428800:
                        bot.sendChatAction(chat_id, 'upload_document')
                        tr = bot.sendDocument(chat_id, open(required_file_name, 'rb'), caption="@" + bot_username, parse_mode='Markdown')
                        examine(tr, amanobot.namedtuple.Message)
                        time.sleep(0.5)
                        ends = datetime.now()
                        mss = (ends - starts).seconds
                        os.remove(required_file_name)
                        bot.deleteMessage((msg['chat']['id'],sent))
                    else:
                        rst = InlineKeyboardMarkup(inline_keyboard=[[dict(text='❌ Recycle this message', callback_data='del_msgs')]])
                        bot.editMessageText((msg['chat']['id'], sent), "⚠️ *{}* is more than the 50MB limit. Unfortunately, The current download job has ended unexpectedly.\n Try downloading something smaller than this".format(app_name), 'Markdown', reply_markup=rst)
                        os.remove(required_file_name)
                        time.sleep(5)
                        bot.deleteMessage((msg['chat']['id'],sent))
                        return True
    elif msg.get('data'):
        if msg['data'] == 'del_msgs':
            os.remove(required_file_name)
            bot.deleteMessage((msg['from']['id'], msg['message']['message_id']))
