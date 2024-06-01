from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from ZelzalMusic import app
import config

@app.on_message(
    command(["المطور", "مطور"])
)
async def maker(client: Client, message: Message):
    user = await app.get_users(config.OWNER_ID)
    photo_url = "https://telegra.ph/file/dbacb042fe3d9276c687e.jpg"

    name_caption = f"اسم: {user.first_name}"
    bio_caption = f"النبذة: {user.bio}"

    await app.send_photo(
        chat_id=message.chat.id,
        photo=photo_url,
        caption=f"{name_caption}\n{bio_caption}",
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
