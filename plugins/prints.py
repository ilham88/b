import config
import urllib
import dotenv
import os
bot = config.bot

def prints(msg):
    if msg.get('text'):
        if msg['text'].startswith('/print ') or msg['text'].startswith('!print '):
            try:
            	apiurl = 'https://api.thumbnail.ws/api'
    			papi = 'abdf158215d05e1a973510c5c81d9a2cdd99ad2c7cd8'
                bot.sendPhoto(msg['chat']['id'], f"{apiurl}/{papi}/thumbnail/get?url={urllib.parse.quote_plus(msg['text'][7:])}&width=1280",
                              reply_to_message_id=msg['message_id'])
            except Exception as e:
                bot.sendMessage(msg['chat']['id'], f'Ocorreu um erro ao enviar a print, favor tente mais tarde.\nDescrição do erro: {e.description}',
                                reply_to_message_id=msg['message_id'])
            return True
