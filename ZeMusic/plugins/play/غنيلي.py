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



@app.on_message(command(["غنيلي", "‹ غنيلي ›", "غ", ""]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/proxMusicl/{rl}"
    await client.send_voice(message.chat.id,url,caption="↯ : تم اختيار اغنية عشوائيه لك 🤍",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/MeDoO15200")
                ],
            ]
        )
    )


@app.on_message(command(["صوره", "🕷", "‹ صور ›", "صور"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,50)
    url = f"https://t.me/vnnkli/{rl}"
    await client.send_photo(message.chat.id,url,caption="↯ : تم اختيار صوره اليك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/MeDoO15200")
                ],
            ]
        )
    )


@app.on_message(command(["‹ انمي ›", "انمي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/LoreBots7/{rl}"
    await client.send_photo(message.chat.id,url,caption="↯ : تم اختيار انمي اليك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/MeDoO15200")
                ],
            ]
        )
    )


@app.on_message(command(["‹ متحركه ›", "متحركه"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/GifWaTaN/{rl}"
    await client.send_animation(message.chat.id,url,caption="↯ : تم اختيار المتحركه اليك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/MeDoO15200")
                ],
            ]
        )
    )

@app.on_message(command(["‹ اقتباسات ›", "اقتباس"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/LoreBots9/{rl}"
    await client.send_photo(message.chat.id,url,caption="↯ : تم اختيار اقتباس اليك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/MeDoO15200")
                ],
            ]
        )
    )

@app.on_message(command(["هيدرا", "‹ هيدرات ›"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/flflfldld/{rl}"
    await client.send_photo(message.chat.id,url,caption="↯ : تم اختيار هيدرات اليك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/MeDoO15200")
                ],
            ]
        )
    )

@app.on_message(command(["صور", " ‹ صور ›"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/vvyuol/{rl}"
    await client.send_photo(message.chat.id,url,caption="↯ : تم اختيار صوره اليك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/MeDoO15200")
                ],
            ]
        )
    )

@app.on_message(command(["داعش", "افتار شباب"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(2,90)
    url = f"https://t.me/mlscc_dhsb/{rl}"
    await client.send_photo(message.chat.id,url,caption="↯ : تم اختيار الذبح اليك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/MeDoO15200")
                ],
            ]
        )
    )

@app.on_message(command(["‹ قران ›", "قران"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(1,90)
    url = f"https://t.me/lllIIlIllIlIIlI/{rl}"
    await client.send_voice(message.chat.id,url,caption="↯ : تم اختيار ايـه قرآنيه اليك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/MeDoO15200")
                ],
            ]
        )
    )

@app.on_message(command(["الشيخ", "النقشبندي", "نقشبندي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(1,90)
    url = f"https://t.me/ggcnjj/{rl}"
    await client.send_voice(message.chat.id,url,caption="🥹♥ ¦ تـم اختيـار الشيخ نقشبندي اليك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/MeDoO15200")
                ],
            ]
        )
    )

@app.on_message(command(["فيلم", "‹ فيلم ›"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(1,50)
    url = f"https://t.me/gyigkk/{rl}"
    await client.send_audio(message.chat.id,url,caption="↯ : تم اختيار فيلم اليك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/MeDoO15200")
                ],
            ]
        )
    )

@app.on_message(command(["استوري", "‹ ستوريات ›"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(1,50)
    url = f"https://t.me/yoipopl/{rl}"
    await client.send_audio(message.chat.id,url,caption="↯ : تم اختيار استوري اليك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/MeDoO15200")
                ],
            ]
        )
    )
  
@Client.on_message(filters.command(["صور انمي", "صورة انمي", "صوره انمي", "انمي"], ""))
async def sssora(client, message):
  if not message.chat.type == enums.ChatType.PRIVATE:
    await joinch(message)
  if len(lisetanme) == 0:
     user = await get_userbot(client.me.username)
     async for msg in user.get_chat_history("LoreBots7"):
      if msg.media:
        lisetanme.append(msg)
  phot = random.choice(lisetanme)
  photo = f"https://t.me/LoreBots7/{phot.id}"
  await message.reply_photo(photo=photo, caption="**♪ 𝑱𝒐𝒊𝒏 ➧ @MeDoO152  💎 .**")
