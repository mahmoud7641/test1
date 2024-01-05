from pyrogram import filters
from pyrogram.types import Message

from config import OWNER_ID
from MahmoudBot import Mahmoud
from MahmoudBot.utils import get_served_users


@Mahmoud.on_message(filters.command(["stats", "users"]) & filters.user(OWNER_ID))
async def get_stats(_, message: Message):
    users = len(await get_served_users())
    await message.reply_text(f"»  الاحصائيات الحالية من {Mahmoud.name} :\n\n {users عدد المستخدمين")
