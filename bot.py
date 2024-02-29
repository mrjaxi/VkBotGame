import logging

import asyncio

import aiomysql
import pymysql
import pymysql.cursors
from aiomysql import create_pool

from vkbottle.bot import Bot, Message
from config import labeler, api, state_dispenser
from database.settings import settings
from handlers import chat_labeler, admin_labeler
from environs import Env

logger = logging.getLogger(__name__)
env = Env()
env.read_env(".env")

loop = asyncio.get_event_loop()





async def main():
    if not settings.conn:
        try:
            settings.conn = await create_pool(host=env.str("DB_HOST"), user=env.str("DB_USER"),
                                        password=env.str("DB_PASS"),
                                        db=env.str("DB_NAME"), maxsize=50)

            print("Pool = ", settings.conn)
        except aiomysql.Error as e:
            print(f'Error connecting: {e}')

    print("DB AIO")



    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    labeler.load(chat_labeler)
    labeler.load(admin_labeler)
    bot = Bot(
        api=api,
        labeler=labeler,
        state_dispenser=state_dispenser,
    )
    try:
        await bot.run_polling()
    finally:
        await asyncio.sleep(1)


if __name__ == '__main__':
    try:
        # loop.run_until_complete(dblib())
        # asyncio.set_event_loop(loop)
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
