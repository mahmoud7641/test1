import asyncio
import importlib

from pyrogram import idle

from MahmoudBot import LOGGER, Mahmoud
from MahmoudBot.modules import ALL_MODULES


async def Mahmoud_boot():
    try:
        await Mahmoud.start()
    except Exception as ex:
        LOGGER.error(ex)
        quit(1)

    for all_module in ALL_MODULES:
        importlib.import_module("MahmoudBot.modules." + all_module)

    LOGGER.info(f"@{Mahmoud.username} بدأ البوت.")
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(Mahmoud_boot())
    LOGGER.info("جار ايقاف البوت...")
