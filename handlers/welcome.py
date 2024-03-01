import asyncio
from datetime import datetime

from vkbottle import CtxStorage
from vkbottle import Keyboard, KeyboardButtonColor, \
    Text
import bot
from config import labeler, photo_uploader, audio_uploader
from data.group import group_position_name
from data.partOneMessage import first_part_message_one
from database.db import Database
from states.mystates import WelcomeStates, PartOneStates, TestOneStates, PartTwoStates, PartThreeStates

ctx_storage = CtxStorage()
db = Database('database.db')


@labeler.message(command="dell")
async def dell_user(message):
    db.del_user(message.peer_id)

    await message.answer("Данные о вас были удалены!")


@labeler.message(command="part")
async def test_user(message):
    nowdate = datetime.now()
    user_id = db.get_user_id(message.peer_id)[0][0]
    ctx_storage.set(f"{message.peer_id}_team", (int(user_id) % 10))
    ctx_storage.set(f"{message.peer_id}_number", 0)
    await bot.state_dispenser.set(message.peer_id, PartTwoStates.PASSWORD_START_TWO_STATES)
    await message.answer("Для продолжения введите пароль")


@labeler.message(text=['Начать', 'начать', 'Начать игру! 🌟'])
async def start_handler(message):
    if db.user_exists(int(message.peer_id)):
        await message.answer("Вы уже проходили тестирование")
    else:
        await bot.state_dispenser.set(message.peer_id, WelcomeStates.PASSWORD_START_STATE)
        # if (bool(ctx_storage.get("fio"))):
        #     await  message.answer(CtxStorage().get("fio"))
        return "🔒  Напиши пароль игры"


@labeler.message(state=WelcomeStates.PASSWORD_START_STATE)
async def password_handler(message):
    # password_for_start_game = "3333"
    if (message.text == "0102032024") or (message.text == "0103032024"):
        number = 0
        ctx_storage.set(f"{message.peer_id}_number", 0)
        # if message.text == "8888":
        #     number = 0
        #     ctx_storage.set(f"{message.peer_id}_number", 0)
        # elif message.text == "5555":
        #     number = 1
        #     ctx_storage.set(f"{message.peer_id}_number", 1)
        # elif message.text == "6666":
        #     number = 2
        #     ctx_storage.set(f"{message.peer_id}_number", 2)
        # else:
        #     number = 3
        #     ctx_storage.set(f"{message.peer_id}_number", 3)
        # await message.answer(CtxStorage().get("a"))
        keyboard = (
            Keyboard(inline=True)
            .add(Text("Готов! Начинаем! 😎"), color=KeyboardButtonColor.POSITIVE)
        ).get_json()
        nowdate = datetime.now()
        newdate = nowdate.strftime("%d/%m/%Y")
        db.add_user(message.peer_id, newdate, number)

        await message.answer("Ты ввел правильный пароль! 🥳"
                             "\n\nНачинаем нашу игру! ", keyboard=keyboard)

    elif (message.text == "Готов! Начинаем! 😎"):
        photo1 = await photo_uploader.upload(
            file_source=f"img/ЧАСТЬ 1 - ТЕХНЛОГИЯ.png",
            peer_id=message.peer_id,
        )
        await message.answer("""В этой увлекательной игре 3 части :\n\n1. Технология\n\n2. Карьера\n\n3. Вызовы\n\nИ вот с какой мы части начнем !""",
                             attachment=photo1)

        try:
            audio = await audio_uploader.upload(
                file_source="voice/hello.mp3",
                peer_id=message.peer_id,
                title='название'
            )
            await message.answer(attachment=audio)
        except Exception:
            await message("Ошибка аудио:(")

        keyboard = (
            Keyboard(inline=True)
            .add(Text("Начинаем! 💫"), color=KeyboardButtonColor.POSITIVE)
        ).get_json()

        await asyncio.sleep(3)

        await message.answer("Ну как, ты готов взяться за это дело?", keyboard=keyboard)

        mess_key = await bot.state_dispenser.set(message.peer_id, WelcomeStates.VOICE_HELLO_STATE)
        return mess_key
    else:
        return "Ой, ошибка. 🤔 Попробуй еще раз 😊 "

@labeler.message(text=["Начинаем! 💫"], state=WelcomeStates.VOICE_HELLO_STATE)
async def fio_handler(message):
    await message.answer("Как же я рад, что у меня появился такой преемник, как ты! 😊"
                         "\n\nОсталось оформить все документы, чтобы ты мог приступить к работе. Вот тебе анкета")
    await bot.state_dispenser.set(message.peer_id, WelcomeStates.FIO_STATE)
    return "Напиши свое ФИО"

@labeler.message(state=WelcomeStates.FIO_STATE)
async def city_handler(message):
    nowdate = datetime.now()
    newdate = nowdate.strftime("%d/%m/%Y")
    # ctx_storage.set("fio", "Рахметов Вадим Ильшатович")
    user_id = db.get_user_id(message.peer_id)[0][0] - 1
    db.add_user_test_one(message.peer_id, newdate, message.text)
    # вставляем юзера в базу данных и его команду
    db.set_name_and_team(message.peer_id, message.text, (int(user_id) % 10))
    ctx_storage.set(f"{message.peer_id}_team", (int(user_id) % 10))

    await bot.state_dispenser.set(message.peer_id, WelcomeStates.CITY_STATE)
    return "Из какого ты населенного пункта? 🏙️"


# @labeler.message(state=WelcomeStates.CITY_STATE)
# async def class_handler(message):
#     db.set_city(message.peer_id, message.text)
#
#     keyboard = (
#         Keyboard(inline=True)
#         .add(Text("Лицей №86"), color=KeyboardButtonColor.POSITIVE)
#         .row()
#         .add(Text("Школа №4"), color=KeyboardButtonColor.POSITIVE)
#     ).get_json()
#     await bot.state_dispenser.set(message.peer_id, WelcomeStates.CLASS_STATE)
#     messageForReturn = await message.answer("В какой школе ты учишься? 🏫",
#                                             keyboard=keyboard)
#     return messageForReturn


# это была функция про школу, а теперь про город
@labeler.message(state=WelcomeStates.CITY_STATE)
async def end_handler(message):
    db.set_city(message.peer_id, message.text)
    # db.set_school(message.peer_id, message.text)
    # db.set_school_test_one(message.peer_id, message.text)

    # keyboard = (
    #     Keyboard(inline=True)
    #     .add(Text("10"), color=KeyboardButtonColor.POSITIVE)
    #     .add(Text("11"), color=KeyboardButtonColor.POSITIVE)
    # ).get_json()
    await bot.state_dispenser.set(message.peer_id, WelcomeStates.SCHOOL_STATE)
    # messageForReturn = await message.answer("В каком классе ты учишься?",
    #                                         keyboard=keyboard)
    return "В какой школе ты учишься? Напиши полное название 🏫 "

@labeler.message(state=WelcomeStates.SCHOOL_STATE)
async def school_handler(message):
    db.set_school(message.peer_id, message.text)
    await bot.state_dispenser.set(message.peer_id, WelcomeStates.END_STATE_ONE)
    return "В каком классе ты учишься?"

#TODO: Не знаю как сделать симуляцию печати
@labeler.message(state=WelcomeStates.END_STATE_ONE)
async def end_one_handler(message):
    db.set_user_class(message.peer_id, message.text)
    db.set_number_class(message.peer_id, message.text)
    await message.answer("Ура! Твоя анкета заполнена! 💯 Отправляю ее на проверку")
    await asyncio.sleep(3)
    await message.answer("Проверка")
    await asyncio.sleep(3)
    await message.answer("Проверка")
    await asyncio.sleep(3)
    await message.answer("Проверка")
    await asyncio.sleep(4)
    await message.answer("Проверка завершена. Твоя анкета принята! 💯")

    # --------------------------------начинается блок по вопросам мотивации для Димы-----------------------------------------------------------------------------------
    await message.answer("И уже совсем скоро мы начнем нашу игру! 🤩 "
                         "\n\nНо перед этим ответь, пожалуйста, на вопросы 😊")
    await asyncio.sleep(3)
    await bot.state_dispenser.set(message.peer_id, TestOneStates.ONE_STATES)
    keyboard = (
        Keyboard(inline=True)
        .add(Text("От учителя"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("От родителей"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Из интренета"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("От друзей"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Я случайно тут оказался"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()
    mess_key = await message.answer('Откуда ты узнал про игру "Производство будущего"?',
                                    keyboard=keyboard)
    return mess_key


@labeler.message(state=TestOneStates.ONE_STATES)
async def answer_two_handler(message):
    check = {
        "От учителя": 1,
        "От родителей": 2,
        "Из интренета": 3,
        "От друзей": 4,
        "Я случайно тут оказался": 5
    }
    db.set_test_answer_one(message.peer_id, message.text, check[message.text])
    await bot.state_dispenser.set(message.peer_id, TestOneStates.TWO_STATES)
    keyboard = (
        Keyboard(inline=True)
        .add(Text("Физика, математика"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Химия, биология"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Информатика"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Другое"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()
    mess_key = await message.answer("Какой профиль тебе ближе?", keyboard=keyboard)
    return mess_key


@labeler.message(state=TestOneStates.TWO_STATES)
async def answer_three_handler(message):
    check = {
        "Физика, математика": 1,
        "Химия, биология": 2,
        "Информатика": 3,
        "Другое": 4
    }
    db.set_test_answer_two(message.peer_id, message.text, check[message.text])
    await bot.state_dispenser.set(message.peer_id, TestOneStates.THREE_STATES)
    keyboard = (
        Keyboard(inline=True)
        .add(Text("Не знаю ничего"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Знаю немного"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Хорошо разбираюсь"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()
    mess_key = await message.answer("Знаком ли ты с переработкой нефти?", keyboard=keyboard)
    return mess_key


@labeler.message(state=TestOneStates.THREE_STATES)
async def answer_four_handler(message):
    check = {
        "Не знаю ничего": 1,
        "Знаю немного": 2,
        "Хорошо разбираюсь": 3
    }
    db.set_test_answer_three(message.peer_id, message.text, check[message.text])
    await bot.state_dispenser.set(message.peer_id, TestOneStates.TWELVE_STATES)
    keyboard = (
        Keyboard(inline=True)
            .add(Text("Не знаю ничего"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Знаю немного"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Хорошо знаком"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()
    mess_key = await message.answer("Знаком ли ты с «Газпромнефть-ОНПЗ»?", keyboard=keyboard)
    return mess_key


@labeler.message(state=TestOneStates.FOUR_STATES)
async def answer_five_handler(message):
    check = {
        "Не нравится": 1,
        "Отношусь прохладно": 2,
        "Отношусь нормально": 3,
        "Отношусь хорошо": 4,
        "Отношусь отлично": 5
    }
    db.set_test_answer_four(message.peer_id, message.text, check[message.text])
    await bot.state_dispenser.set(message.peer_id, TestOneStates.FIVE_STATES)
    keyboard = (
        Keyboard(inline=True)
        .add(Text("Только бензина"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Бензина и моторного масла"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Резины"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Пластмассы"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Большого количества вещей"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()
    mess_key = await message.answer("Для чего используется нефть? Получения/производства...", keyboard=keyboard)
    return mess_key


@labeler.message(text=["Только бензина",
                       "Бензина и моторного масла",
                       "Резины",
                       "Пластмассы",
                       "Большого количества вещей"],
                 state=TestOneStates.FIVE_STATES)
async def answer_six_handler(message):
    check = {
        "Только бензина": 1,
        "Бензина и моторного масла": 2,
        "Резины": 3,
        "Пластмассы": 4,
        "Большого количества вещей": 5
    }
    db.set_test_answer_five(message.peer_id, message.text, check[message.text])
    await bot.state_dispenser.set(message.peer_id, TestOneStates.SIX_STATES)
    keyboard = (
        Keyboard(inline=True)
        .add(Text("Мне бы хотелось больше узнать о ней"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Мне это интересно"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Возможно"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Нет, это скучная тема"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Нет, это бесполезная информация"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()
    mess_key = await message.answer("Хотелось бы тебе больше узнать о нефтяной отрасли?", keyboard=keyboard)
    return mess_key


@labeler.message(text=["Мне бы хотелось больше узнать о ней",
                       "Мне это интересно",
                       "Возможно",
                       "Нет, это скучная тема",
                       "Нет, это бесполезная информация"],
                 state=TestOneStates.SIX_STATES)
async def answer_seven_handler(message):
    check = {
        "Нет, это бесполезная информация": 1,
        "Нет, это скучная тема": 2,
        "Возможно": 3,
        "Мне это интересно": 4,
        "Мне бы хотелось больше узнать о ней": 5
    }
    db.set_test_answer_six(message.peer_id, message.text, check[message.text])
    await bot.state_dispenser.set(message.peer_id, TestOneStates.SEVEN_STATES)
    keyboard = (
        Keyboard(inline=True)
        .add(Text("Отношусь отлично"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Отношусь хорошо"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Отношусь нормально"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Отношусь прохладно"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Не нравится"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()
    mess_key = await message.answer("Нравятся ли тебе нефтяные компании?", keyboard=keyboard)
    return mess_key


@labeler.message(text=["Не нравится",
                       "Отношусь прохладно",
                       "Отношусь нормально",
                       "Отношусь хорошо",
                       "Отношусь отлично"],
                 state=TestOneStates.SEVEN_STATES)
async def answer_eight_handler(message):
    check = {
        "Не нравится": 1,
        "Отношусь прохладно": 2,
        "Отношусь нормально": 3,
        "Отношусь хорошо": 4,
        "Отношусь отлично": 5
    }
    db.set_test_answer_seven(message.peer_id, message.text, check[message.text])
    await bot.state_dispenser.set(message.peer_id, TestOneStates.EIGHT_STATES)
    keyboard = (
        Keyboard(inline=True)
        .add(Text("Хотел бы стать частью компании"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Мне это интересно"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Не знаю"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Скорее нет"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Категорически нет"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()
    mess_key = await message.answer("Хотелось бы тебе в будущем работать в нефтяной компании?", keyboard=keyboard)
    return mess_key


@labeler.message(text=["Категорически нет",
                       "Скорее нет",
                       "Не знаю",
                       "Мне это интересно",
                       "Хотел бы стать частью компании"],
                 state=TestOneStates.EIGHT_STATES)
async def answer_nine_handler(message):
    check = {
        "Категорически нет": 1,
        "Скорее нет": 2,
        "Не знаю": 3,
        "Мне это интересно": 4,
        "Хотел бы стать частью компании": 5
    }
    db.set_test_answer_eight(message.peer_id, message.text, check[message.text])
    await bot.state_dispenser.set(message.peer_id, TestOneStates.NINE_STATES)
    keyboard = (
        Keyboard(inline=True)
        .add(Text("Да, знаю, и я от них в восторге"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Да, они мне нравятся"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Да, слышал"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Нет, не слышал"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Нет, мне это неинтересно"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()
    mess_key = await message.answer(
        "Слышал ли ты о мероприятиях, которые проводят нефтяные компании?",
        keyboard=keyboard)
    return mess_key


@labeler.message(text=["Да, знаю, и я от них в восторге",
                       "Да, они мне нравятся",
                       "Да, слышал",
                       "Нет, не слышал",
                       "Нет, мне это неинтересно"],
                 state=TestOneStates.NINE_STATES)
async def answer_ten_handler(message):
    check = {
        "Нет, мне это неинтересно": 1,
        "Нет, не слышал": 2,
        "Да, слышал": 3,
        "Да, они мне нравятся": 4,
        "Да, знаю, и я от них в восторге": 5
    }
    db.set_test_answer_nine(message.peer_id, message.text, check[message.text])
    await bot.state_dispenser.set(message.peer_id, TestOneStates.TEN_STATES)
    keyboard = (
        Keyboard(inline=True)
        .add(Text("Отношусь отлично"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Отношусь хорошо"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Отношусь нормально"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Отношусь прохладно"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Не нравится"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()
    mess_key = await message.answer(
        "Нравится ли тебе регион в котором ты живешь? ",
        keyboard=keyboard)
    return mess_key


@labeler.message(text=["Отношусь отлично",
                       "Отношусь хорошо",
                       "Отношусь нормально",
                       "Отношусь прохладно",
                       "Не нравится"],
                 state=TestOneStates.TEN_STATES)
async def answer_eleven_handler(message):
    check = {
        "Не нравится": 1,
        "Отношусь прохладно": 2,
        "Отношусь нормально": 3,
        "Отношусь хорошо": 4,
        "Отношусь отлично": 5
    }
    db.set_test_answer_ten(message.peer_id, message.text, check[message.text])
    await bot.state_dispenser.set(message.peer_id, TestOneStates.ELEVEN_STATES)
    keyboard = (
        Keyboard(inline=True)
        .add(Text("Планирую остаться, работать и жить здесь"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Мне интересно остаться в своем регионе"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Возможно"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Скорее нет"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Категорически нет"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()
    mess_key = await message.answer(
        "Хотел бы ты работать в своем регионе?",
        keyboard=keyboard)
    return mess_key


@labeler.message(text=["Категорически нет",
                       "Скорее нет",
                       "Возможно",
                       "Мне интересно остаться в своем регионе",
                       "Планирую остаться, работать и жить здесь"],
                 state=TestOneStates.ELEVEN_STATES)
async def answer_twelve_handler(message):
    check = {
        "Категорически нет": 1,
        "Скорее нет": 2,
        "Возможно": 3,
        "Мне интересно остаться в своем регионе": 4,
        "Планирую остаться, работать и жить здесь": 5
    }
    db.set_test_answer_eleven(message.peer_id, message.text, check[message.text])
    await bot.state_dispenser.set(message.peer_id, TestOneStates.TWELVE_STATES)
    keyboard = (
        Keyboard(inline=True)
        .add(Text("Люди с отличной интересной работой"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Люди, которые приносят пользу обществу"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Люди, у которых хорошая работа"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Люди, которые просто делают свою работу"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Люди, не достигшие успеха"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()
    mess_key = await message.answer(
        "На твой взгляд люди, работающие в своем регионе это",
        keyboard=keyboard)
    return mess_key


@labeler.message(state=TestOneStates.TWELVE_STATES)
async def answer_end_handler(message):
    check = {
        "Не знаю ничего": 1,
        "Знаю немного": 2,
        "Хорошо знаком": 3
    }
    db.set_test_answer_four(message.peer_id, message.text, check[message.text])
    await message.answer("Спасибо за ответы!"
                         "\nДавай начнем игру 🚀")
    keyboard = (
        Keyboard(inline=True)
        .add(Text("Даа! 😊"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Конечно! 😎"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()
    await bot.state_dispenser.set(message.peer_id, WelcomeStates.END_STATE_TWO)
    messageForReturn = await message.answer("УРА, УРА, УРА! 🎉 Сегодня замечательный день!"
                                            "\n\nДавай не будем терять времени. Готов получить первые инструкции?",
                                            keyboard=keyboard)
    return messageForReturn


@labeler.message(text=["Даа! 😊", "Конечно! 😎"],
                 state=WelcomeStates.END_STATE_TWO)
async def end_button_handler(message):
    await message.answer("Ты же знаешь, что завод огромный")
    # тут будет картинка
    photo1 = await photo_uploader.upload(
        file_source=f"img/Завод.jpg",
        peer_id=message.peer_id,
    )
    await message.answer("Посмотри, как красиво он выглядит", attachment=photo1)

    keyboard = (
        Keyboard(inline=True)
            .add(Text("Вау!"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Красиво!"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()

    await message.answer(
        "Как тебе?" ,
        keyboard=keyboard)

@labeler.message(text=["Вау!", "Красиво!"],state=WelcomeStates.END_STATE_TWO)
async def end_button_handler(message):
    keyboard = (
        Keyboard(inline=True)
            .add(Text("Узнать! 😼"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()

    await message.answer(
        "Именно поэтому завод будут строить несколько команд одновременно. Нам ведь нужно успеть! Давай узнаем, какую часть завода будешь строить ты👷" ,
        keyboard=keyboard)

@labeler.message(text=["Узнать! 😼"],state=WelcomeStates.END_STATE_TWO)
async def end_button_handler(message):
    keyboard = (
        Keyboard(inline=True)
            .add(Text("В какой я команде?"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()

    await message.answer(
        "Теперь нужно начинать строительство. Времени у нас мало⏳, поэтому нужно срочно собрать команду и приступать" ,
        keyboard=keyboard)


@labeler.message(text=["В какой я команде?"], state=WelcomeStates.END_STATE_TWO)
async def my_team_handler(message):
    # user = db.search_user_team(ctx_storage.get(f"{message.peer_id}_team"), ctx_storage.get(f"{message.peer_id}_number"))
    # str = ""
    # count = 0
    # for i in user:
    #     count += 1
    #     str += f"\n{count}: {i[0]}"
    id_team = ctx_storage.get(f"{message.peer_id}_team")

    await message.answer(f'''Ты в команде: "{group_position_name[id_team]}"''')
    # сообзения по командам
    await asyncio.sleep(7)
    await message.answer(first_part_message_one[id_team])

    # Общие сообщения
    await asyncio.sleep(3)
    keyboard = (
        Keyboard(inline=True)
        .add(Text("Я подошел к столу 😊"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()
    message_key = await message.answer(
        "Подойди к столу, чтобы познакомиться с командой и получить следующие инструкции", keyboard=keyboard)
    # ctx_storage.delete(f"{message.peer_id}_team")
    # ctx_storage.delete(f"{message.peer_id}_number")
    await bot.state_dispenser.set(message.peer_id, PartOneStates.START_STATE)
    return message_key
