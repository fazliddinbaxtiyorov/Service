from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp

from loader import dp
# from keyboards.default.plotforms import platform


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"👋 Hello {message.from_user.full_name}, I'm YouTube Assistant. \n 📥 You will be "
                         f"able to download videos from "
                         f"YouTube, TikTok And Instagram.\n🔗Choose And Send video link.")
