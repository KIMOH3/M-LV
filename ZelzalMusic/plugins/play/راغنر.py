import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZelzalMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZelzalMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["راغنار","راغنر"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/74e9cfc6183d2f8a81e1d.jpg",
        caption=f"""𝅄 𓏺 𝖭𝖺𝗆𝖾 : › ，ᖇ ᥲ ᘜ ꪀ ᥲ ᖇ 𓏺¹𖥻
𝅄 𓏺 𝖴𝗌𝖾𝗋 : › @l_k_l_I
𝅄 𓏺 𝖲𝗈𝗎𝗋𝖼𝖾 : › @OOOJ30
𝅄 𓏺 𝖡𝗂𝗈 : › ᶠᵒʳ⤸ꪔᥱ➤【 @IR_A_G 】【 @S_S_U_Z 】【 @MR_1X0 】ƒᥙᥴƙ ᥆ƒƒ""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫 𝐑𝐚𝐠𝐧𝐚𝐫", url=f"https://t.me/l_k_l_I"),
            ]
        ]
         ),
     )
  
