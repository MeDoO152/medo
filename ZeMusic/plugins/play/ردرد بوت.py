import asyncio
from pyrogram import Client, filters ,enums
from strings.filters import command
from pyrogram.types import *
from ZeMusic import app
from pyrogram.enums import ChatMemberStatus
from pyrogram.enums import ParseMode, ChatMemberStatus

def get_rd(text, id):
    chat_id = str(id)
    text = text
    with open("getrdod.txt", "r+") as f:
       x = f.readlines()
       final = f"{chat_id}#{text}"
       for a in x:
         if final in a:
            return int(a.split(f"{final}AHMEDRD")[1].replace("\n",""))
    return False


def add_rd(text, id, rd) -> bool:
    chat_id = str(id)
    with open("getrdod.txt", "a+") as f:
       x = f.readlines()
       for a in x:
         if f"{chat_id}#{text}" in a:
           return False
       f.write(f"{chat_id}#{text}AHMEDRD{rd}\n")
    return True


def del_rd(x):
   word = str(x).replace("\n","")
   with open("getrdod.txt", "r+") as fp:
      lines = fp.readlines()
   with open("getrdod.txt", "w+") as fp:
          for line in lines:
            line = line.replace("\n","")
            if word != line:
              fp.write(line+"\n")
          return



def del_rdod(id) -> bool:
    chat_id = str(id)
    gps = open("getrdod.txt").read()
    if chat_id not in gps:
      return False
    with open("getrdod.txt", "r+") as fp:
      lines = fp.readlines()
    with open("getrdod.txt", "w+") as fp:
          for line in lines:
            line = line.replace("\n","")
            if chat_id not in line:
              fp.write(line+"\n")
          return


@app.on_message(filters.regex("^المشرفين$"))
async def adlist(_, message):
    chat_id = message.chat.id
    admin = "- قائمة المشرفين\n— — — — —\n"
    async for admins in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
           admin+=f"› {'@'+admins.user.username if admins.user.username else admins.user.mention} - `{admins.user.id}` .\n"
    await message.reply(text=(admin))

@app.on_message(filters.regex("^البوتات$"))
async def botslist(_, message):
    chat_id = message.chat.id
    rnryr = "- قائمة البوتات\n— — — — —\n"
    async for b in app.get_chat_members(chat_id, filter=enums.ChatMembersFilter.BOTS):
           rnryr+=f"› {'@'+b.user.username if b.user.username else b.user.mention} - `{b.user.id}` .\n"
    await message.reply(text=(ahmed))

@app.on_message(filters.regex("^اضف رد$") & filters.group)
async def adf_rd(client, message):
    get = await get_rtba(message.chat.id, message.from_user.id)
    if not get: return await message.reply("• هذا االأمر لا يخصك")
    ZeAR1 = await app.ZeAR(
    message.chat.id, "ارسل كلمة الرد", reply_to_message_id=message.id, filters=filters.text & filters.user(message.from_user.id))
    text = ZeAR1.text
    ZeAR2 = await app.ZeAR(
    message.chat.id, "ارسل جواب الرد", reply_to_message_id=ZeAR1.id, filters=filters.user(message.from_user.id))
    copy = await ZeAR2.copy(LOG)
    rd = copy.id
    a = add_rd(text, message.chat.id, rd)
    if a: return await ZeAR2.reply("تم اضافة الرد بنجاح")
    else: return await ZeAR2.reply("حدث خطأ")


@app.on_message(filters.regex("^مسح رد$") & filters.group)
async def delete_rd(client, message):
   get = await get_rtba(message.chat.id, message.from_user.id)
   if not get: return await message.reply("• هذا االأمر لا يخصك")
   ZeAR = await app.ZeAR(
     message.chat.id, "ارسل الرد الآن", filters=filters.text & filters.user(message.from_user.id), reply_to_message_id=message.id)
   a = get_rd(ZeAR.text, message.chat.id)
   if not a:
     return await ZeAR.reply("الرد غير موجود")
   x = f"{message.chat.id}#{ZeAR.text}AHMEDRD{a}"
   b = del_rd(x)
   await ZeAR.reply("• تم مسح الرد")
   


@app.on_message(filters.regex("^مسح الردود$") & filters.group)
async def delrdood(client, message):
   get = await get_rtba(message.chat.id, message.from_user.id)
   if not get: return await message.reply("• هذا االأمر لا يخصك")
   a = del_rdod(message.chat.id)
   print(a)
   if not a : return await message.reply("• تم مسح الردود هنا")
   else: return await message.reply("• لاتوجد ردود هنا")


