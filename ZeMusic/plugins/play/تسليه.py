import asyncio
import random
import config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from ZeMusic import app
from strings.filters import command
from config import OWNER_ID
from pyrogram.enums import ParseMode, ChatMemberStatus



iddof = []
@app.on_message(
     command(["قفل العاب","تعطيل العاب"])
     & filters.group

   
)
async def iddlock(client:Client, message:Message):
    dev = (OWNER_ID)
   
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.id in dev:
        rotba = "مطـور اساسي"
    if get.status in [ChatMemberStatus.OWNER]:
        rotba= "المــــألك"
    if get.status in [ChatMemberStatus.ADMINISTRATOR]:
        rotba= "أدمـــن"
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and dev:
        if message.chat.id in iddof:
            return await message.reply_text(f"**يا {message.from_user.mention}\n الالعاب مقفله من قبل**")
        iddof.append(message.chat.id)
        return await message.reply_text(f"**تم قفل الالعاب بنجاح\n\nبواسطة {rotba} ←{message.from_user.mention}**")
    else:
        return await message.reply_text(f"**يا {message.from_user.mention} انت لست مشرفا هنا**")
        
        
@app.on_message(
    command(["فتح العاب","تفعيل العاب"])
    & filters.group
)
async def idljjopen(client:Client, message:Message):
    dev = (OWNER_ID)
    
    get = await client.get_chat_member(message.chat.id, message.from_user.id)
    if message.from_user.id in dev:
        rotba = "مطـور اساسي"
    if get.status in [ChatMemberStatus.OWNER]:
        rotba= "المــــألك"
    if get.status in [ChatMemberStatus.ADMINISTRATOR]:
        rotba= "أدمـــن"
    if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR] and  dev:
        if not message.chat.id in iddof:
            return await message.reply_text(f"**يا {message.from_user.mention}\n الالعاب مفتوحه من قبل**")
        iddof.remove(message.chat.id)
        return await message.reply_text(f"**تم فتح الالعاب بنجاح\n\nبواسطة {rotba} ←{message.from_user.mention}**")
    else:
        return await message.reply_text(f"**يا {message.from_user.mention} انت لست مشرفا هنا**")
        
@app.on_message(command(['زوجني','ز']))
def iddd(client:Client, message:Message):
    chat_id = message.chat.id
    if chat_id in iddof:
         return
    members = [
        member for member in client.get_chat_members(chat_id)
        if not member.user.is_bot
    ]
    random_member = random.choice(members)
    random_member_mention = f"[{random_member.user.first_name}](tg://user?id={random_member.user.id})"
    random_message = random.choice([
        f"• اخترت لك هذا الشخص {random_member_mention} \n 🙈♥️",
        f"• اخترت لك هذا الشخص \n {random_member_mention} \n **"
    ])
    client.send_message(chat_id, random_message, reply_to_message_id= message.id)
@app.on_message(command(['اقتباس','ق']))
def call_random_member(client:Client, message:Message):
    chat_id = message.chat.id
    members = [
        member for member in client.get_chat_members(chat_id)
        if not member.user.is_bot
    ]
    if chat_id in iddof:
        return
    random_member = random.choice(members)
    random_member_mention = f"[{random_member.user.first_name}](tg://user?id={random_member.user.id})"
    random_message = random.choice([
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n يجب أن تحاول ثلاث مرات قبل اليأس **",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n أعطي كل يوم فرصة لتصبح أفضل يوم في حياتك**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n لحكمة هي معرفة متى تتجاهل**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n الصبر هو المفتاح إلى كلَّ قفل غامض**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n أنت مسؤول عن ماتشعر به، ولكنك لست مسؤولًا عن ما يفعله الآخرون**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n حكمتي تقول: دع الغضب يقتلع من قلبك السعادة كما تقتل الفحم النار من طريقه**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n إذا لم تكن تعيش بالطريقة التي تريدها، يجب عليك أن تغيرها**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n الفائزون لا يقومون بممارسة الأسرار. إنهم يتوجهون نحو الأهداف الكبيرة**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n ليس هناك شيء أفضل في الحياة من أن تكون في حالة حب وسعادة**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n عندما يتغير الريح، يجب علينا أن نعدل اتجاه الشراع بدلاً من أن نتوقف عن السفر**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n الحياة مثل الموج عليك فقط أن تجد توازنك حتى لا تسقط**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n العلم يجري كالماء، ولا يتوقف أبدًا - لا على الجدران ولا على السور، لكنه يصب في نهاية المطاف في ثنايا الإنسان**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n الشجرة التي لا تنحني عند الريح، هي التي تتحطم في الاعاصير**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n امنيتي ان يكون فيها زوايا خطرة ، فلا شي يمكن ان ينمي من دون التحدي**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n لا يمكنك تجاهل الظلام. يجب أن تنشئ شمعة**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n إن للبُعدِ طعمً يُصدِرُه الألمْ، ولكنَّ مِن يُجيد العِشقَ يجفَل الأميال **",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n المرء لا يتشكل على أساس المواقف التي يمر بها بل على أساس الردود التي يمنحها لتلك المواقف **",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n أن تختار، في النهاية، طريقًا واحدًا، لم يكن في صالحك أن تترك طرقاً أخرى غير مستكشفة ",
         f"-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n إن لم يكن عندك شيء جيد ليقال، فابقَ صامتًا**",
         f"**-اليــك اقتبــاس اليـوـم ❤️\n│ لـ {random_member_mention}\n النجاح هو القدرة على الذهاب من فشل إلى فشل بدون فقد أرزاقك الحماس **", 
    ])
    client.send_message(chat_id, random_message, reply_to_message_id= message.id)
@app.on_message(command(['نداء','ن']))
def call_random_member(client:Client, message:Message):
    chat_id = message.chat.id
    members = [
        member for member in client.get_chat_members(chat_id)
        if not member.user.is_bot
    ]
    if chat_id in iddof:
         return
    random_member = random.choice(members)
    random_member_mention = f"[{random_member.user.first_name}](tg://user?id={random_member.user.id})"
    random_message = random.choice([
        f"ووين ككارس لنا واجد نرجو فيك 😾 {random_member_mention}",
        f"• يـا قمـري ❤️‍🔥 {random_member_mention}",
        f"حبي فوتك من الخاص وتعال 🤔 {random_member_mention}",
        f"• يـا راس السطل تعال {random_member_mention}",
        f"• انت ليش قمر هكي 🌚♥ {random_member_mention}"
    ])
    client.send_message(chat_id, random_message, reply_to_message_id= message.id)



GAME_MESSAGE = "ꪔᥱ𝙳o᥆\n\n🐉¦ مرحبا بك عزيزي:\n🐉¦في قسم العاب ميدو\n\nꪔᥱ𝙳o᥆"
GAME_BUTTONS = [
    [ 
        InlineKeyboardButton ('العاب 3D', callback_data= 'GAME1'),
        InlineKeyboardButton ('مميزات', callback_data= 'GAME2'),
        ],[
        InlineKeyboardButton ('⌞ ᥉᥆υᖇᥴᥱ ꪔᥱ𝙳o᥆⌝', url =f"https://t.me/V_l_B2")              
                 ],[
                InlineKeyboardButton(
                        "𝗁᥆ꪔᥱ", callback_data="close"),
               ],
          ]
    

nmla = []


@app.on_message(command("رفع نمله"))
async def rf3nmla(client, message):
  if not message.reply_to_message.from_user.mention in nmla:
    nmla.append(message.reply_to_message.from_user.mention)
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n نمله 😂♥️")


@app.on_message(command("تنزيل نمله"))
async def tnzelnmla(client, message):
  if message.reply_to_message.from_user.mention in nmla:
    nmla.remove(message.reply_to_message.from_user.mention)
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n نمله 😂♥️")


@app.on_message(command("المرفوعين نمل"))
async def nml(client, message):
  nq = ""
  for n in nmla:
      nq += n + "\n"
  await message.reply_text(nq)





@app.on_message(command("رفع صرصار"))
async def rf3srsar(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n صرصار 😂♥️")


@app.on_message(command("تنزيل صرصار"))
async def tnzelsrar(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n صرصار 😂♥️")


@app.on_message(command("رفع رقاصه"))
async def yasooo(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n رقاصه حد يرمي فلوس عليها 😂💃")


@app.on_message(command("تنزيل رقاصه"))
async def yaso(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n رقاصه تابت😂😔")
  
  
@app.on_message(command("رفع متناك"))
async def bjoiuyjk(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n متناك حد يركبو 😂♥️")


@app.on_message(command("تنزيل متناك"))
async def kamal(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n متناك اعرث تاب 😂♥️")
  
  
@app.on_message(command("رفع نجس"))
async def fdsa(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n نجس بنجاح  😂♥️")


@app.on_message(command("تنزيل نجس"))
async def kophvc(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n النجس استحمي 😂♥️")
  
  
@app.on_message(command("رفع عره"))
async def roky(client, message):
  await message.reply_text(f"تم رفع العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n عره عالمجتمع 😂♥️")


@app.on_message(command("تنزيل عره"))
async def zerso(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n عره خلاص 😂♥️")
  
  
@app.on_message(command("رفع بقره"))
async def vvvtyy(client, message):
  await message.reply_text(f"تم رفع العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n بقا بقر حديحلبو 🐄🤭")


@app.on_message(command("تنزيل بقره"))
async def tttryuh(client, message):
  await message.reply_text(f"تم تنزيل العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n خلاص خلص لبن 😂")
  
  
@app.on_message(command("رفع قرد"))
async def uiipppl(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n قرد حد يديلو موزه 😂🐒")


@app.on_message(command("تنزيل قرد"))
async def bjhupq(client, message):
  await message.reply_text(f"تم تنزيل العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n القرد بقا انسان🙊🧍")
  
  
@app.on_message(command("رفع قلبي"))
async def pooiejh(client, message):
  await message.reply_text(f"تم رفع العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n خلاص بقيت قلبو 😂♥️")


@app.on_message(command("تنزيل قلبي"))
async def ttrqew(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\nمبقتش قلبوو 😭💔")
  
  
@app.on_message(command("رفع خدام"))
async def qyui(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n خدام تع خدم ع البار    😂🤓")


@app.on_message(command("تنزيل خدام"))
async def klhj(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n الخدام ساب الشغل  😢🚶")
  
  
@app.on_message(command("رفع معرص"))
async def wqew(client, message):
  await message.reply_text(f"تم رفع العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n معرص البار  😂🤓")


@app.on_message(command("تنزيل معرص"))
async def ohho(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n المعرص بقا راجل   😂🧔")
  
  
@app.on_message(command("رفع ارمله"))
async def drsss(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n  بقيتي ارمله وجوزك مات 🥹")


@app.on_message(command("تنزيل ارمله"))
async def gkvdr(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n خلاث متبقيش قموصه جوزك عايش اهو 😂🫶🏻")
  
  
@app.on_message(command("رفع مزه"))
async def cgfyu6f(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n يمزه خدي بالك من نفسك 🥹❤️")


@app.on_message(command("تنزيل مزه"))
async def hhhhug(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n انتي صدقتي انك مزه ولا اي انا كنت بطبل 😂😝")
  
  
@app.on_message(command("رفع ابني"))
async def cbky(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n  بقيت ابنو وكل حياتو🥹🖤")


@app.on_message(command("تنزيل ابني"))
async def ccgy(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n حتي عيلتك مش طيقاك ورموك في الشارع ")
  
  
@app.on_message(command("رفع خاينه"))
async def mkloo(client, message):
  await message.reply_text(f"تم رفع العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n  ي خاينه ي مهزأه ")


@app.on_message(command("تنزيل خاينه"))
async def fkijbh(client, message):
  await message.reply_text(f"تم تنزيل العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n مين الاهبل للي كان مفكر القمر دا ممكن يبقي خاين 🥹🥹💕")  
  
  
@app.on_message(command("رفع بنتي"))
async def yuhhss(client, message):
  await message.reply_text(f"تم رفع العض\n🗿 \n√و : {message.reply_to_message.from_user.mention}\n\n بقيتي بنتي وحته من قلبي 🥹❤️❤️❤️")


@app.on_message(command("تنزيل بنتي"))
async def hloih(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\nكنت بهزر انا مخلفتش لسه🤡😂  ")  
  
  
@app.on_message(command("رفع خاين"))
async def kloss(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n خنتها كام مره قول متتكسفش يخاين")


@app.on_message(command("تنزيل خاين"))
async def fiihug(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n ايدا طلع سوء تفاهم انت اشرف من الشرف يسالك😂❤️")
  
  
@app.on_message(command("رفع خول"))
async def dadr(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n 😂 خول طول عمرك مش اول مره")


@app.on_message(command("تنزيل خول"))
async def hjj7gv(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n  اهو يعم نزلتك 🙂💕")
  
  
@app.on_message(command("رفع حمار"))
async def cgfyu6f(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n خلاص بقت حمار رسمي نظمي😹")


@app.on_message(command("تنزيل حمار"))
async def cxxv(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n خلاث يعم كنا بنهزر معاك متبقاش قفوش 😂😝")
  
  



@app.on_message(command("رفع غبي"))
async def polkij(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n غبي و هتفضل غبي😹🤞")


@app.on_message(command("تنزيل غبي"))
async def nbvcc(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n غبي و بقي بيفهم😹🫶")
  
  
@app.on_message(command("رفع مراتي"))
async def ttttuhyp(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n مراتك خد و عملو واحد😹😽")


@app.on_message(command("تنزيل مراتي"))
async def xxxxt(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n طلقتها شوف غيرها 😂😝")  
  
  
@app.on_message(command("رفع زبال"))
async def oooph(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n زبال تع  نضف الجروب😹")


@app.on_message(command("تنزيل زبال"))
async def zzzas(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n زبال تعب و استقال 😂😝")  
  
  
@app.on_message(command("رفع خدامه"))
async def ggggop(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n خدامه تع اغسلي رجلي 😹🤞")


@app.on_message(command("تنزيل خدامه"))
async def vvvuu(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\nخدامه نزلت اجازه😹🫶")  
  
  
@app.on_message(command("رفع كلبه"))
async def mmmuy(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n كلبه خدي عضمه😹🤞")


@app.on_message(command("تنزيل كلبه"))
async def dfrewq(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n خلاث كلبه تحولت الانسان😿😹")  
  
  
@app.on_message(command("رفع طيز"))
async def ssoss(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n طيز و كبيره كمان😹🤞")


@app.on_message(command("تنزيل طيز"))
async def nobo(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n طيز متزعلش نزلتك😹🫶")  
  
  
@app.on_message(command("رفع حرامي"))
async def llok(client, message):
  await message.reply_text(f"تم رفع العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n حرامي وهبلغ عنه😹🚓")


@app.on_message(command("تنزيل حرامي"))
async def kaompj(client, message):
  await message.reply_text(f"تم تنزيل العضو\n🗿 \n√ : {message.reply_to_message.from_user.mention}\n\n حرامي ربنا تاب عليه😂😔")
  
  
@app.on_message(
    command(["الالعاب","العاب","الالعاب. 🐰"])
   
)
async def zohary(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fd1d0b81db80a82bdb407.jpg",
        caption= GAME_MESSAGE,
        reply_markup=InlineKeyboardMarkup(GAME_BUTTONS)
    )  
@app.on_callback_query()
async def callback_query(client, CallbackQuery):
          if CallbackQuery.data == "GAME1":
            
             GAME1_MESSAGE = "ꪔᥱ𝙳o᥆\n\nمرحبا بك في قسم العاب 3D\n\n🐉"

             GAME1_BUTTONS = [
                 [
                    InlineKeyboardButton(
                        "°فلابي بيرد°", url=f"http://t.me/awesomebot?game=FlappyBird"), 
                    InlineKeyboardButton (
                        "°تبديل النجوم°", url=f"http://t.me/gamee?game=Switchy"),
                ],[
                    InlineKeyboardButton (
                        "°موتسيكلات°" , url=f"http://t.me/gamee?game=motofx"),
                    InlineKeyboardButton (
                        "°اطلاق النار°" , url=f"http://t.me/gamee?game=NeonBlaster"),
                ],[
                    InlineKeyboardButton (
                        "°كرة القدم°" , url=f"http://t.me/gamee?game=Footballstar"),
                    InlineKeyboardButton (
                        "°تجميع الالوان°" , url=f"http://t.me/awesomebot?game=Hextris"),
                ],[        
                    InlineKeyboardButton (
                        "°المجوهرات°" , url=f"http://t.me/gamee?game=DiamondRows"),
                    InlineKeyboardButton (
                        "°ركل الكرة°" , url=f"http://t.me/gamee?game=KeepitUP"),
                ],[        
                    InlineKeyboardButton (
                        "°بطولة السحق°" , url=f"http://t.me/gamee?game=SmashRoyale"),
                    InlineKeyboardButton (
                        "°2048°" , url=f"http://t.me/awesomebot?game=g2048"),
                ],[        
                    InlineKeyboardButton (
                        "°كرة السلة°" , url=f"http://t.me/gamee?game=BasketBoy"),
                    InlineKeyboardButton (
                        "°القط المجنون°" , url=f"http://t.me/gamee?game=CrazyCat"),
                ],[
                    InlineKeyboardButton (
                        "𝗁᥆ꪔᥱ" , callback_data= 'GAME')
                  ],
             ]
             await CallbackQuery.edit_message_text( 
                 GAME1_MESSAGE ,
                 reply_markup = InlineKeyboardMarkup(GAME1_BUTTONS) 
              )
          elif CallbackQuery.data == "GAME":
               
               RETURN_GAME = "ꪔᥱ𝙳o᥆\n\n🐉¦مرحبا بك في قسم العاب cr\n🐉¦اختار ما تشاء من الالعاب مسليه وستمتع بها\n\nꪔᥱ𝙳o᥆" 

               RETURN_BUTTON = [
                    [ 
                      InlineKeyboardButton ('🕷¦العاب 3D', callback_data= 'GAME1'),
                      InlineKeyboardButton ('🐰¦العاب', callback_data= 'GAME2')
                      ],[
        InlineKeyboardButton ('⌞ ᥉᥆υᖇᥴᥱ ꪔᥱ𝙳o᥆⌝', url =f"https://t.me/V_l_B2")              
                 ],[
                InlineKeyboardButton(
                        "𝗁᥆ꪔᥱ", callback_data="GAME"),
               ],
          ]
     
               await CallbackQuery.edit_message_text( 
                 RETURN_GAME ,
                 reply_markup = InlineKeyboardMarkup(RETURN_BUTTON) 
                    )
          elif CallbackQuery.data == "GAME2":
               
               SOURCE_GAME = "🐰\n\n العاب ميدو\nكت\nتويت\nاسال\nصراحه\nانا مين\nبايو\nمين في الكول\nسورس\nزخرفه\nاذكار\nانصحني\nكتبات\nافلام\nغنيلي\nرفع\nذكاء\nنكته\nكشف\nايدي\nميديا\nتحويل ملصق\n🐰." 

               SORGAM_BUTTON = [
                    [ 
                      InlineKeyboardButton ('⌞ ᥉᥆υᖇᥴᥱ ꪔᥱ𝙳o᥆⌝', url =f"https://t.me/V_l_B2")
                      ],[
                         InlineKeyboardButton (
                                 "𝗁᥆ꪔᥱ", callback_data="GAME"),
                    ]
               ]    
               await CallbackQuery.edit_message_text( 
                 SOURCE_GAME ,
                 reply_markup = InlineKeyboardMarkup(SORGAM_BUTTON) 
                    )
    
    
