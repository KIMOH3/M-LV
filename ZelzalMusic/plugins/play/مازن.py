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
    command(["مازن","مستر مازن","ميزو"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/8623792f8becc9362160b.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪ • ᯓ𓆩˹ 𝐃𝐞𝐯ᬽ | 𝐌𝐚𝐳𝐞𝐧 ˼𓆪𓆃‌❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @M_LR1 ❫
◉ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 : ❪ eirux.t.me ❫
◉ 𝙱𝙸𝙾    : ❪ My Bro »〔 @M_R_C2 & @D_R_X_7 〕
⛥ My Channel »〔 eirux.t.me & eirthon.t.me 〕⛥ My group »〔 @mr_eirux 〕⛥ My trust »〔 mz_xf.t.me 〕❫""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "• ᯓ𓆩˹ 𝐃𝐞𝐯ᬽ | 𝐌𝐚𝐳𝐞𝐧 ˼𓆪𓆃", url=f"https://t.me/M_LR1"),
            ]
        ]
         ),
     )
  
