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

def get_filename_from_cd(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]
def progress_callback_simple(downloaded,total):
    sys.stdout.write(
        "\r" +
        (len(str(total))-len(str(downloaded)))*" " + str(downloaded) + "/%d"%total +
        " [%3.2f%%]"%(100.0*float(downloaded)/float(total))
    )
    sys.stdout.flush()

def download(srcurl, dstfilepath, progress_callback=None, block_size=8192):
    def _download_helper(response, out_file, file_size):
        if progress_callback!=None: progress_callback(0,file_size)
        if block_size == None:
            buffer = response.read()
            out_file.write(buffer)

            if progress_callback!=None: progress_callback(file_size,file_size)
        else:
            file_size_dl = 0
            while True:
                buffer = response.read(block_size)
                if not buffer: break

                file_size_dl += len(buffer)
                out_file.write(buffer)

                if progress_callback!=None: progress_callback(file_size_dl,file_size)
               
    with open(dstfilepath,"wb") as out_file:
        if python3:
            with urllib.request.urlopen(srcurl) as response:
                file_size = int(response.getheader("Content-Length"))
                _download_helper(response,out_file,file_size)
        else:
            response = urllib2.urlopen(srcurl)
            meta = response.info()
            file_size = int(meta.getheaders("Content-Length")[0])
            _download_helper(response,out_file,file_size)

import traceback
try:
def dados(msg):
    if msg.get('text'):
        if msg['text'].startswith('/dl') or msg['text'].startswith('!dl'):
            input_str = msg['text'][3:]
            if input_str == '':
                bot.sendMessage(msg['chat']['id'], '*Use:* `/dl or !dl <url/link>`',
                                parse_mode='Markdown',
                                reply_to_message_id=msg['message_id'])
            else:
                sent = bot.sendMessage(msg['chat']['id'], "searched Google........", 'Markdown', reply_to_message_id=msg['message_id'])['message_id']
                url = input_str
                filename = url.split('/')[-1]
                with open(filename,"wb") as out_file:
                    with urllib.request.urlopen(url) as response:
                    file_size = int(response.getheader("Content-Length"))
                    _download_helper(response,out_file,file_size)
                    file = download(url, filename, progress_callback_simple)
                    bot.sendChatAction(msg['chat']['id'], 'upload_document')
                    bot.sendDocument(msg['chat']['id'], file, reply_to_message_id=msg['message_id'])
                    bot.editMessageText((msg['chat']['id'], sent), "searched Google", 'Markdown', disable_web_page_preview=True)
                    return True    
except:
    traceback.print_exc()
    input()
    
