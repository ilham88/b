def dados(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('Chat:', content_type, chat_type, chat_id)
 
    if content_type != 'text':
        return
 
    command = msg['text'][-1:].lower()
 
    if command == 'c':
        markup = ReplyKeyboardMarkup(keyboard=[
                     ['Plain text', KeyboardButton(text='Text only')],
                     [dict(text='Phone', request_contact=True), KeyboardButton(text='Location', request_location=True)],
                 ])
        bot.sendMessage(chat_id, 'Custom keyboard with various buttons', reply_markup=markup)
    elif command == 'i':
        markup = InlineKeyboardMarkup(inline_keyboard=[
                     [dict(text='Telegram URL', url='https://core.telegram.org/')],
                     [InlineKeyboardButton(text='Callback - show notification', callback_data='notification')],
                     [dict(text='Callback - show alert', callback_data='alert')],
                     [InlineKeyboardButton(text='Callback - edit message', callback_data='edit')],
                     [dict(text='Switch to using bot inline', switch_inline_query='initial query')],
                 ])
 
        global message_with_inline_keyboard
        message_with_inline_keyboard = bot.sendMessage(chat_id, 'Inline keyboard with various buttons', reply_markup=markup)
    elif command == 'h':
        markup = ReplyKeyboardHide()
        bot.sendMessage(chat_id, 'Hide custom keyboard', reply_markup=markup)
    elif command == 'f':
