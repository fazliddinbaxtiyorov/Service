from aiogram import executor, types
import aiohttp
import re

from keyboards.default.plotforms import platform
from loader import bot, dp


@dp.message_handler(text='TikTok')
async def choose(msg: types.message):
    await msg.answer('Please Send TikTok Video Link...', reply_markup=platform)


@dp.message_handler()
async def download(url):
    async with aiohttp.ClientSession() as session:
        request_url = f'https://api.douyin.wtf/api?url={url}'
        async with session.get(request_url) as response:
            data = await response.json()
            video = data['video_data']['nwm_video_url_HQ']
            return video


# Download videos


@dp.message_handler()
async def process(message: types.Message):
    if re.compile('https://[a-zA-Z]+.tiktok.com/').match(message.text):
        wait = await message.reply('Download...')
        video = await download(message.text)
        await bot.delete_message(message.chat.id, wait['message_id'])
        await message.answer_video(video, caption=f'Done!', reply_markup=platform)


if __name__ == "__main__":
    executor.start_polling(dp)
