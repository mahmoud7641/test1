from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from MahmoudBot import Mahmoud
from MahmoudBot.utils import add_served_user, keyboard


@Mahmoud.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    await message.reply_text(
        text=f"""
           ¤¦ اهلا بـك عزيـزي {message.from_user.first_name} فـي بـوت اسـتـخـراج الـجلـسـات

¤¦ يمكنك استـخـراج التالـي

¤¦  تـلـيـثـون 

¤¦ بايـروجـرام 

¤¦ تم انشاء البوت بواسطة: @VL_VD """,
        reply_markup=keyboard,
        disable_web_page_preview=True,
    )
    await add_served_user(message.from_user.id)
