from pyrogram import Client, filters
from pyrogram.types import Message
from ZelzalMusic import app 

@app.on_message(filters.command("واتساب"))
async def generate_whatsapp_link(client, message: Message):
    if len(message.command) < 2:
        await message.reply("ابعت رقمك مع رمز الدوله زي كدا +1234567890")
        return

    phone_number = message.command[1]

    whatsapp_link = f"https://wa.me/{phone_number}"

    await message.reply(f"لينك شاتك واتساب يقلبي {phone_number}:\n{whatsapp_link}")
