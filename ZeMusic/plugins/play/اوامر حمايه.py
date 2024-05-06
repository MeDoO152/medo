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
        caption=f"""⌔︙اوامــر البــوت الرئيسيـة \n—————————————\n⌔︙اختر ماتريد عرضه من القائمه :\n\nقناه السورس :𝗦𝗢𝗨𝗥𝗖𝗘 𝗠𝗲𝗗𝗼𝗢
—————————————""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامر الحمايه ①", callback_data="medo1"),
                    InlineKeyboardButton(
                        "اوامر الادمنيه ②", callback_data="medo2"),
                ],[
                    InlineKeyboardButton(
                        "اوامر المدراء ③", callback_data="medo3"),
                    InlineKeyboardButton(
                        "اوامر المنشئين ④", callback_data="medo4"),
                ],[
                    InlineKeyboardButton(
                        "اوامـر المالكيـن ⑤", callback_data="medo5"),
                    InlineKeyboardButton(
                        "اوامر التحشيش ⑥", callback_data="medo6"),
                ],[
                    InlineKeyboardButton(
                        "اوامــر التسليـه ⑦", callback_data="medo7"),
                    InlineKeyboardButton(
                        "اوامــر البنـــك ⑧", callback_data="medo8"),
                ],[
                    InlineKeyboardButton(
                        "اوامـر المطـور", callback_data="medo9"),
                    InlineKeyboardButton(
                        "اوامـر التـشغيل", callback_data="medo10"),
                ],[
                    InlineKeyboardButton(
                        "الالـعــاب", callback_data="medo11"),
                ],[
                    InlineKeyboardButton(
                        "القفل / الفتح", callback_data="zzzdv"),
                    InlineKeyboardButton(
                        "التفعيل/ التعطيل", callback_data="zzzdv"),
                ],[
                    InlineKeyboardButton(
                        "𝗦𝗢𝗨𝗥𝗖𝗘 𝗠𝗲𝗗𝗼𝗢", url="https://t.me/V_l_B2"),
                ],
            ]
        ),
    )



@app.on_callback_query(filters.regex("zzzback"))
async def zzzback(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""⌔︙اوامــر البــوت الرئيسيـة \n—————————————\n⌔︙اختر ماتريد عرضه من القائمه :\n\nقناه السورس :𝗦𝗢𝗨𝗥𝗖𝗘 𝗠𝗲𝗗𝗼𝗢
—————————————""",
       reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامر الحمايه ①", callback_data="medo1"),
                    InlineKeyboardButton(
                        "اوامر الادمنيه ②", callback_data="medo2"),
                ],[
                    InlineKeyboardButton(
                        "اوامر المدراء ③", callback_data="medo3"),
                    InlineKeyboardButton(
                        "اوامر المنشئين ④", callback_data="medo4"),
                ],[
                    InlineKeyboardButton(
                        "اوامـر المالكيـن ⑤", callback_data="medo5"),
                    InlineKeyboardButton(
                        "اوامر التحشيش ⑥", callback_data="medo6"),
                ],[
                    InlineKeyboardButton(
                        "اوامــر التسليـه ⑦", callback_data="medo7"),
                    InlineKeyboardButton(
                        "اوامــر البنـــك ⑧", callback_data="medo8"),
                ],[
                    InlineKeyboardButton(
                        "اوامـر المطـور", callback_data="medo9"),
                    InlineKeyboardButton(
                        "اوامـر التـشغيل", callback_data="medo10"),
                ],[
                    InlineKeyboardButton(
                        "الالـعــاب", callback_data="medo11"),
                ],[
                    InlineKeyboardButton(
                        "القفل / الفتح", callback_data="medo12"),
                    InlineKeyboardButton(
                        "التفعيل/ التعطيل", callback_data="zzzdv"),
                ],[
                    InlineKeyboardButton(
                        "𝗦𝗢𝗨𝗥𝗖𝗘 𝗠𝗲𝗗𝗼𝗢", url="https://t.me/V_l_B2"),
                ],
            ]
        ),
    )



@app.on_callback_query(filters.regex("medo7") & SUDOERS)
async def mpdtsf(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""<b>↯︙مرحباً بك عزيزي المطور </b>\n\n<b>↯︙استخدم الازرار بالاسفل\n↯︙ل تصفح اوامر الميوزك</b>""",
       reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامر التسليه 1⃣", callback_data="tsluaoih"),
                    InlineKeyboardButton(
                        "اوامر التسليه 2⃣", callback_data="tsluaefgh"),
                ],[
                    InlineKeyboardButton(
                        "القائمه الرئيسيه ⏺", callback_data="zzzback"),
                ],
            ]
        ),
    )



@app.on_callback_query(filters.regex("medo12"))
async def zzzll(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
<b>⚙️U+2069 ❬ م1 ❭ اوامر حماية المجموعه ⇊<b>
<b>═══════『♡』═══════ٴ<b>
<b>🔐 ╖ قفل «» فتح + الامر<b>
U+2066<b>♻️U+2069 ╜ قفل «» فتح ❬ الكـــل ❭<b>
<b>═══════『♡』═══════ٴ<b>
<b>📮╖ الدردشه<b>
<b>📜╢ المعرفات<b>
<b>📸╢ الصور<b>
<b>📽️╢ الفيديوهات<b>
<b>🎟╢ الاستيكر<b>
<b>📂╢ الملفات<b>
<b>🎥╢ المتحركه<b>
<b>⏏️╢ الرفع<b>
<b>🔊╢ الريكورد<b>
<b>🎧╢ الصوت<b>
<b>📞╢ الجهات<b>
<b>🔊╢ الترحيب<b>
<b>🚫╢ المغادره<b>
<b>🎧╢ الاغاني<b>
<b>🏨╢ الزخرفه<b>
<b>🍿╢ الافلام<b>
<b>🎬╢ اليوتيوب<b>
<b>💱╢ الترجمه<b>
<b>🔄╢ الردود<b>
<b>🚿╢ التوجيه<b>
<b>🗳️╢ الاشعارات<b>
<b>💳╢ التاج<b>
<b>🧾╢ رابط الحذف<b>
<b>🔈╢ اطردني<b>
<b>🤔╢ مين ضافني<b>
<b>🏓╢ الالعاب<b>
<b>🎁╢ الروايات<b>
<b>🎆╢ الابراج<b>
<b>🔍╢ معاني الاسماء<b>
<b>💬╜ الترحيب<b>
<b>═══════『♡』═══════ٴ<b>
<b>⚠️ ❬ بالكتم, بالطرد ❭<b>
<b>═══════『♡』═══════ٴ<b>
<b>🌐╖ الروابط<b>
<b>🔄╢ التوجيه<b>
<b>🍿╢ الفشار<b>
<b>⚜️╢ البوتات<b>
<b>⚠️╜ الممنوعه<b>
<b>═══════『♡』═══════ٴ<b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "القائمه الرئيسيه ⏺", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("tsluaoih"))
async def zzzad(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""<b>🥳╖ ❬ م7 ❭ 1⃣ اوامر التسليه ⇊<b>
🔐╜ رفع «» تنزيل + الامر
═══════『♡』═══════ٴ
🐣╖ متوحد «» متوحده
💬╢ تاج للمتوحدين
📎╜ مسح المتوحدين
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
💢╖ بقره<b>
💬╢ تاج للبقرات<b>
📎╜ مسح البقرات<b>
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🐒╖ غبي<b>
💬╢ تاج للاغبيه
📎╜ مسح الاغبيه
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🤪╖ حمار
💬╢ تاج للحمير
📎╜ مسح الحمير
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🐕╖ كلب
💬╢ تاج للكلاب
📎╜ مسح الكلاب
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🐰╖ قرد
💬╢ تاج للقرود
📎╜ مسح القرود
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🤡╖ فرسه<b>
💬╢ تاج للفرسات
📎╜ مسح الفرسات
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🤰╖ عره
💬╢ تاج للعرر
📎╜ مسح العرر
<b>•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
👰╖ زوجتي
💬╢ تاج للزوجات
📎╜ مسح المتزوجات
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
👩‍❤️‍👨╖ زواج «» طلاق
💬╢ تاج للمتزوجين
📎╜ مسح المتزوجين
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
💘╖ رفع بقلبي «» تنزيل من قلبي
💬╢ تاج للي بقلبي
📎╜ مسح من قلبي
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
🙊╖ بيستي
💬╢ تاج للبيست
📎╜ مسح البيستيه
•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ
""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "القائمه الرئيسيه ⏺", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("tsluaefgh"))
async def zzzch(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""<b>🥳╖ ❬ م7 ❭ 2⃣ اوامر التسليه ⇊<b>
<b>🔐╜ رفع «» تنزيل + الامر <b>
<b>═══════『♡』═══════ٴ<b>
<b>🐣╖ وتكه<b>
<b>💬╢ تاج للوتكات<b>
<b>📎╜ مسح الوتكات<b>
<b>•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ<b>
<b>💢╖ رقاصه<b>
<b>💬╢ تاج للرقاصات<b>
<b>📎╜ مسح الرقاصات<b>
<b>•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ<b>
<b>🐒╖ مهزء<b>
<b>💬╢ تاج للمهزئين<b>
<b>📎╜ مسح المهزئين<b>
<b>•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ<b>
<b>🤪╖ حيوان<b>
<b>💬╢ تاج للحيوانات<b>
<b>📎╜ الحيوانات<b> 
<b>•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ<b>
<b>🐕╖ فاشل<b>
<b>💬╢ تاج للفشله<b>
<b>📎╜ مسح الفشله<b>
<b>•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ<b>
<b>🐰╖ دكري<b>
<b>💬╢ تاج للدكور<b>
<b>📎╜ مسح الدكور<b>
<b>•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ<b>
<b>🤡╖ قطتي<b>
<b>💬╢ تاج للقطط<b>
<b>📎╜ مسح القطط<b>
<b>•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ<b>
<b>🤰╖ ابني<b>
<b>💬╢ تاج للابناء<b>
<b>📎╜ مسح الابناء<b>
<b>•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ<b>
<b>👰╖ بنتي<b>
<b>💬╢ تاج للبنوتات<b>
<b>📎╜ مسح البنوتات<b>
<b>•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ<b>
<b>👩‍❤️‍👨╖ حبيبي<b>
<b>💬╢ تاج للحبايب<b>
<b>📎╜ مسح الحبايب<b>
<b>•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ<b>
<b>💘╖ زوجي<b>
<b>💬╢ تاج للازواج<b>
<b>📎╜ مسح الازواج<b>
<b>•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ<b>
<b>🙊╖ زوجتي<b>
<b>💬╢ تاج للزوجات<b>
<b>📎╜ مسح الزوجات<b>
<b>•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ<b>
<b>👰╖ خاين<b>
<b>💬╢ تاج للخونه<b>
<b>📎╜ مسح الخونه<b>
<b>•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ<b>
<b>👩‍❤️‍👨╖ خاينه<b>
<b>💬╢ تاج للخاينين<b>
<b>📎╜ مسح الخاينين<b>
<b>•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ<b>
<b>💘╖ عبيط<b>
<b>💬╢ تاج للعبط<b>
<b>📎╜ مسح العبط<b>
<b>•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·ٴ<b>
<b>🙊╖ متخزوق<b> 
<b>💬╢ تاج للمتخزوقين<b>
<b>📎╜ مسح المتخزوقين<b>
<b>•·•·•·•·•·•·•·•·•·••·•·•·••·•·•··•·•·••·•··••·•·•·<b>
""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "القائمه الرئيسيه ⏺", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("medo9") & SUDOERS)
async def zzzup(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
<b>💎╖ ❬ اوامر المطورين ⇊ ❭<b>
<b>👮‍♂️╜ « المطور » ⇊<b>
<b>═══════『♡』═══════ٴ<b>
<b>🤴╖ رفع «» تنزيل ❬ مالك ❭<b>
<b>🔂╢ تغيير رابط الجروب<b>
<b>🔊╢ اذاعه بالمجموعات<b>
<b>👨‍🏭╢ اذاعه بالتوجيه للمجموعات<b>
<b>🤹‍♀╢ اذاعه موجهه بالتثبيت<b>
<b>☀️╢ اذاعه خاص<b>
<b>💘╢ اذاعه بالتوجيه خاص<b>
<b>🎙️╢ اذاعه بالتثبيت<b>
<b>📶╢ جلب نسخه احتياطيه<b>
<b>🏋‍♂╢ رفع نسخه احتياطيه<b>
<b>🍃╢ الاحصائيات<b>
<b>🚷╢ حذف المالكين<b>
<b>📚╜ ❬ + ❭ جميع ماسبق<b>
<b>═══════『♡』═══════ٴ<b>
<b>💎 « المطور الاساسي » ⇊<b>
<b>═══════『♡』═══════ٴ<b>
<b>📑╖ اضف «» حذف رد عام<b>
<b>🤴╢ رفع «» تنزيل ❬ مميز عام ❭<b>
<b>💎╢ مسح المميزين عام<b>
<b>🗃️╢ الردود العامه<b>
<b>🧨╢ حذف الردود العامه<b>
<b>🛠╢ اذاعه بالتوجيه خاص<b>
<b>🍃╢ اذاعه بالتوجيه للمجموعات<b>
<b>🎯╢ اذاعه بالتثبيت<b>
<b>☀️╢ اذاعه موجهه بالتثبيت<b>
<b>🧲╢ جلب «» رفع ❬نسخه احتياطيه❭<b>
<b>⏳╢ الاحصائيات<b>
<b>🤴╢ رفع «» تنزيل ❬ مطور ❭<b>
<b>🤖╢ المطورين «» حذف المطورين<b>
<b>🔗╢ ضع اسم للبوت<b>
<b>📝╢ تغيير رساله المغادره<b>
<b>🚫╢ حظر «» كتم  ❬ عام ❭<b>
<b>🥺╢ المكتومين  عام<b> 
<b>💔╢ المحظورين عام<b>
<b>♻️╢ الغاء العام<b>
<b>📚╜ ❬ + ❭ جميع ماسبق<b>
<b>═══════『♡』═══════ٴ<b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "القائمه الرئيسيه ⏺", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("medo10") & SUDOERS)
async def zzzsu(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
<b>⩹━⛥━𝗦𝗢𝗨𝗥𝗖𝗘 𝗠𝗲𝗗𝗼𝗢━★━⩺<b>

  <b>╭۪ᰲ╍ׂ╌ׂ╍۪ᰲ╌ᰲ┄ׅ╍╌ᰲ┄ׅ╍╌ᰲ┄ׅ╍╌ᰲ┄ׅׅ╍╌ᰲ┄ׅׅ╍╌ׅ╮<b>
  <b>   🎧 :  اوامر تشغيل البوت في الجروب<b>
  <b>╰۫᷼╍ׅ╌ׅ╍۫᷼╌᷼┄۫╍╌᷼┄۫╍╌᷼┄۫╍╌᷼┄۫╍╌ᰲ┄ׅׅ╍╌۫╯<b>

<b>═══════『♡』═══════ٴ<b>
<b>▶️╖ تشغيل «» ريبلاي علي اغنيه<b>
<b>🎶╢ تشغيل + اسم الاغنيه<b>
<b>📹╢ فيديو + اسم الفديو<b>
<b>⏹╢ ايقاف<b>
<b>⏯️╢ تخطي<b>
<b>👷‍♂️╢ الحساب المساعد<b>
<b>🔢╜ قائمه التشغيل<b>
<b>═══════『♡』═══════ٴ<b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "القائمه الرئيسيه ⏺", callback_data="zzzdv"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzbn") & SUDOERS)
async def zzzbn(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
↯︙<b>قائمة اوامر المطور :</b>
– – – – – – – – – – – – – – – – – –
<b>- قائمة اوامر الحظر :</b>
– – – – – – – – – – – – – – – – – –
بلوك/الغاء بلوك/المبلكين
<b>- ل حظر/الغاء حظر شخص من استخدام ميوزك البوت</b>
– – – – – – – – – – – – – – – – – –
احظره عام/الغاء حظره عام
<b>- ل حظر/الغاء حظر شخص من استخدام ميوزك البوت عام</b>
– – – – – – – – – – – – – – – – – –
المحظورين عام
<b>- ل جلب قائمة المحظورين عام في البوت</b>
– – – – – – – – – – – – – – – – – –
حظر مجموعة/سماح
<b>- ل حظر/الغاء حظر مجموعة من استخدام ميوزك البوت</b>
– – – – – – – – – – – – – – – – – –
المجموعات المحظورة
<b>- ل جلب قائمة بالمجموعات المحظورة من استخدام البوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "القائمه الرئيسيه ⏺", callback_data="zzzdv"),
               ],
          ]
        ),
    )


@app.on_callback_query(filters.regex("zzzas") & SUDOERS)
async def zzzas(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
↯︙<b>قائمة اوامر المطور :</b>
– – – – – – – – – – – – – – – – – –
<b>↯︙قائمة اوامر المساعد :</b>
– – – – – – – – – – – – – – – – – –
السجل ⦗ تفعيل / تعطيل ⦘
<b>- ل تفعيل/تعطيل اشعارات مجموعة سجل البوت</b>
– – – – – – – – – – – – – – – – – –
⦗ المغادره التلقائيه ⦗ تفعيل / تعطيل
<b>- ل تفعيل/تعطيل المغادره التلقائيه ل الحساب المساعد من المجموعات عند عدم استخدام الميوزك</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "القائمه الرئيسيه ⏺", callback_data="zzzdv"),
               ],
          ]
        ),
   )


@app.on_callback_query(filters.regex("zzyius") & SUDOERS)
async def zzzas(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
⩹━⛥━𝗦𝗢𝗨𝗥𝗖𝗘 𝗠𝗲𝗗𝗼𝗢━★━⩺
       
اوامر القفل و الفتح للحمايه:

╮ ⇐الصور
│──────────────────
│⇐  الروابط
│──────────────────
│⇐  السب
│──────────────────
│⇐  التوجيه
│──────────────────
│⇐  الفيديو
│──────────────────
│⇐  التثبيت 
│──────────────────
│⇐  الكل
│──────────────────
│⇐  الملصقات
│──────────────────
│⇐  الايدي
│──────────────────
│⇐  جمالي
│──────────────────
│⇐  الحظر
│──────────────────
│⇐  الكتم
│──────────────────
│⇐ البايو
│──────────────────
│⇐ الدعوه
│──────────────────
│⇐ المتحركات
│──────────────────
│⇐ الاباحي
│──────────────────
╯ ⇐ التقيد
⩹━⛥━𝗦𝗢𝗨𝗥𝗖𝗘 𝗠𝗲𝗗𝗼𝗢━★━⩺

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "القائمه الرئيسيه ⏺", callback_data="zzzdv"),
               ],
          ]
        ),
   )


@app.on_callback_query(filters.regex("zyiusse") & SUDOERS)
async def zzzas(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
اوامر الحمايه 

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "القائمه الرئيسيه ⏺", callback_data="zzzdv"),
               ],
          ]
        ),
   )


@app.on_callback_query(filters.regex("medo11") & SUDOERS)
async def zzzbn(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
💎 الالعاب الخاصه بالسورس
•━━━━━━━『♡』━━━━━━━•ٴ
⚙️╖ لفتح الالعاب او قفلها ارسل ⇊
🔰╜ قفل الالعاب ࿗ فتح الالعاب
•━━━━━━━『♡』━━━━━━━•ٴ
🎱╖ لعبه XO ࿗ ❬اكس او❭
😎╢ لعبة الصراحه ࿗ ❬صراحه❭
💃╢ لعبة مريم ࿗ ❬مريم❭
🥺╢ لعبة عقاب ࿗ ❬عقاب❭
💥╢ جمالى % ࿗ ❬نسبه جمالي❭
❤️╢ نسبه الحب ࿗ ❬نسبه الحب❭
👺╢ الكذب ࿗ ❬كشف الكذب❭
🐜╢ لعبه النمله الجامده ࿗ ❬نمله❭
🦗╢ الصرصار الجامد ࿗ ❬صرصار❭
🐷╢ الخنزير الجامد ࿗ ❬خنزير❭
🏀╢ كره السله ࿗ ❬كره السله❭
🎯╢ لعبة النشال ࿗ ❬النشال❭
🎲╢ لعبة النرد او الزهر ࿗ ❬النرد❭
💎╢ كت تويت ࿗ ❬تويت❭
👀╢ كت تويت ࿗ ❬تويت بالصور❭
🤹‍♂️╢ اسرع شخص ࿗ ❬الاسرع❭
🏤╢ لعبة المطابقه ࿗  ❬التشابه❭
U+2066🏜U+2069╢ لعبة الذكاء ࿗ ❬المختلف❭
🎰╢ لعبة الارقام ࿗ ❬الرياضيات❭
🌐╢ لعبة ترجمه ࿗ ❬الانجليزي❭
🎎╢ لعبة تصحيح ࿗  ❬الامثله❭
U+2066♻️U+2069╢ لعبة عكس ࿗ الكلمات ❬العكس❭
🤔╢ لعبة التفكير ࿗  ❬الفزوره❭
🎬╜ اللعبه الشهيره ࿗  ❬المعاني❭
•━━━━━━━『♡』━━━━━━━•ٴ

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "القائمه الرئيسيه ⏺", callback_data="zzzback"),
               ],
          ]
        ),
    )


@app.on_callback_query(filters.regex("zzzsu") & SUDOERS)
async def zzzsu(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
↯︙<b>قائمة اوامر المطور :</b>
– – – – – – – – – – – – – – – – – –
<b>- قائمة اوامر الرفع :</b>
– – – – – – – – – – – – – – – – – –
رفع مطور/تنزيل مطور
<b>- ل رفع/تنزيل شخص مطور في ميوزك البوت</b>
– – – – – – – – – – – – – – – – – –
المطورين
<b>- ل عرض قائمة مطورين البوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "القائمه الرئيسيه ⏺", callback_data="zzzdv"),
               ],
          ]
        ),
    )
    
    
@app.on_callback_query(filters.regex("zzzsu") & SUDOERS)
async def zzzsu(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
↯︙<b>قائمة اوامر المطور :</b>
– – – – – – – – – – – – – – – – – –
<b>- قائمة اوامر الرفع :</b>
– – – – – – – – – – – – – – – – – –
رفع مطور/تنزيل مطور
<b>- ل رفع/تنزيل شخص مطور في ميوزك البوت</b>
– – – – – – – – – – – – – – – – – –
المطورين
<b>- ل عرض قائمة مطورين البوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "القائمه الرئيسيه ⏺", callback_data="zzzdv"),
               ],
          ]
        ),
    )
    
    
@app.on_callback_query(filters.regex("zzzjosu") & SUDOERS)
async def zzzsu(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
↯︙<b>قائمة اوامر المطور :</b>
– – – – – – – – – – – – – – – – – –
<b>- قائمة اوامر الرفع :</b>
– – – – – – – – – – – – – – – – – –
رفع مطور/تنزيل مطور
<b>- ل رفع/تنزيل شخص مطور في ميوزك البوت</b>
– – – – – – – – – – – – – – – – – –
المطورين
<b>- ل عرض قائمة مطورين البوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "القائمه الرئيسيه ⏺", callback_data="zzzdv"),
               ],
          ]
        ),
    )
    
    
@app.on_callback_query(filters.regex("zzzsu") & SUDOERS)
async def zzzsu(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
↯︙<b>قائمة اوامر المطور :</b>
– – – – – – – – – – – – – – – – – –
<b>- قائمة اوامر الرفع :</b>
– – – – – – – – – – – – – – – – – –
رفع مطور/تنزيل مطور
<b>- ل رفع/تنزيل شخص مطور في ميوزك البوت</b>
– – – – – – – – – – – – – – – – – –
المطورين
<b>- ل عرض قائمة مطورين البوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "القائمه الرئيسيه ⏺", callback_data="zzzdv"),
               ],
          ]
        ),
    )

@app.on_callback_query(filters.regex("medo7") & SUDOERS)
async def mpdtsf(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""<b>↯︙مرحباً بك عزيزي المطور </b>\n\n<b>↯︙استخدم الازرار بالاسفل\n↯︙ل تصفح اوامر الميوزك</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامر التسليه 1⃣", callback_data="tsluaoih"),
                    InlineKeyboardButton(
                        "اوامر التسليه 2⃣", callback_data="tsluaefgh"),
                ],[
                    InlineKeyboardButton(
                        "القائمه الرئيسيه ⏺", callback_data="zzzback"),
                ],
            ]
        ),
    )

@app.on_callback_query(filters.regex("kdkdodas") & SUDOERS)
async def zzzas(_, query: CallbackQuery):
   await query.edit_message_text(
       f""" طريقة تفعيل البوت في مجموعتك ⚡♥️:
1.) اولا قم بإضافة البوت اللي مجموعتك ⚡.
2.) قم بترقية البوت مشرف مع الصلاحيات المطلوبة ⚡.
3.)  يقوم البوت بتحديث قائمة الاداره تلقائياً ⚡.
3.)  قم بإضافة الحساب المساعد اللي المجموعة ⚡.
4.) تاكد من تشغيل المحادثة المرئية ⚡.
📌  اذا لم يستطع الحساب المساعد الانضمام اللي المحادثة المرئيه قم بإعادة تشغيل المحادثه ⚡.
💡 في حال واجهت اي مشكلة اخري يمكنك التواصل مع المطور من هنا : https://t.me/V_l_B0\n\n⚡  Developer by 𝗠.𝗲.𝗗.𝗼.𝗢
""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "القائمه الرئيسيه ⏺", callback_data="zzzdv"),
               ],
          ]
        ),
   )
