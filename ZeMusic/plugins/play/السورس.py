import asyncio
import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import app
from random import  choice, randint

def get_file_id(msg: Message):
    if msg.media:
        for message_type in (
            "photo",
            "animation",
            "audio",
            "document",
            "video",
            "video_note",
            "voice",
            # "contact",
            # "dice",
            # "poll",
            # "location",
            # "venue",
            "sticker",
        ):
            obj = getattr(msg, message_type)
            if obj:
                setattr(obj, "message_type", message_type)
                return obj

@app.on_message(
   command(["ميدو","المبرمج","المطور","مبرمج السورس"])
   
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5d5218d8cf4afd2c3e90c.jpg",
        caption=f"""**[𝗦𝗢𝗨𝗥𝗖𝗘 𝗠𝗲𝗗𝗼𝗢 - - ‍💻🖤](t.me/V_l_B2)**\n\n**{message.from_user.mention}\n•────‌‌‏──‌‌‏─‌‌‏─‌‌‏─‌‌‏─‌‌‏─‌‌‏─‌‌‏────‌‌‏──‌‌─‌‌‏─•
    ╔═══════ 𝕄𝔼𝔻𝕆𝕆 ═══════╗  

                𝗢𝗪𝗡𝗘𝗥 ➪ @V_l_B0                       

    ╚═══════ 𝕄𝔼𝔻𝕆𝕆 ═══════╝  
ٴ•────‌‌‏──‌‌‏─‌‌‏─‌‌‏─‌‌‏─‌‌‏─‌‌‏─‌‌‏─────‌‌‏──‌‌─•\nᥲ #ρᥱᖇ᥉᥆ꪀ Ꭵ᥉ #ժᥱ𝖋ᥱᥲƚᥱժ 𝖡ꪗ ƚᎻᥱ #ƚᎻᎥꪀᘜ᥉ Ꮋᥱ #ᥱꪎᥲᘜᘜᥱᖇᥲƚᥱ᥉ 𝐂𝐇 ⦂ J_GGC.t.me**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                   InlineKeyboardButton(
                        "𝕄𝔼𝔻𝕆𝕆", url=f"https://t.me/V_l_B0"), 
                ],[
                
                 ],

            ]

        ),

    )
    

@app.on_message(
    command(["سورس","السورس"])

)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/5d5218d8cf4afd2c3e90c.jpg",
        caption=f"""╭──── • ◈ • ────╮
么 [᥉᥆υᖇᥴᥱ 𝙼𝚎𝙳𝚘𝙾](t.me/V_l_B2)
么 [ժᥱ᥎ 𝙼𝚎𝙳𝚘𝙾](t.me/V_l_B0)
么 [ ᥉υρρ᥆ᖇƚ ](t.me/V_l_B2)
╰──── • ◈ • ────╯\n\n⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙶𝚁𝙾𝚄𝙿", url=f"https://t.me/V_l_B3"), 
                    InlineKeyboardButton(
                        "𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=f"https://t.me/V_l_B2"),
                  ],[
                    InlineKeyboardButton(
                        "𝙼𝚎𝙳𝚘𝙾", url=f"https://t.me/V_l_B0"),
                  ],[
                    InlineKeyboardButton(
                        ".💘اضف البوت اللي مجموعتك", url=f"https://t.me/{app.username}?startgroup=true"),
                ],

            ]

        ),

    )

