from PIL import Image, ImageDraw, ImageFont
from uuid import uuid4
import config
import requests
import time
import sqlite3
import telegram
import telegram.ext
import html
import os

sticker_dump = os.environ["log"]
# Here dumps all the stickers
error_dump = os.environ["logs"]
# Here dumps all the errors

def draw(text):
    def border(draw, color, border, loc, text, font):
        for x in range(loc[0] - border, loc[0] + border + 1, 2):
            for y in range(loc[1] - border, loc[1] + border + 1, 2):
                draw.multiline_text((x, y), text, font=font, spacing=0, align="center", fill=color)
    font = ImageFont.truetype("font.otf", 72)
    image = Image.new('RGBA', (4096, 4096), (255, 255, 255, 0)); draw = ImageDraw.Draw(image)
    sz = draw.multiline_textsize(text, font=font, spacing=0)
    box = max(sz) + 40
    coord = (20, (box-sz[1]-40)// 2) if sz[0] > sz[1] else ((box-sz[0]-40)// 2, 20)
    border(draw, (255,255,255,255), 10, coord, text, font)
    draw.multiline_text(coord, text, font=font, spacing=0, align="center", fill=(0,0,0,255))
    image = image.crop((0, 0, box, box))
    fn = "%s.webp" % int(time.time())
    image.save(fn)
    return fn


def get_db(text):
    con = sqlite3.connect("data.sqlite")
    cur = con.cursor()
    d = cur.execute("select * from cache where text = ?", (text, )).fetchone()
    if d is None:
        return None
    return d[1]
    cur.close()


def set_db(text, val):
    if get_db(text) is None:
        con = sqlite3.connect("data.sqlite")
        cur = con.cursor()
        cur.execute("insert into cache (text, id) values (?, ?)", (text, val))
        cur.close()


def get_sticker_id(bot, text):
    db = get_db(text)
    if db:
        return db
    p = draw(text)
    m = bot.send_sticker(sticker_dump, open(p, 'rb'))
    os.remove(p)
    set_db(text, m.sticker.file_id)
    return m.sticker.file_id


def inlinequery(bot, update):
    query = update.inline_query.query
    fid = get_sticker_id(bot, query)
    results = [telegram.inlinequeryresultcachedsticker.InlineQueryResultCachedSticker(str(uuid4()), sticker_file_id=fid)]
    update.inline_query.answer(results)


def error(bot, update, error):
    print("update: %s\nerror: %s" % (update, error))
    bot.send_message(error_dump, 'Update <pre>%s</pre> caused error <pre>%s</pre>' % (html.escape(str(update)), html.escape(str(error))), parse_mode="HTML")


def main():
    u = telegram.ext.Updater(os.environ.get("TOKEN"))  # Here goes bot token
    d = u.dispatcher
    d.add_handler(telegram.ext.InlineQueryHandler(inlinequery))
    d.add_error_handler(error)
    u.start_polling()
    u.idle()

main()
