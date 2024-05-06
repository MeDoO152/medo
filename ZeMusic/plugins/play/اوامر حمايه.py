import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, CallbackQuery, InlineKeyboardMarkup, Message
from typing import Union
from pyrogram.types import InlineKeyboardButton
from ZeMusic import app
from ZeMusic.misc import HAPP, SUDOERS, XCB
from config import OWNER_ID







@app.on_message(command(["اوامر", "الاوامر"]))
async def zdatsr(client: Client, message: Message):
    usr = await client.get_users(OWNER_ID)
    name = usr.first_name
    usrnam = usr.username
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5d5218d8cf4afd2c3e90c.jpg",
        caption=f"""مرحبا بك عزيزي في اوامر بوت الميوزك 🎸 ⋅\n- اسمك : {message.from_user.mention} 💘 ⋅\n- عليك استخدام الازرار بالاسفل لتصفح اوامر الميوزك 🎸 ⋅ \n\n• ⌯ 𝐃𝐄𝐕.𝐒𝐎𝐔𝐑𝐂𝐄.𝑴𝒆𝑫𝒐𝑶 ⌯ • </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• اوامــر التشغيــل •", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "• اوامـر القنـاة •", callback_data="zzzch"),
                    InlineKeyboardButton(
                        "• اوامـر الادمـن •", callback_data="zzzad"),
                ],[
                    InlineKeyboardButton(
                        "• اوامــر المطــور •", callback_data="zzzdv"),
                ],[
                    InlineKeyboardButton(
                        "•𓌹⦓𝗦𝗢𝗨𝗥𝗖𝗘 𝗠𝗲𝗗𝗼𝗢⦔𓌺 •", url="https://t.me/MeDoO15200"),
                ],
            ]
        ),
    )
