from aiogram import types
from loader import dp, bot, db
from keyboards.inline.help_inline_button import help_inline


@dp.message_handler(lambda message: message.text.startswith('/'))
async def save_command(message: types.Message):
    await bot.send_message(chat_id=-4043269193, text=f"{message.message_id}\n"
                                                     f"{message.chat.id}\n"
                                                     f"Вопрос = {message.text}")


@dp.message_handler(lambda message: message.reply_to_message and "Вопрос = /" in message.reply_to_message.text)
async def handle_reply_to_saved_command(message: types.Message):

    lines = message.reply_to_message.text.split('\n')
    message_id = int(lines[0])
    chat_id = int(lines[1])
    response_text = f"Ответ - {message.text}"
    additional_text = f"Вам помог ответ?"

    await message.delete()
    await message.reply_to_message.delete()
    await message.answer(f"{message.from_user.full_name} - ответил ✅")
    await bot.send_message(chat_id=chat_id, text=response_text, reply_to_message_id=message_id)
    await bot.send_message(chat_id=chat_id, text=additional_text, reply_markup=help_inline, reply_to_message_id=message_id)