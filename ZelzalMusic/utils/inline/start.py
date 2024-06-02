from pyrogram.types import InlineKeyboardButton

import config
from ZelzalMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="صلي على النبي وتبسم ♥️✨", callback_data="welcome_message")
        ],
        [
            InlineKeyboardButton(text="𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫", user_id=config.OWNER_ID),
        ],
        [
            InlineKeyboardButton(text=_["ZTHON_BUTTON"], url="https://t.me/OOOJ30"),
            InlineKeyboardButton(text=_["ZTHON_BUTTON2"], url="https://t.me/M2RR1"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_1"], url="https://t.me/{app.username}?startgroup=true"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(text="Developer", user_id=config.OWNER_ID),
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="zzzback")],
        [
            InlineKeyboardButton(text=_["ZTHON_BUTTON"], url="https://t.me/OOOJ30"),
            InlineKeyboardButton(text=_["ZTHON_BUTTON2"], url="https://t.me/M2RR1"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_1"], url="https://t.me/{app.username}?startgroup=true"),
        ],
    ]
    return buttons