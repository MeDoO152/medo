import asyncio
from pyrogram import Client, filters
from strings.filters import command
from ZeMusic.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)



###############الاوامر الموجوده هنااا############

#كيبورد الاعضاء



REPLY_MESSAGE = "**صلي علي اشرف خلق الله 🥹✨**"

REPLY_MESSAGE_BUTTONS = [
    [
        ("سورس"),
        ("مبرمج السورس")
    ],
    [
        ("تلاوات. 📖")
    ],
    [
        ("النقشبندي"),
        ("قران")
    ],
    [
        ("استوريهات. 🥹")
    ],
    [
        ("اقتباسات"),
        ("هيدرات")
    ],
    [
        ("شعر. 🗣")
    ],
    [
        ("صوره"),
        ("انمي")
    ],
    [
        ("متحركه. 🎬")
    ],
    [
        ("افتار بنات"),
        ("افتار شباب")
    ],
    [
        ("لعيبه. ⛹")
    ],
    [
        ("نكته"),
        ("كتبات")
    ],
    [
        ("اذكار. 💎")
    ],
    [
        ("حساب العمر"),
        ("ابراج")
    ],
    [
        ("تويت. 😂")
        
    ],
    [
        ("لو خيروك"),
        ("انصحني")
    ],
    [
        ("الالعاب. 🐰")
    ],
    [
        ("احكام"),
        ("كلمه")
    ],
    [
        ("يـوتيوب. 📽")
        
    ],
    [
        ("احرف"),
        ("العكس") 
    ],
    [
        ("الاوامر")
        
    ],
    [
        ("سوال"),
        ("صراحه")             
        
    ],
    [
        ("اخفاء الازرار . 🕷")
    ]
]


@app.on_message(filters.regex("^/medo"))
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("^اخفاء الازرار . 🕷$"))
async def down(client, message):
          m = await message.reply(" **- تم اخفاء الازرار بنجاح . 🐰\n\n- لاظهار كيب الارشادات /ARN   \n. 🕷**\n\n- لاظهار كيب الاعضاء والتسليه  /medo  \n. 🕷**", reply_markup= ReplyKeyboardRemove(selective=True))



@app.on_message(filters.regex("يـوتيوب. 📽"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://telegra.ph/file/5d5218d8cf4afd2c3e90c.jpg",
        caption=f"""**يتم استخدام هذا الامر لعرض تحميل من اليوتيوب**\n**استخدم الامر بهذا الشكل** `تنزيل` ** او ** `يوتيوب` ** كمثل تنزيل سوره الرحمن اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𝚂𝙾𝚄𝚁𝙲 𝙴𝙼𝚎𝙳𝚘𝙾", url=f"https://t.me/MeDoO15200"),
            ]
         ]
     )
  )

