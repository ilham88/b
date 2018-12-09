# init project
from flask import Flask, jsonify, render_template, request
from os import environ
application = Flask(__name__)


# I've started you off with Flask, 
# but feel free to use whatever libs or frameworks you'd like through `.requirements.txt`.

# unlike express, static files are automatic: http://flask.pocoo.org/docs/0.12/quickstart/#static-files

# http://flask.pocoo.org/docs/0.12/quickstart/#routing
# http://flask.pocoo.org/docs/0.12/quickstart/#rendering-templates
@application.route('/')
def hello():
    return render_template('index.html')


from pyrogram import Client, Filters
app = Client(environ['TOKEN'])



@app.on_message(Filters.text & Filters.chat("Bfas237group"))
def move(client, message):
  if "Oft" in message.text:
      client.send_message("bfas237off", "[{}](tg://user?id={}) **wrote:**\n{}\n\n**⬇️ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛɪɴᴜᴇ ʜᴇʀᴇ ⬇️**".format(message.reply_to_message.from_user.first_name, message.reply_to_message.from_user.id, message.reply_to_message.text))
      message.reply("I moved this discussion to the [Offtopic Group ↗️](https://t.me/bfas237off/{})".format(message.reply_to_message.message_id, message.reply_to_message.text), reply_to_message_id=message.reply_to_message.message_id, quote=True)
      client.delete_messages(
    "Bfas237group",
    message_ids=message.message_id
)
      client.delete_messages(
    "bfas237off",
    message_ids=message.reply_to_message.message_id
)
@app.on_message(Filters.text & Filters.chat("bfas237off"))
def move(client, message):
    if "Ont" in message.text:
        client.send_message("Bfas237group", "[{}](tg://user?id={}) **wrote:**\n{}\n\n**⬇️ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛɪɴᴜᴇ ʜᴇʀᴇ ⬇️**".format(message.reply_to_message.from_user.first_name, message.reply_to_message.from_user.id, message.reply_to_message.text))
        message.reply("The Main group has been created for this discussion so why not join [Offtopic Group ↗️](https://t.me/bfas237off/{})".format(message.reply_to_message.message_id, message.reply_to_message.text), reply_to_message_id=message.reply_to_message.message_id, quote=True)
        client.delete_messages(
    "bfas237off",
    message_ids=message.message_id
)
        client.delete_messages(
    "Bfas237group",
    message_ids=message.reply_to_message.message_id
)
 # Automatically start() and idle()
@app.on_message(Filters.private & Filters.document)
def _(c, m):
    r = c.send_message(
        "bfas237off",
        "I'm downloading this ^",
        reply_to_message_id=message.reply_to_message.message_id
    )
    
    c.download_media(
        m,
        progress=p,
        progress_args=(r.message_id,)
    )

last_progress = 0


def p(c, cur, tot, message_id):
    global last_progress

    progress = cur * 100 // tot

    if progress != last_progress:
        try:
            c.edit_message_text(
                "bfas237off",
                message_id,
                "**Downloading**: `{}%`".format(progress)
            )
            
            last_progress = progress
        except:
            pass
# Simple in-memory store
dreams = [
  'Find and count some sheep',
  'Climb a really tall mountain',
  'Wash the dishes',
]

@application.route('/dreams', methods=['GET'])
def get_dreams():
    return jsonify(dreams)

# could also use the POST body instead of query string: http://flask.pocoo.org/docs/0.12/quickstart/#the-request-object
@application.route('/dreams', methods=['POST'])
def add_dream():
    dreams.append(request.args.get('dream'))
    return ''
  
  
# listen for requests :)
if __name__ == "__main__":
    app.run() 
    from os import environ
    application.run(host='0.0.0.0', port=int(environ['PORT']))
