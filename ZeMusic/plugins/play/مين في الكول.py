from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ZeMUSIC import app
from config import OWNER_ID
import asyncio
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from ZeMUSIC.utils.database import *
from pytgcalls.exceptions import (NoActiveGroupCall,TelegramServerError)

# Function to create inline keyboard
def create_keyboard():
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("إغلاق المحادثة الصوتية", callback_data="close_vc")]])
    return keyboard

@app.on_message(filters.regex("مين في الكول"))
async def strcall(client, message):
    assistant = await group_assistant(Ze,message.chat.id)
    try:
        await assistant.join_group_call(message.chat.id, AudioPiped("./strings/call.mp3"), stream_type=StreamType().pulse_stream)
        text="↯︙الاعضاء المتواجدين في المكالمة المرئية :\n\n"
        participants = await assistant.get_participants(message.chat.id)
        k =0
        for participant in participants:
            info = participant
            if info.muted == False:
                mut="⦗ يتكلم ⦘"
            else:
                mut="⦗ لا يتكلم ⦘"
            user = await client.get_users(participant.user_id)
            k +=1
            text +=f"{k}:{user.mention}↬{mut}\n"
        text += f"\n↯︙عدد الاشخاص في المكالمة المرئية ↬ ⦗ {len(participants)} ⦘"    
        await message.reply(f"{text}")
        await asyncio.sleep(5)
        await assistant.leave_group_call(message.chat.id)
    except NoActiveGroupCall:
        await message.reply(f"لم يتم العثور على دردشة فيديو نشطة.\nيرجى بدء دردشة فيديو في مجموعتك/قناتك والمحاولة مرة أخرى.")
    except TelegramServerError:
        await message.reply(f"ارسل مرة اخرى يوجد خطأ في احد سيرفرات التليكرام")

# Command to calculate math expressions
@app.on_message(filters.command("math", prefixes="/"))
def calculate_math(client, message):   
    expression = message.text.split("/math ", 1)[1]
    try:        
        result = eval(expression)
        response = f"ᴛʜᴇ ʀᴇsᴜʟᴛ ɪs : {result}"
    except:
        response = "ɪɴᴠᴀʟɪᴅ ᴇxᴘʀᴇssɪᴏɴ"
    message.reply(response)

# Command to make the bot leave a group (only for owner)
@app.on_message(filters.command("leavegroup") & filters.user(OWNER_ID))
async def bot_leave(_, message):
    chat_id = message.chat.id
    text = f"sᴜᴄᴄᴇssғᴜʟʟʏ   ʟᴇғᴛ  !!."
    await message.reply_text(text)
    await app.leave_chat(chat_id=chat_id, delete=True)

# Function to handle inline keyboard for video chat started
@app.on_message(filters.video_chat_started)
async def brah(client, message):
       await message.reply("𖠇 تم بدء المحادثه الصوتيه..✅\n│\n└𖠇 بواسطة الادمنيه 👨‍✈️ ", reply_markup=create_keyboard())

# Function to handle inline keyboard for video chat ended
@app.on_message(filters.video_chat_ended)
async def brah2(client, message):
    da = message.video_chat_ended.duration
    ma = divmod(da, 60)
    ho = divmod(ma[0], 60)
    day = divmod(ho[0], 24)
    if da < 60:
       await message.reply(f"𖠇 تم انهاء المحادثه الصوتيه..❎\n│\n└𖠇 وقت المحادثة : {da} ثواني ", reply_markup=create_keyboard())
    # The rest of the time calculation part is removed for simplicity

# Function to handle inline keyboard for inviting new members to video chat
@app.on_message(filters.video_chat_members_invited)
async def fuckoff(client, message):
           text = f"• قــــام ← {message.from_user.mention}"
           x = 0
           for user in message.video_chat_members_invited.users:
             try:
               text += f"\n• بــدعـــوة ←{user.first_name}"
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text}", reply_markup=create_keyboard())
           except:
             pass
