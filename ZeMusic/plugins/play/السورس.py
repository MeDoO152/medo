import asyncio
from pyrogram import enums
from pyrogram import types
import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","السورس"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5d5218d8cf4afd2c3e90c.jpg",
        caption=f"""**╭──── • ◈ • ────╮
么  𝙳𝙴𝚅  𝙼𝚎𝙳𝚘𝙾
么 َ ᥉υρρ᥆ᖇƚ 
么 [َ𝚂𝙾𝚞𝚁𝚂 (t.me/MeDoO15200)
╰──── • ◈ • ────╯
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "‹ ᯓ 𝙳𝙴𝚅 𝙼𝚎𝙳𝚘𝙾 𝅘𝅥𝅯 . 🕷 › ", url=f"https://t.me/MeDoO152"),
                ],[
                    InlineKeyboardButton(
                        "‹ ᯓ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𖠛›", url=f"https://t.me/MeDoO15200"), 
                    InlineKeyboardButton(
                        "‹ ᯓ 𝚂𝚞𝙿𝙿𝙾𝚁𝚃 𖠛›", url=f"https://t.me/MeDoO1520"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف البوت لمجموعتك ›", url=f"https://t.me/MeDoO152_bot?startgroup=true"),
            ]
        ]
         ),parse_mode=enums.ParseMode.MARKDOWN)
