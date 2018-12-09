"""This is the Welcome Bot in @PyrogramChat.

It uses the Emoji module to easily add emojis in your text messages and Filters
to make it only work for specific messages in a specific chat.
"""

from pyrogram import Client, Emoji, Filters

MENTION = "[{}](tg://user?id={})"
MESSAGE = "{} Welcome to [Pyrogram](https://docs.pyrogram.ml/)'s group chat {}!"


    
@app.on_message(Filters.text & Filters.chat("Bfas237group"))
async def move(client, message):
    if "Oft" in message.text:
        await client.send_message("bfas237off", "`{}` wrote:\n{}\n\n**⬇️ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛɪɴᴜᴇ ʜᴇʀᴇ ⬇️**".format(message.reply_to_message.from_user.first_name, message.reply_to_message.text))
        await client.send_message("Bfas237group", "I moved this discussion to the [Offtopic Group ↗️](https://t.me/bfas237off/{})".format(message.reply_to_message.message_id, message.reply_to_message.text), reply_to_message_id=message.reply_to_message.message_id)
        await client.delete_messages(
    "Bfas237group",
    message_ids=message.message_id
)

@app.on_message(Filters.text & Filters.chat("bfas237off"))
async def move(client, message):
    if "Ont" in message.text:
        await client.send_message("Bfas237group", "`{}` wrote:\n{}\n\n**⬇️ ᴘʟᴇᴀsᴇ ᴄᴏɴᴛɪɴᴜᴇ ʜᴇʀᴇ ⬇️**".format(message.reply_to_message.from_user.first_name, message.reply_to_message.text))
        await client.send_message("bfas237off", "This happens to be an [OnTopic Discussion ↗️](https://t.me/Bfas237group/{})".format(message.reply_to_message.message_id, message.reply_to_message.text), reply_to_message_id=message.reply_to_message.message_id)
        await client.delete_messages(
    "bfas237off",
    message_ids=message.message_id
)

@app.on_message(Filters.private & Filters.document)
async def _(c, m):
    await r = c.send_message(
        "bfas237off",
        "I'm downloading this ^",
        reply_to_message_id=message.reply_to_message.message_id
    )
    
    await c.download_media(
        m,
        progress=p,
        progress_args=(r.message_id,)
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


app.run()  # Automatically start() and idle()
