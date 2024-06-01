#lord


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from ZelzalMusic import app
import config


@app.on_message(
    command(["المطور", "مطور"])
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo="https://telegra.ph/file/dbacb042fe3d9276c687e.jpg",
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
