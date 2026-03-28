from aiogram import Bot, Dispatcher
import asyncio 
import config
from handlers import common, settings

async def main():
    bot = Bot(token = config.BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(common.router)
    dp.include_router(settings.router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())