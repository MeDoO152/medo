import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message
from ZeMusic import app



###############الاوامر الموجوده هنااا############

#رابط الجروب 
#شغال



@app.on_message(command(["الرابط","/link"]) & ~filters.bot & ~filters.private)
async def invitelink(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        return await message.reply_text("قم برفعي مسؤول في المجموعة أولا ؟")
    await message.reply_text(f"**تم إنشاء رابط الدعوة بنجاح :**\n {invitelink}")
    
