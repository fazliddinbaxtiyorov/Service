from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    await message.answer("If you have problems \n✉️ Write we: @moonblack7, @am1rov_008")
