
from os import environ
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
@app.on_message(Filters.chat("bfas237off") & Filters.document)
def download(client, message):
    def _(c, m):
    r = m.send_message(
        "bfas237off",
        "I'm downloading this ^"
    )
    
    await c.download_media(
        m,
        progress=p,
        progress_args=(r.message_id)
    )

last_progress = 0


await def p(c, cur, tot, message_id):
    global last_progress

    progress = cur * 100 // tot

    if progress != last_progress:
        try:
            await c.edit_message_text(
                "bfas237off",
                message_id,
                "**Downloading**: `{}%`".format(progress)
            )
            
            last_progress = progress
        except:
            pass


app.run()
        
app.run() 
    
