import config
import requests
import dotenv
import os
import bs4 
import re


bot = config.bot
def imdb(msg):
    if msg.get('text'):
        if msg['text'].startswith('!imdb'):
            movie_name = msg['text'][6:]
            if msg['text'][6:] == '':
                res = '*Uso:* `!imdb <film title>` - _Otain film information from imdb db._'
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

                bot.sendMessage(msg['chat']['id'], "*Title : *`{}`\n*Rating : *`{}`\n*Country : *`{}`\n*Language : *`{}`\n*IMDB Url : *`{}`\n*Story Line : *{}".format(mov_title, mov_rating, mov_country, mov_language, mov_link, story_line), 'Markdown', disable_web_page_preview=True, reply_to_message_id=msg['message_id'])
                return True
