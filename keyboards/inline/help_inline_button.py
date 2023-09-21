from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


help_inline = InlineKeyboardMarkup(row_width=2)
one = InlineKeyboardButton('Да 👍', callback_data='yes')
two = InlineKeyboardButton('Нет 👎', callback_data='no')
help_inline.add(one, two)