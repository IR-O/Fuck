# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT, SUPPORT_CHANNEL

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://telegra.ph/file/40b93b46642124605e678.jpg",
    "https://telegra.ph/file/01a2e0cd1b9d03808c546.jpg",
    "https://telegra.ph/file/ed4385c26dcf6de70543f.jpg",
    "https://telegra.ph/file/33a8d97739a2a4f81ddde.jpg",
    "https://telegra.ph/file/cce9038f6a9b88eb409b5.jpg",
    "https://telegra.ph/file/262c86393730a609cdade.jpg",
    "https://telegra.ph/file/33a8d97739a2a4f81ddde.jpg",
]

HEY_IMG = "https://telegra.ph/file/33a8d97739a2a4f81ddde.jpg"

ALIVE_ANIMATION = [
    "https://telegra.ph//file/f9e2b9cdd9324fc39970a.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/c4c2759c5fc04cefd207a.mp4",
    "https://telegra.ph//file/b1fa6609b1c4807255927.mp4",
    "https://telegra.ph//file/f3c7147da6511fbe27c25.mp4",
    "https://telegra.ph//file/39071b73c02e3ff5945ca.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/6efdd8e28756bc2f6e53e.mp4",
]

FIRST_PART_TEXT = "✨ *ʜᴇʟʟᴏ* `{}`, ʜᴏᴡ ᴀʀᴇ ʏᴏᴜ . . ."

PM_START_TEXT = "ʜᴇʏ ᴛʜᴇʀᴇ [{}](tg://user?id={}) ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ !━━━━━━━━━━━━━━━━━━━━━━.\n๏ ɪ ᴀᴍ [˹ɪꝛσ ꭙ ᴍᴜꜱɪᴄ♡˼](https://t.me/Iro_x_music_bot) ᴀɴᴅ ɪ ʜᴀᴠᴇ sᴘᴇᴄɪᴀʟ ғᴇᴀᴛᴜʀᴇs.\n๏ ɪ ᴀᴍ ᴅɪғғᴇʀᴇɴᴛ ғʀᴏᴍ ᴀɴᴏᴛʜᴇʀ ʙᴏᴛs.\n\n๏ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʜᴇʟᴩ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴍʏ ᴍᴏᴅᴜʟᴇs ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅs.\n\n✨ᴘᴏᴡᴇʀᴇᴅ ʙʏ : [𝙄𝙍𝙊](https://t.me/iro_bot_support)✨."
START_BTN = [
    [
        InlineKeyboardButton(
            text="✨ᴋɪᴅɴᴀᴘ ᴍᴇ✨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{SUPPORT_CHANNEL}"),
    ],
    
    [
        InlineKeyboardButton(text="ᴄᴏᴍᴍᴀɴᴅs", callback_data="Main_help"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="✨ᴋɪᴅɴᴀᴘ ᴍᴇ✨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{SUPPORT_CHANNEL}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="ᴄʜᴀɴɴᴇʟ", url="https://t.me/iro_bot_support"),
        ib(text="ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/iro_x_support"),
    ],
    [
        ib(
            text="✨ᴋɪᴅɴᴀᴘ ᴍᴇ✨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *ɪꝛσ* 🫧

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
