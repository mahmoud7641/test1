from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup,Message

from config import SUPPORT_CHAT,OWNER_ID


keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="بدا استخراج الجلسة 🖥️", callback_data="gensession")
                    ],
                    [
                    InlineKeyboardButton("سـورس مـحـمـود - Mahmoud", url="t.me/YY5Y8")
                    ],
                    [
                    InlineKeyboardButton("مـعـلـومات الـمـطـور", url="t.me/S9_FG"),
                ],
                [
                    InlineKeyboardButton("الـمـطـور👷", user_id=OWNER_ID),
                    InlineKeyboardButton("اوامـر الـبـوت", url="https://telegra.ph/%D8%A7%D9%88%D8%A7%D9%85%D8%B1-%D8%A8%D9%88%D8%AA-%D8%A7%D9%84%D8%A7%D8%B3%D8%AA%D8%AE%D8%B1%D8%A7%D8%AC-10-11")
                ]
            ]
        )

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="بايروجورام v1", callback_data="pyrogram1"),
            InlineKeyboardButton(text="بايروجورام v2", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="تليثون", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="استخرج مجدداً", callback_data="gensession")]]
)
