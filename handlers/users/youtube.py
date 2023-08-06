import datetime
from pytube import YouTube
from aiogram import executor, types
from loader import bot, dp

from keyboards.default.plotforms import platform


@dp.message_handler(text='YouTube')
async def choose(msg: types.message):
    await msg.answer('Please Send YouTube Video Link...', reply_markup=platform)


async def cmd_answer(message: types.Message):
    if message.text.startswith('https://youtube.be/') or message.text.startswith(
            'https://www.youtube.com/') or message.text.startswith('https://youtube.com/shorts/'):
        await message.answer("Download...")
        url = message.text
        yt = YouTube(url)
        title = yt.title
        author = yt.author
        channel = yt.channel_url
        resolution = yt.streams.get_highest_resolution().resolution
        length = yt.length
        views = yt.views
        picture = yt.thumbnail_url
        keyboard = types.InlineKeyboardMarkup()
        keyboard.add(types.InlineKeyboardButton(text="Download a video", callback_data="download"))
        await message.answer_photo(f'{picture}', caption=f"📹 <b>{title}</b> <a href='{url}'>→</a> \n"  # Title#
                                                         f"👤 <b>{author}</b> <a href='{channel}'>→</a> \n"  # Author Of Channel# 
                                                         f"⚙️ <b>Expand —</b> <code>{resolution}</code> \n"  #
                                                         f"⏳ <b>Trivality—</b> <code>{str(datetime.timedelta(seconds=length))}</code> \n"  # Length#
                                                         f"👁 <b> Look back—</b> <code>{views:,}</code> \n",
                                   parse_mode='HTML', reply_markup=keyboard)  # Views#


@dp.callback_query_handler(text="download")
async def button_download(call: types.CallbackQuery):
    url = call.message.html_text
    yt = YouTube(url)
    title = yt.title
    author = yt.author
    resolution = yt.streams.get_highest_resolution().resolution
    stream = yt.streams.filter(progressive=True, file_extension="mp4")
    stream.get_highest_resolution().download(f'{call.message.chat.id}', f'{call.message.chat.id}_{yt.author}')
    with open(f"{call.message.chat.id}/{call.message.chat.id}_{yt.author}", 'rb') as video:
        await bot.send_video(call.message.chat.id, video, caption=f"📹 <b>{title}</b> \n"  # Title#
                                                                  f"👤 <b>{author}</b> \n\n"  # Author Of Channel#
                                                                  f"⚙️ <b>Expand—</b> <code>{resolution}</code> \n"
                                                                  f"📥 <b>Helped by @full_video_save_bot</b>",
                             parse_mode='HTML')

if __name__ == "__main__":
    executor.start_polling(dp)
