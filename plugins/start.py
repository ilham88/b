import config
import keyboard

bot = config.bot
version = config.version
bot_username = config.bot_username


def start(msg):
    if msg.get('text'):
        if msg['chat']['type'] == 'private':
            teclado = keyboard.start_pv
            smsg = 'Hello! I am a multipurpose bot that can do many stuffs and even manage your groups and keep it clean from spam. \n\n Use the keyboard below to learn how to use me'
        else:
            teclado = keyboard.start
            smsg = 'Hello there! to know more about me, start me in private and understand how i work.'
        if msg['text'].split()[0] == '/start' or msg['text'] == '!start' or msg['text'].split()[0] == '/start@' + bot_username:
            bot.sendMessage(msg['chat']['id'], smsg,
                            reply_to_message_id=msg['message_id'], reply_markup=teclado)
            return True


    elif msg.get('data'):

        if msg['data'] == 'tools_cmds':
            bot.editMessageText(
                (msg['message']['chat']['id'], msg['message']['message_id']),
                text='''*Tools:*

/climate - information Displays climate.
/coub - Search of small animations.
/echo - Repeats the text informed.
/gif - Search GIFs.
/git - Send information of a user from GitHub.
/html - Repeats the text informed by using HTML.
/ip - Display information about an IP/domain.
/jsondump - Sends the json of the message.
/mark - Repeats the text reported using Markdown.
/print - Sends a print of a web site.
/pypi - Search modules in PyPI.
/r - Research topics on Reddit
/request - Makes a request to a web site.
/shorten - Shortens a URL.
/token - Displays information for a token bot.
/tr - Translates a text.
/yt - Search YouTube videos.
/ytdl - download the audio from a video on YouTube.''',
                parse_mode='Markdown',
                reply_markup=keyboard.cmds_back
            )


        elif msg['data'] == 'admin_cmds':
            bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                '''*Admin Commands:*

/ban - Bans a user.
/config - Sends a settings menu.
/defregras - Defines the rules of the group.
/kick - Kicks a user.
/mute - Restricts a user.
/pin - Fixed a message in the group.
/title - Sets the title of the group.
/unban - Desbane a user.
/unmute - Desrestringe a user.
/unpin - Desfixa the message set in the group.
/unwarn - Remove the warnings from the user.
/warn - Warns a user.
/welcome - Sets the message of welcome.''',
                                parse_mode='Markdown',
                                reply_markup=keyboard.cmds_back)


        elif msg['data'] == 'user_cmds':
            bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                '''*Commands for normal users:*

/add - Sends a suggestion to the AI of the bot.
/admins - Shows the list of admins of the chat.
/data - Sends a random number from 1 to 6.
/bug - Reports a bug to my developer.
/id - Displays your information or a user.
/ping - Replies with a ping message.
/rules - Displays the rules of the group.
/roulette - To play Russian Roulette.''',
                                parse_mode='Markdown',
                                reply_markup=keyboard.cmds_back)


        elif msg['data'] == 'start_back':
            if msg['message']['chat']['type'] == 'private':
                teclado = keyboard.start_pv
            else:
                teclado = keyboard.start
            bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                "Hi, I'm a multipurpose bot, to find out more about my functions click on the buttons below:",
                                reply_markup=teclado)

 
        elif msg['data'] == 'all_cmds':
            bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                'Select a command category to view. \n\n If you need help with the bot or have any suggestions from the @Bfas237botdevs',
                                reply_markup=keyboard.all_cmds)


        elif msg['data'] == 'infos':
            bot.editMessageText((msg['message']['chat']['id'], msg['message']['message_id']),
                                '''• ByatsgzeRobot

Version: {}
Maintainers: <a href="https://github.com/AmanoTeam">Amano Team</>
Translators: <a href="1.1.1.1">Bfaschat</>

Partnerships:
 » <a href="https://t.me/bfas237botdevs">Bfas237 Bot devs</>

©2018 - <a href="https://#">B™</>'''.format(version),
                                parse_mode='html',
                                reply_markup=keyboard.start_back,
                                disable_web_page_preview=True)
