import config
import urllib
import dotenv
from dotenv import load_dotenv
# OR, the same with increased verbosity:
load_dotenv(verbose=True)
import os
bot = config.bot
papi = 'abdf158215d05e1a973510c5c81d9a2cdd99ad2c7cd8'

def prints(msg):
    if msg.get('text'):
        if msg['text'].startswith('/print ') or msg['text'].startswith('!print '):
            try:
                bot.sendPhoto(msg['chat']['id'], f"https://api.thumbnail.ws/api/{papi}/thumbnail/get?url={urllib.parse.quote_plus(msg['text'][7:])}&width=1280",
                              reply_to_message_id=msg['message_id'])
            except Exception as e:
                bot.sendMessage(msg['chat']['id'], f'Ocorreu um erro ao enviar a print, favor tente mais tarde.\nDescrição do erro: {e.description}',
                                reply_to_message_id=msg['message_id'])
            return True
