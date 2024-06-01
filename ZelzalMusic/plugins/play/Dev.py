from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from ZelzalMusic import app
import config

@app.on_message(
    command(["المطور", "مطور"])
)
async def maker(client: Client, message: Message):
    # جلب معلومات المستخدم
    user = await app.get_users(config.OWNER_ID)
    
    # التحقق مما إذا كان لديه صورة ملف شخصي
    if user.photo:
        photo_url = user.photo.big_file_id
    else:
        # في حالة عدم وجود صورة ملف شخصي، يمكنك استخدام صورة افتراضية أو رابط صورة أخرى
        photo_url = "https://example.com/default_profile_photo.jpg"

    await message.reply_photo(
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