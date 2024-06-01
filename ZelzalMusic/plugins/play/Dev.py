from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from ZelzalMusic import app
import config
import io
import requests

@app.on_message(
    command(["المطور", "مطور"])
)
async def maker(client: Client, message: Message):
    user = await app.get_users(config.OWNER_ID)
    
    if user.photo:
        # استخدام رابط الصورة المباشرة من ملف الشخصي
        photo_url = user.photo.big_file_id
    else:
        photo_url = "https://telegra.ph/file/dbacb042fe3d9276c687e.jpg"

    await app.send_photo(
        chat_id=message.chat.id,
        photo=photo_url,
        caption="~ 𝐃𝐞𝐯 𝐁𝐨𝐓",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𓆩👨‍💻︙مطور الـبـوت 𓆪", url=f"tg://openmessage?user_id={config.OWNER_ID}"
                    ),
                ],
            ]
        ),
    )
