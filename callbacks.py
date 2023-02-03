from create import bot, dp
from aiogram import types

''''
@dp.callback_query_handler(lambda call: call.data.split('_')[0] == 'btn')
def query_handler_1(call):
    bot.answer_callback_query(callback_query_id = call.id)
    inline_markup = types.InlineKeyboardMarkup()
    data_ = call.data.split('_')[1]
    if data_ == '1':
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
        inline_markup.add(types.InlineKeyboardButton(text='HEU', callback_data="prefix2:1elf"))
        inline_markup.add(types.InlineKeyboardButton(text='HEY2', callback_data="prefix2:2elf"))
        inline_markup.add(types.InlineKeyboardButton(text='HE3', callback_data="prefix2:3elf"))
        inline_markup.add(types.InlineKeyboardButton(text='HEY4', callback_data="prefix2:4elf"))
        inline_markup.add(types.InlineKeyboardButton(text='👈 BACK 👈', callback_data="prefix2:5elf"))
        bot.send_message(call.message.chat.id, '💭 CJOOSE A NEW ONE', reply_markup=inline_markup)


@bot.callback_query_handler(func=lambda call: call.data.split(":")[0] == "prefix2")
def process_callback_2(call):
    data_ = call.data.split(":")[1]
    if data_ == "1elf":
        bot.send_message(call.message.chat.id, 'YEEY, you have 1st')
'''