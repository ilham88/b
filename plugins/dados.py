import config
import requests
import re

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
bot = config.bot
bot_username = config.bot_username


def dados(msg):
    if msg.get('text'):
        if msg['text'].startswith('/dl') or msg['text'].startswith('!dl'):
            input_str = msg['text'][3:]
            if input_str == '':
                bot.sendMessage(msg['chat']['id'], '*Use:* `/dl or !dl <url/link>`',
                                parse_mode='Markdown',
                                reply_to_message_id=msg['message_id'])
            else:
                sent = bot.sendMessage(msg['chat']['id'], '*Processing your request..... 🔁*', 'Markdown', reply_to_message_id=msg['message_id'])[
                'message_id']
                start = datetime.now()
                url = input_str
                r = requests.get(url, allow_redirects=True)
                filename = get_filename_from_cd(r.headers.get('content-disposition'))
                f = open(filename, 'wb').write(r.content)
                j = f.json
                print(j)
                end = datetime.now()
                ms = (end - start).seconds
                bot.editMessageText((msg['chat']['id'], sent), "searched Google", 'Markdown', disable_web_page_preview=True)
                return True
