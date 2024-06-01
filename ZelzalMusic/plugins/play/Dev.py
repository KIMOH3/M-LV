from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from ZelzalMusic import app
import config
import io

@app.on_message(
    command(["المطور","مطور"])
)
async def maker(client: Client, message: Message):
    user = await app.get_users(config.OWNER_ID)
    photos = await app.get_profile_photos(user.id, limit=1)
    if photos.total_count > 0:
        photo = photos.photos[0][-1]  # اختيار أحدث صورة
        await app.send_photo(
            chat_id=message.chat.id,
            photo=photo.file_id,
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
    else:
        # في حالة عدم وجود صورة ملف شخصي، يمكنك استخدام صورة افتراضية أو رابط صورة أخرى
        await app.send_message(message.chat.id, text="لا يوجد صورة ملف شخصي.")
