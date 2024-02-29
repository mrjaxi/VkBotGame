import asyncio

import aiomysql
from aiomysql import create_pool
from environs import Env

import bot
from config import labeler
from database.aiodb import user_info, full_user_info
from database.db import Database
from database.settings import settings, settingsAio
from states.mystates import AddNfsStates

db = Database('database.db')

aioDbState = False

@labeler.message(command="add_nfc")
async def add_nfc_start(message):
    await bot.state_dispenser.set(message.peer_id, AddNfsStates.START_STATE)
    return "Теперь вводите номера меток"


@labeler.message(command="nfc_stop", state=AddNfsStates.START_STATE)
async def nfc_stop_start(message):
    await bot.state_dispenser.delete(message.peer_id)
    return "Вы вышли из раздела добавления меток"


@labeler.message(state=AddNfsStates.START_STATE)
async def add_nfc(message):
    if str(message.text).isdigit():
        if db.card_exists(message.text):
            await message.answer("Метка с таким номером уже существует\nВведите другой номер метки")
        else:
            db.set_nfc_id(message.text)
            await message.answer(f"Метка с номером {message.text} введена в БД")
    else:
        await message.answer("Введено некорректное число")


@labeler.message(text="stop_game")
async def ping_handler(message):
    await bot.state_dispenser.delete(message.peer_id)

env = Env()
env.read_env(".env")
@labeler.message(text="aionew")
async def ping_handleer(message):
    await message.answer("Начало")
    for i in range(0, 9):
        data = await user_info("111235234")
        print("Данные = ", data)
    await message.answer("Конец")


@labeler.message(text="aio")
async def ping_handler(message):
    if not settingsAio.aiocheck:
        await message.answer("Начало")
        if not settings.conn:
            try:
                await message.answer("Соединение...")
                print("Установка соединения")
                settings.conn = await create_pool(host=env.str("DB_HOST"), user=env.str("DB_USER"),
                                                  password=env.str("DB_PASS"),
                                                  db=env.str("DB_NAME"), maxsize=50)

                print("Pool = ", settings.conn)
                await message.answer("Соединение завершено")
            except aiomysql.Error as e:
                await message.answer("Ошибка соединения")
                print(f'Error connecting: {e}')
            print("Установка соединения звершена")
        print("Начало")
        await message.answer("Запуск цикла")
        settingsAio.aiocheck = True
        while settingsAio.aiocheck:
            settingsAio.mass = await full_user_info()
            print("Данные = ", settingsAio.mass)
            await asyncio.sleep(2)
        await message.answer("Завершение цикла")
        await message.answer("Конец")
    else:
        settingsAio.aiocheck = False

