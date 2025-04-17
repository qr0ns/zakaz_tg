import asyncio

import logging

from aiogram import Dispatcher, Bot

from config import TOKEN_API
from handlers import router


bot = Bot(token=TOKEN_API)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot was successfully finished")