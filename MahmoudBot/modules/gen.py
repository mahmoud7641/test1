import asyncio

from pyrogram import Client, filters
from oldpyro import Client as Client1
from oldpyro.errors import ApiIdInvalid as ApiIdInvalid1
from oldpyro.errors import PasswordHashInvalid as PasswordHashInvalid1
from oldpyro.errors import PhoneCodeExpired as PhoneCodeExpired1
from oldpyro.errors import PhoneCodeInvalid as PhoneCodeInvalid1
from oldpyro.errors import PhoneNumberInvalid as PhoneNumberInvalid1
from oldpyro.errors import SessionPasswordNeeded as SessionPasswordNeeded1
from pyrogram.errors import (
    ApiIdInvalid,
    FloodWait,
    PasswordHashInvalid,
    PhoneCodeExpired,
    PhoneCodeInvalid,
    PhoneNumberInvalid,
    SessionPasswordNeeded,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telethon import TelegramClient
from telethon.errors import (
    ApiIdInvalidError,
    PasswordHashInvalidError,
    PhoneCodeExpiredError,
    PhoneCodeInvalidError,
    PhoneNumberInvalidError,
    SessionPasswordNeededError,
)
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest
from pyromod.listen.listen import ListenerTimeout

from config import SUPPORT_CHAT,OWNER_ID
from MahmoudBot import Mahmoud
from MahmoudBot.utils import retry_key


async def gen_session(
    message, user_id: int, telethon: bool = False, old_pyro: bool = False
):
    if telethon:
        ty = f"<b>تليثون</b>"
    elif old_pyro:
        ty = f"<b>بايروجورام</b> 𝐯𝟏"
    else:
        ty = f"<b>بايروجورام</b> 𝐯𝟐"

    await message.reply_text(f"» جار بدأ استخراج جلسة {ty}...")

    try:
        api_id = await Mahmoud.ask(
            identifier=(message.chat.id, user_id, None),
            text="<b>» من فضلك ارسل API ID :</b>",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Mahmoud.send_message(
            user_id,
            "» استنيتك 5 دقائق وقتك خلص.\n\nمن فضلك استخرج مجدداً.",
            reply_markup=retry_key,
        )

    if await cancelled(api_id):
        return

    try:
        api_id = int(api_id.text)
    except ValueError:
        return await Mahmoud.send_message(
            user_id,
            "» الـ API ID اللي ارسلته غلط.\n\nمن فضلك اعد الاستخراج.",
            reply_markup=retry_key,
        )

    try:
        api_hash = await Mahmoud.ask(
            identifier=(message.chat.id, user_id, None),
            text="<b>» ارسل الـ API HASH للإكمال :</b>",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Mahmoud.send_message(
            user_id,
            "» استنيتك 5 دقائق وقتك خلص.\n\nمن فضلك استخرج مجدداً.",
            reply_markup=retry_key,
        )

    if await cancelled(api_hash):
        return

    api_hash = api_hash.text

    if len(api_hash) < 30:
        return await Mahmoud.send_message(
            user_id,
            "» الـ API HASH اللي ارسلته غلط.\n\nمن فضلك اعد الاستخراج.",
            reply_markup=retry_key,
        )

    try:
        phone_number = await Mahmoud.ask(
            identifier=(message.chat.id, user_id, None),
            text="<b>⎆ يـرجـى إرسـال رقـم هاتفـك مـع رمـز الدولة مثــال 📱: +201025814272</b>",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Mahmoud.send_message(
            user_id,
            "» استنيتك 5 دقائق وقتك خلص.\n\nمن فضلك استخرج مجدداً.",
            reply_markup=retry_key,
        )

    if await cancelled(phone_number):
        return
    phone_number = phone_number.text

    await Mahmoud.send_message(user_id, "<b>» جار إرسال الكود للرقم اللي ارسلته..</b>.")
    if telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="Mahmoud", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()

    try:
        if telethon:
            code = await client.send_code_request(phone_number)
        else:
            code = await client.send_code(phone_number)
        await asyncio.sleep(1)

    except FloodWait as f:
        return await Mahmoud.send_message(
            user_id,
            f"» فشل في ارسال الكود للستجيل.\n\nمن فضلك انتظر {f.value or f.x} ثانية و حاول مجدداً.",
            reply_markup=retry_key,
        )
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        return await Mahmoud.send_message(
            user_id,
            "» الايبي هاش او الايبي ايدي اللي ارسلتهم غلط.\n\nمن فضلك اعد الاستخراج.",
            reply_markup=retry_key,
        )
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        return await Mahmoud.send_message(
            user_id,
             "» الرقم اللي ارسلته غلط.\n\nمن فضلك اعد الاستخراج.", 
            reply_markup=retry_key,
        )

    try:
        otp = await Mahmoud.ask(
            identifier=(message.chat.id, user_id, None),
            text=f"<b> من فضلك ارسل الكود اللي انبعت لـ {phone_number}.\n\nلو الكود كدا <code>12345</code> , من فضلك :أرسله كدا، يكون بين كل رقم مسافة <code>1 2 3 4 5.</code> </b>",
            filters=filters.text,
            timeout=600,
        )
        if await cancelled(otp):
            return
    except ListenerTimeout:
        return await Mahmoud.send_message(
            user_id,
            "» استنيتك 10 دقائق وقتك خلص.\n\nمن فضلك استخرج مجدداً.", 
            reply_markup=retry_key,
        )

    otp = otp.text.replace(" ", "")
    try:
        if telethon:
            await client.sign_in(phone_number, otp, password=None)
        else:
            await client.sign_in(phone_number, code.phone_code_hash, otp)
    except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
        return await Mahmoud.send_message(
            user_id,
            "» الكود اللي ارسلته:<b>غلط.</b>\n\nمن فضلك اعد الاستخراج مجدداً.",
            reply_markup=retry_key,
        )
    except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
        return await Mahmoud.send_message(
            user_id,
            "» الكود اللي ارسلته:<b>منتهي الصلاحية.</b>\n\nمن فضلك اعد الاستخراج مجدداً.",
            reply_markup=retry_key,
        )
    except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
        try:
            pwd = await Mahmoud.ask(
                identifier=(message.chat.id, user_id, None),
                text="<b>» من فضلك ارسل كلمة سر تحقق الخطوتين للإكمال</b>",
                filters=filters.text,
                timeout=300,
            )
        except ListenerTimeout:
            return Mahmoud.send_message(
                user_id,
                "» استنيتك 5 دقائق وقتك خلص.\n\nمن فضلك استخرج مجدداً.",
                reply_markup=retry_key,
            )

        if await cancelled(pwd):
            return
        pwd = pwd.text

        try:
            if telethon:
                await client.sign_in(password=pwd)
            else:
                await client.check_password(password=pwd)
        except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
            return await Mahmoud.send_message(
                user_id,
                "» كلمة سر تحقق الخطوتين اللي ارسلتها غلط.\n\nمن فضلك اعد الاستخراج.",
                reply_markup=retry_key,
            )

    except Exception as ex:
        return await Mahmoud.send_message(user_id, f"خطأ : <code>{str(ex)}</code>")

    try:
        txt = """
                <b>تم استخراج كود جلستك من:</b> @ENO6bot
نوع الجلسة: {0}

<code>{1}</code>

<b>المطور:</b> @VL_VD
<b>انـتـبـه❗:</b> لا تعطي كود جلستك لأي شخص، يمكن له اختراق او حذف حسابك بواسطة الكود!
<b>قناة المطور:</b> @YY5Y8
"""
        if telethon:
            string_session = client.session.save()
            await client.send_message(
                "me",
                txt.format(ty, string_session, SUPPORT_CHAT),
                link_preview=False,
                parse_mode="html",
            )
            await client(JoinChannelRequest("@YY5Y8"))
        else:
            string_session = await client.export_session_string()
            await client.send_message(
                "me",
                txt.format(ty, string_session, SUPPORT_CHAT),
                disable_web_page_preview=True,
            )
            await client.join_chat("yy5y8")
    except KeyError:
        pass
    try:
        await client.disconnect()
        await Mahmoud.send_message(
            chat_id=user_id,
            text=f"تم إستخراج بنجاح جلسة {ty}.\n\nمن فضلك تحقق من الرسائل المحفوظة.\n\nبوت الاستخراج بواسطة: @VL_VD.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="الرسائل المحفوظة",
                            url=f"tg://openmessage?user_id={user_id}",
                        )
                    ]
                ]
            ),
            disable_web_page_preview=True,
        )
    except:
        pass


async def cancelled(message):
    if "/cancel" in message.text:
        await message.reply_text(
            "</b>» تم إلغـاء عملية الإستخراج !<b>", reply_markup=retry_key
        )
        return True
    elif "/restart" in message.text:
        await message.reply_text(
            "<b>» تم ترسيت البوت بنجـاح ✅ !</b>", reply_markup=retry_key
        )
        return True
    elif message.text.startswith("/"):
        await message.reply_text(
            "<b>» تم إلغـاء عملية الإستخراج !</b>", reply_markup=retry_key
        )
        return True
    else:
        return False
        
