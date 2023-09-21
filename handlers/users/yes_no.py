from aiogram import types
from loader import dp, bot


@dp.callback_query_handler(text='yes')
async def positive_answer(call: types.CallbackQuery):
    print(call)
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Мы рады, что вам это помогло! 🚀')


@dp.callback_query_handler(text='no')
async def negative_answer(call: types.CallbackQuery):
    await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Попробуйте задать еще раз, но по-другому 💭')