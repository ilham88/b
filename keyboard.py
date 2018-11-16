from amanobot.namedtuple import InlineKeyboardMarkup
import config

start = InlineKeyboardMarkup(inline_keyboard=[
    [dict(text='🤖 Start a conversation', url='https://t.me/{}?start=start'.format(config.bot_username))]
])

start_pv = InlineKeyboardMarkup(inline_keyboard=[
    [dict(text='📚 Commands', callback_data='all_cmds')] +
    [dict(text='ℹ️ About Bot', callback_data='infos')],
    [dict(text='➕ Add to your group', url='https://t.me/{}?startgroup=new'.format(config.bot_username))] +
    [dict(text='⭐ Rate', url='https://t.me/storebot?start=' + config.bot_username)]
])

all_cmds = InlineKeyboardMarkup(inline_keyboard=[
    [dict(text='👮 Admins', callback_data='admin_cmds')] +
    [dict(text='👤 Users', callback_data='user_cmds')],
    [dict(text='🔧 Ultra Tools', callback_data='tools_cmds')] +
    [dict(text='🔎 inline Mode', switch_inline_query_current_chat='/')],
    [dict(text='« Go Back', callback_data='start_back')]
])

start_back = InlineKeyboardMarkup(inline_keyboard=[
    [dict(text='« Go Back', callback_data='start_back')]
])

cmds_back = InlineKeyboardMarkup(inline_keyboard=[
    [dict(text='« Go Back', callback_data='all_cmds')]
])

del_msg = InlineKeyboardMarkup(inline_keyboard=[
    [dict(text='🗑 Delete All messages', callback_data='del_msg')]
])

ia_question = InlineKeyboardMarkup(inline_keyboard=[
    [dict(text='✅ Accept', callback_data='ia_yes')] +
    [dict(text='❌ Cancel', callback_data='ia_no')]
])
