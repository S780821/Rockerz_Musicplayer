import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from modules.config import BOT_USERNAME
START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f7a3acc8e6e0e85f56150.jpg",
        caption=f"""**
⛦➪ Ꮋᴇʟʟᴏ Ꮖ ᴀᴍ  Տᴜᴘᴇʀ ҒᴀՏᴛ  ᎷᴜՏɪᴄ Ꮲʟᴀʏᴇʀ Ꮯʀᴇᴀᴛᴇᴅ Ᏼʏ [Oғғɪᴄɪᴀʟ ᴀғᴋ xD](https://t.me/log_afk)
⛦➪ Ᏼᴏᴛ Ғᴏʀ Ͳᴇʟᴇɢʀᴀᴍ ᏀʀᴏᴜᴘՏ...""",
   reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ᗩᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ Ꮐʀᴏᴜᴘ ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📨 Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/Blaze_Support"
                    ),
                    InlineKeyboardButton(
                        "ՄᴘᴅᴀᴛᴇՏ 📨", url=f"https://t.me/The_Blaze_Network"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🎇 Ꮯʜᴀᴛ Ꮓᴏɴᴇ 🎇", url=f"https://t.me/UNIQUE_SOCIETY")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "sᴀʟɪᴍ"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴊᴏɪɴ ʜᴇʀᴇ ᴀɴᴅ sᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/BLAZE_SUPPORT")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["repo", "#repo", "@repo", "/repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴄʟɪᴄᴋ ᴍᴇ ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ 💞", url=f"https://t.me/UNIQUE_SOCIETY")
                ]
            ]
        ),
    )
