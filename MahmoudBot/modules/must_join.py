from config import MUST_JOIN
from MahmoudBot import Mahmoud
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Mahmoud.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Mahmoud, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/YY5Y8" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://telegra.ph/file/e924a4f0982e80f18c49e.jpg", caption=f"  ¤¦ اهلا بك عزيزي\n\n¤¦ لا يمكنك استخدام البوت\n\n¤¦ الا بعد الاشتراك بقناة البوت\n\n¤¦ اشترك بالقناة بعدها ارسل /start .",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("إضغط للاشتراك بالقناة", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"ضعني ادمن في قناة الاشتراك الاجباريMUST_JOIN chat : {MUST_JOIN} !")
        
        
        
