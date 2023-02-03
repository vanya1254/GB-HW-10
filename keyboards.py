from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from callbacks import *

kb_start = ReplyKeyboardMarkup(resize_keyboard=True)

btn_set = KeyboardButton('/set 100')
btn_rules = KeyboardButton('/rules')
btn_help = KeyboardButton('/help')

kb_start.add(btn_set, btn_help, btn_rules)



kb_inline_start = InlineKeyboardMarkup(row_width=1)

inline_help = InlineKeyboardButton(text='Админ', url='https://t.me/BiTHek')
inline_rules = InlineKeyboardButton(text='Зарубежный аналог россграм', url='https://www.instagram.com/jkdunkey/')

kb_inline_start.add(inline_help, inline_rules)