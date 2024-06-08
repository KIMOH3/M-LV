import asyncio
import random
from pyrogram import enums, types
from pyrogram.types import (Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, ChatPrivileges)
from pyrogram import filters, Client
from ZelzalMusic import app
import config  # تأكد من استيراد config بشكل صحيح

bot_name = {}

name = "لورد"

@app.on_message(filters.regex("تعيين اسم البوت") & filters.private & filters.user(config.OWNER_ID), group=7113)
async def set_bot_name(client, message):
    global name
    try:
        # رسالة توضيحية للتأكد من أن الفلتر يعمل
        await message.reply_text("تم التعرف على الأمر. الآن سيتم طلب الاسم الجديد.")
        
        ask = await app.ask(message.chat.id, "ارسل الاسم الجديد", timeout=300)
        name = ask.text
        await message.reply_text("تم تعيين الاسم بنجاح")
    except Exception as e:
        await message.reply_text(f"حدث خطأ: {str(e)}")

caesar_responses = [
    "اسمي {name} يصحبي 💘 ⋅",
    "يسطا قولتلك اسمي {name} ☺️",
    "ايه يا زميلي 😂♥️ ،",
    "قلب البوت 🥹💘 ⋅",
    "ثانية بشقط واحدة تانية 😂💘 ،",
    "يعم والله بحبك بس ناديلي بـ {name} 🙂",
    "ايه يا معلم مين مزعلك",
    "ايوه جاي 😂♥️ ،",
    "تًبا لك ماذا تريد من امي 🙂",
    "يسطا هوا عشان بحبك تصدعني؟",
    "تعرف بالله هحبك أكتر لو ناديتلي {name} 🥹💘",
    "اي ي معلم مين مزعلك؟",
    "متصلي على النبي كدا💘 ⋅",
    "مش فاضيلك نصايه وكلمني ☺ .",
    "انجز عايزني أشقطلك مين؟",
    "شكلها منكدا عليك وجاي تطلعهم علينا 😂♥ ,",
]

@app.on_message(filters.command(["بوت", "البوت"], ""), group=71135)
async def caesar_bot(client, message):
    global name
    bot_username = (await app.get_me()).username
    bar = random.choice(caesar_responses).format(name=name)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("خدني لجروبك 🫣♥", url=f"https://t.me/{bot_username}?startgroup=True")]
    ])
    
    await message.reply_text(
        text=f"**[{bar}](https://t.me/{bot_username}?startgroup=True)**",
        disable_web_page_preview=True,
        reply_markup=keyboard,
        parse_mode=enums.ParseMode.MARKDOWN
    )

# تأكد من أن config.py يحتوي على معرف المستخدم الخاص بك
# owner_id = 123456789  # استبدل هذا الرقم بمعرف المستخدم الخاص بك
