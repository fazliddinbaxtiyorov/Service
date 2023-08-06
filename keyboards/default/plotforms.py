from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

platform = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='YouTube'), KeyboardButton(text='TikTok')],
    ], resize_keyboard=True)

