import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["مطور","ميدو","المبرمج","المطور"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5d5218d8cf4afd2c3e90c.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[𝗦𝗢𝗨𝗥𝗖𝗘 𝗠𝗲𝗗𝗼𝗢](https://t.me/,MeDoO15200)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @MeDoO152 ❫
◉ 𝙸𝙳      : ❪ `860340899` ❫
◉ 𝙱𝙸𝙾    : ❪ 𝗦𝗢𝗨𝗥𝗖𝗘 𝗠𝗲𝗗𝗼𝗢 (https://t.me/MeDoO15200) ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒𝗦𝗢𝗨𝗥𝗖𝗘 𝗠𝗲𝗗𝗼𝗢", url=f"https://t.me/MeDoO15200"), 
                 ],[
                   InlineKeyboardButton(
                        "𝗦𝗢𝗨𝗥𝗖𝗘 𝗠𝗲𝗗𝗼𝗢 ", url=f"https://t.me/MeDoO15200"),
                ],

            ]

        ),

    )
