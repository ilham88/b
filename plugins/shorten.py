import config
import requests
import urllib.request
from urllib.parse import urlparse, urlsplit
import http.client, sys, re
from os.path import splitext
bot = config.bot
import tldextract
from amanobot.namedtuple import InlineKeyboardMarkup
from amanobot.exception import TelegramError, NotEnoughRightsError
import keyboard
from tldextract import extract
def shorten(msg):
    if msg.get('text'):
        if msg['text'].startswith('!trim '):
            try:
                trim = ""
                text = msg['text'][6:]
                text = text.replace("http://","")
                text = text.replace("https://","")
                if not re.match(r'http(s?)\:', text):
                    url = 'http://' + text
                    parsed = urlsplit(url)
                    host = parsed.netloc
                    if host.startswith('www.'):
                        host = host[4:]
                    remove_spacec = url.split(' ')
                    final_namec = ''.join(remove_spacec)
                    r = requests.get('http://bsbe.cf/api?create&key=R9YqpUJtLu7djN3rkEFZna182cwIQlzbHxT&link={}'.format(final_namec))
                
                    
                    if r.status_code != 404:
                        b = r.json()
                        print(b)
                        Link = b["Link"]
                        ID = b["ID"]
                        Error = b["Error"]
                        u = requests.get('http://bsbe.cf/api?stats&key=R9YqpUJtLu7djN3rkEFZna182cwIQlzbHxT&id={}'.format(ID))
                        c = u.json()
                        print(c)
                        Clicks = c["Clicks"]
                        if b["Status"] != True:
                            req = "😭 Your Link encountered a Glitch"
                            inf = "" 
                            Status = b["Error"]
                            icon = "❌"
                        else:
                            req = "ℹ️ Link Details Below"
                            inf = "(Used for stats)"
                            Status = b["Status"]
                            icon = "✅"
                        extractedDomain = tldextract.extract(final_namec)
                        domainSuffix = extractedDomain.domain + '.' + extractedDomain.suffix
                        print(domainSuffix)    
                        dlb = InlineKeyboardMarkup(inline_keyboard=[[dict(text='↗️ Visit {}'.format(domainSuffix), url='{}'.format(Link))]])
                        bot.sendMessage(msg['chat']['id'], "\n\n*{}*\n\n*Trimmed Link:* {}\n\n*🆔:* `{}`\n\n*👀 Clicks:* {}\n\n*{} Link Status:* {}".format(req, Link, ID, Clicks, icon, Status), 
                            parse_mode='Markdown', reply_to_message_id=msg['message_id'], reply_markup=dlb)
            except IndexError:
                trim = "There was an error in your link"
                
            bot.sendMessage(msg['chat']['id'], trim, 'HTML',
                            reply_to_message_id=msg['message_id'],
                            disable_web_page_preview=True)


        elif msg['text'].startswith('/yghg '):
            text = msg['text'][6:]

            if text == '':
                bot.sendMessage(msg['chat']['id'], '*Uso:* /ytdl URL do vídeo ou nome', 'Markdown',
                                reply_to_message_id=msg['message_id'])
            else:
                sent_id = bot.sendMessage(msg['chat']['id'], 'Obtendo informações do vídeo...', 'Markdown',
                                          reply_to_message_id=msg['message_id'])['message_id']
                try:
                    if 'youtu.be' not in text and 'youtube.com' not in text:
                        url = search_yt(text)[0]['url']
                    else:
                        url = text
                    yt = ydl.extract_info(url, download=False)
                    for format in yt['formats']:
                        if format['format_id'] == '140':
                            fsize = format['filesize']
                    name = yt['title']
                    extname = yt['title']+'.m4a'
                except Exception as e:
                    return bot.editMessageText(
                        (msg['chat']['id'],sent_id),
                        text='Ocorreu um erro.\n\n'+str(e)
                    )
                if fsize < 52428800:
                    first = time.time()
                    if ' - ' in name:
                        performer, title = name.rsplit(' - ',1)
                    else:
                        performer = None
                        title = name
                    bot.editMessageText((msg['chat']['id'],sent_id),
                                        'Baixando <code>{}</code> do YouTube...\n({})'.format(name,pretty_size(fsize)), 'HTML')
                    ydl.extract_info(url, download=True)
                    bot.editMessageText((msg['chat']['id'],sent_id), 'Enviando áudio...')
                    bot.sendChatAction(msg['chat']['id'], 'upload_document')
                    sent = bot.sendAudio(msg['chat']['id'], open(ydl.prepare_filename(yt), 'rb'),
                        performer=performer,
                        title=title,
                        reply_to_message_id=msg['message_id']
                    )
                    os.remove(ydl.prepare_filename(yt))
                    bot.deleteMessage((msg['chat']['id'],sent_id))
                else:
                    bot.editMessageText((msg['chat']['id'],sent_id),
                                        'Ow, o arquivo resultante ({}) ultrapassa o meu limite de 50 MB'.format(pretty_size(fsize)))
