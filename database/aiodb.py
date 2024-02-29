import aiomysql
import pymysql
import pymysql.cursors
from aiomysql import create_pool
from environs import Env

from database.settings import settings

env = Env()
env.read_env(".env")


# async def user_info(val):
#     print("\n\nConnection = 1")
#     con = pymysql.connect(host=env.str("DB_HOST"), port=3306, user=env.str("DB_USER"),
#                           password=env.str("DB_PASS"),
#                           db=env.str("DB_NAME"), cursorclass=pymysql.cursors.DictCursor, connect_timeout=1)
#     print("\n\nConnection = 2")
#     with con:
#         with con.cursor() as cursor:
#             # Read a single record
#             cursor.execute("SELECT * FROM Card WHERE card_id = %s", (val,))
#             result = cursor.fetchone()
#             print(result)
#     return result

async def user_info(val):
    data = None
    # settings.conn = await create_pool(host=env.str("DB_HOST"), user=env.str("DB_USER"),
    #                                         password=env.str("DB_PASS"),
    #                                         db=env.str("DB_NAME"))
    pool = settings.conn
    freesize = pool.freesize
    print(f"Count free : {freesize}")
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            try:
                await cur.execute("SELECT * FROM Card WHERE card_id = %s", (val,))
            except aiomysql.Error as ex:
                print(f'Error select: {ex}')

            data = await cur.fetchall()
            print("Data = ", data)

    # pool.close()
    # await pool.wait_closed()
    return data

async def full_user_info():
    data = None

    pool = settings.conn
    freesize = pool.freesize
    print(f"Count free : {freesize}")
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            try:
                await cur.execute("SELECT * FROM Card")
                await conn.commit()
            except aiomysql.Error as ex:
                print(f'Error select: {ex}')

            data = await cur.fetchall()
    return data
