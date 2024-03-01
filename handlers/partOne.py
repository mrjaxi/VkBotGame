import asyncio

from vkbottle import CtxStorage
from vkbottle import Keyboard, KeyboardButtonColor, \
    Text
import bot
from config import labeler, photo_uploader
from data.keyboard import keyboard_first_part_one, keyboard_first_part_one_answer, keyboard_first_part_two, \
    keyboard_first_part_two_answer, keyboard_first_part_three, keyboard_first_part_three_answer
from data.partOneMessage import first_part_special_one, first_part_special_two, first_part_special_three, \
    first_part_special_four, first_part_special_five, first_part_special_six, first_part_special_seven, \
    first_part_special_eight, first_part_special_nine, first_part_special_ten, first_part_special_eleven, \
    first_part_special_twelve, first_part_special_thirteen, first_part_special_fourteen, first_part_special_fifteen, \
    first_part_special_sixteen,first_part_special_eight_addon, first_part_special_seventeen, first_part_special_eighteen, first_part_special_nineteen, \
    first_part_before_password, first_part_special_two_addon, first_part_special_three_new, first_part_special_pass_new, first_part_special_four_new, \
    first_part_special_six_new, first_part_special_seven_new, first_part_special_twelve_new, \
    first_part_special_pass_new_answer, first_part_special_pass_two_answer
from database.db import Database
from states.mystates import WelcomeStates, PartOneStates, PartTwoStates

ctx_storage = CtxStorage()
db = Database('database.db')


@labeler.message(text=["Я подошел к столу 😊"], state=PartOneStates.START_STATE)
async def part_one_one_handler(message):
    await message.answer("На вашем столе есть чемоданчик для инструментов. Но пока он закрыт 🤔"
                         "\t\tДавай же откроем его!")
    await message.answer("Скорее читайте инструкцию. Я приготовил для вас кое-что интересное 🤩")
    await bot.state_dispenser.set(message.peer_id, PartOneStates.PASSWORD_GAME_STATES)
    return "В инструкции ты найдешь кодовое слово. Напиши его"


@labeler.message(state=PartOneStates.PASSWORD_GAME_STATES)
async def part_one_two_handler(message):
    if message.text == "Нефть" or message.text == "нефть":
        await message.answer("Верно! 😎"
                             "\n\nЯ собрал для вас много всего интересного!"
                             "\n\nИспользуй все, что есть в наборе, и изучай информацию")

        id_team = ctx_storage.get(f"{message.peer_id}_team")
        await message.answer("""Давай посмотрим, что я положил в набор

Набор состоит из следующих элементов:

- основание макета  ⬜
- акриловые конструкции и наклейки
- ножницы ✂️
- ручки 🖊️
- журналы открытий""")

        await message.answer("Давай начнем изучать процессы нефтепереработки!"
                             "\n\nКаждому из вас я оставил «Журнал открытий», чтобы ты мог изучить основные понятия из нефтепереработки"
                             "\n\nПредлагаю тебе открыть журнал и приступить к знакомству с информацией о нефтеперерабатывающей отрасли"
                             "\n\nИзучи информацию внимательно, она скоро пригодится тебе 😊")
        keyboard = (
            Keyboard(inline=True)
            .add(Text("Я прочитал журнал открытий"), color=KeyboardButtonColor.POSITIVE)
        ).get_json()
        await bot.state_dispenser.set(message.peer_id, PartOneStates.END_PASSWORD_GAME_STATES)

        answer_key = await message.answer("У тебя есть 5 минут, чтобы внимательно изучить весь журнал\nНажми на кнопку, когда прочитаешь его", keyboard=keyboard)
        return answer_key
    else:
        await message.answer("Ой, ошибка. 🤔 Попробуй еще раз 😊")

@labeler.message(text=['Я прочитал журнал открытий'], state=PartOneStates.END_PASSWORD_GAME_STATES)
async def read_handler(message):
    await message.answer("А теперь давай проверим, готов ли ты к созданию своего завода? 🤔")
    keyboard = (
        Keyboard(inline=True)
        .add(Text("При первичном"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("При вторичном"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()
    await message.answer("При каком методе переработки нефти происходит изменение химического состава нефти?", keyboard=keyboard)
    await bot.state_dispenser.set(message.peer_id, PartOneStates.ANSWER_ONE_STATES)


@labeler.message(text=["При первичном", "При вторичном"], state=PartOneStates.ANSWER_ONE_STATES)
async def part_one_three_handler(message):
    if message.text == "При первичном":
        await message.answer("Изменение химического состава нефти происходит при вторичных методах нефтепереработки")
    elif message.text == "При вторичном":
        await message.answer(
            "Даа 🤩, изменение химического состава нефти происходит при вторичных методах нефтепереработки")
    db.set_answer_one(message.peer_id, message.text)

    await bot.state_dispenser.set(message.peer_id, PartOneStates.ANSWER_TWO_STATES)
    return "Расположи в правильной последовательности получение продуктов из нефти" \
           "\n1) электрообессоливающая установка - ЭЛОУ" \
           "\n2) установки вторичной переработки нефти" \
           "\n3) установка атмосферно-вакуумной перегонки  - АВТ" \
           "\n4) нефтяная скважина" \
           "\n5) товарный парк"


@labeler.message(state=PartOneStates.ANSWER_TWO_STATES)
async def part_one_four_handler(message):
    if message.text == "41325":
        await message.answer("Даа, все верно 👍")
    else:
        await message.answer(
            "Последовательность получения продуктов из нефти: нефтяная скважина, ЭЛОУ, АВТ, установки вторичной переработки нефти, товарный парк")
    db.set_answer_two(message.peer_id, message.text)

    await bot.state_dispenser.set(message.peer_id, PartOneStates.ANSWER_THREE_STATES)

    keyboard = (
        Keyboard(inline=True)
        .add(Text("метан"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("керосин"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("гудрон"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("бензин"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()
    mess_key = await message.answer(
        "Какая фракция выделяется на вакуумном блоке?",
        keyboard=keyboard)
    return mess_key


@labeler.message(text=["метан", "керосин", "гудрон", "бензин"], state=PartOneStates.ANSWER_THREE_STATES)
async def part_one_five_handler(message):
    if message.text == "гудрон":
        await message.answer("Даа! 🤩 На вакуумном блоке получают гудрон ")
    else:
        await message.answer("На вакуумном блоке получают гудрон")
    db.set_answer_six(message.peer_id, message.text)
    #await asyncio.sleep(2)
    await bot.state_dispenser.set(message.peer_id, PartOneStates.ANSWER_FOUR_STATES)
    keyboard = (
        Keyboard(inline=True)
        .add(Text("для переработки нефти"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("для хранения нефтепродуктов"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("для выделения керосина"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("для транспорта нефтепродуктов"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()
    mess_key = await message.answer(
        "Зачем на НПЗ нужен товарный парк?",
        keyboard=keyboard)
    return mess_key


@labeler.message(text=["для переработки нефти",
                       "для хранения нефтепродуктов",
                       "для выделения керосина",
                       "для транспорта нефтепродуктов"], state=PartOneStates.ANSWER_FOUR_STATES)
async def part_one_six_handler(message):
    if message.text == "для хранения нефтепродуктов":
        await message.answer("Верно! 💫 На НПЗ в товарном парке хранятся нефтепродукты")
    else:
        await message.answer("На НПЗ в товарном парке хранятся нефтепродукты")
    db.set_answer_seven(message.peer_id, message.text)
    await asyncio.sleep(2)
    await bot.state_dispenser.set(message.peer_id, PartOneStates.ANSWER_FIVE_STATES)
    keyboard = (
        Keyboard(inline=True)
        .add(Text("для очистки топлива от сернистых соед."), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("для очистки газов от примесей"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("для очистки промышленной воды"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("для разделения газов на фракции"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()
    mess_key = await message.answer(
        "Для чего нужна установка гидроочистки?",
        keyboard=keyboard)
    return mess_key


@labeler.message(text=["для очистки топлива от сернистых соед.",
                       "для очистки газов от примесей",
                       "для очистки промышленной воды",
                       "для разделения газов на фракции"], state=PartOneStates.ANSWER_FIVE_STATES)
async def part_one_seven_handler(message):
    id_team = ctx_storage.get(f"{message.peer_id}_team")
    if message.text == "для очистки топлива от сернистых соед.":
        await message.answer(
            "Точно! 👏 Установка гидроочистки предназначена для очистки 🧹 топлива от сернистых соединений")
    else:
        await message.answer("Установка гидроочистки предназначена для очистки 🧹 топлива от сернистых соединений")
    db.set_answer_eight(message.peer_id, message.text)
    await asyncio.sleep(2)
    await message.answer("Ну что ж, приступим к самой сборке! ✨")

    # Самые первые сообщения
    await asyncio.sleep(5)
    await message.answer(first_part_special_one[id_team])

    await asyncio.sleep(3)
    photo = await photo_uploader.upload(
        file_source=f"img/part_one_1_{id_team}.png",
        peer_id=message.peer_id,
    )
    await message.answer(first_part_special_two[id_team], attachment=photo)
    await asyncio.sleep(3)

    if id_team == 9:
        photo_9_1 = await photo_uploader.upload(
            file_source=f"img/part_one_1_9_2.png",
            peer_id=message.peer_id,
        )
        await message.answer(attachment=photo_9_1)
        await asyncio.sleep(3)
    if id_team == 1 or id_team == 2 or id_team == 7 or id_team == 9:
        photo_1 = await photo_uploader.upload(
            file_source=f"img/part_one_1_{id_team}_1.png",
            peer_id=message.peer_id,
        )
        await message.answer(first_part_special_two_addon[id_team], attachment=photo_1)
        await asyncio.sleep(3)
    elif id_team == 6:
        await message.answer(first_part_special_two_addon[id_team])
        await asyncio.sleep(3)

    await message.answer(first_part_special_three_new[id_team])
    await asyncio.sleep(10)
    await bot.state_dispenser.set(message.peer_id, PartOneStates.PASS_ONE)
    keyboard = await message.answer(
        "Для продолжения игры убедись, что ты нашел все необходимы части из акрила. Нашел?",
        keyboard=(
            Keyboard(inline=True)
            .add(Text("Да"), color=KeyboardButtonColor.POSITIVE)
        ).get_json()
    )
    return keyboard


# Специальные сообщения---------------------------------------------------


@labeler.message(text=["Да", "да"], state=PartOneStates.PASS_ONE)
async def part_one_pass_one_handler(message):
    id_team = ctx_storage.get(f"{message.peer_id}_team")
    await bot.state_dispenser.set(message.peer_id, PartOneStates.KEYBOARD_ONE)

    # if message.text == "1859":
    #     # Ответ на правильный паролif message.text == "1859":
        # Ответ на правильный парольь
    # await message.answer(first_part_special_pass_new_answer[id_team])
    # await asyncio.sleep(2)

    await message.answer(first_part_special_four_new[id_team])
    await asyncio.sleep(5)

    await message.answer(first_part_special_five[id_team])
    await asyncio.sleep(10)
    # await message.answer(first_part_special_six_new[id_team])
    await message.answer("А еще здесь есть разные наклейки, которые тоже надо будет приклеить. Но о них расскажу чуть позже 🤫")
    await asyncio.sleep(5)
    await message.answer("Сейчас я отправлю твоей команде теорию")

    if id_team == 4 or id_team == 6 or id_team == 7 or id_team == 8:
        photo1 = await photo_uploader.upload(
            file_source=f"img/part_one_3_{id_team}.png",
            peer_id=message.peer_id,
        )
        await message.answer(first_part_special_eight[id_team], attachment=photo1)
        await asyncio.sleep(5)
    else:
        await message.answer(first_part_special_eight[id_team])
        await asyncio.sleep(5)

    if id_team == 5 or id_team == 8:
        photo2 = await photo_uploader.upload(
            file_source=f"img/part_one_4_{id_team}.png",
            peer_id=message.peer_id,
        )
        await message.answer(first_part_special_nine[id_team], attachment=photo2)
        await asyncio.sleep(5)
    else:
        await message.answer(first_part_special_nine[id_team])
        await asyncio.sleep(5)

    await message.answer(first_part_special_ten[id_team])

    await asyncio.sleep(5)
    await message.answer(first_part_special_pass_two_answer[id_team])

    await asyncio.sleep(5)
    if id_team == 5 or id_team == 7:
        photo2 = await photo_uploader.upload(
            file_source=f"img/part_one_4_{id_team}_1.png",
            peer_id=message.peer_id,
        )
        await message.answer(first_part_special_twelve_new[id_team], attachment=photo2)
    else:
        await message.answer(first_part_special_twelve_new[id_team])
    await asyncio.sleep(5)
    if id_team == 3 or id_team == 5 or id_team == 8:
        photo3 = await photo_uploader.upload(
            file_source=f"img/part_one_5_{id_team}.png",
            peer_id=message.peer_id,
        )
        await message.answer(first_part_special_thirteen[id_team], attachment=photo3)
    else:
        await message.answer(first_part_special_thirteen[id_team])

    await asyncio.sleep(5)
    await message.answer("Сейчас тебе пригодится конспект, который создала твоя команда")

    keyboard = await message.answer(first_part_special_fourteen[id_team], keyboard=keyboard_first_part_one[id_team])
    return keyboard


@labeler.message(state=PartOneStates.PASS_TWO)
async def part_one_pass_two_handler(message):
    id_team = ctx_storage.get(f"{message.peer_id}_team")
    if message.text == "Инженер" or message.text == "инженер":

        await message.answer(first_part_special_pass_two_answer[id_team])
        await asyncio.sleep(5)

        # await message.answer(first_part_special_eleven[id_team])

        await asyncio.sleep(5)
        # await asyncio.sleep(3)
        if id_team == 4 or id_team == 6:
            photo2 = await photo_uploader.upload(
                file_source=f"img/part_one_4_{id_team}_1.png",
                peer_id=message.peer_id,
            )
            await message.answer(first_part_special_twelve_new[id_team], attachment=photo2)
        else:
            await message.answer(first_part_special_twelve_new[id_team])

        await asyncio.sleep(5)
        # await asyncio.sleep(3)
        if id_team == 0 or id_team == 2 or id_team == 3 or id_team == 4 or id_team == 6 or id_team == 9:
            photo3 = await photo_uploader.upload(
                file_source=f"img/part_one_5_{id_team}.png",
                peer_id=message.peer_id,
            )
            await message.answer(first_part_special_thirteen[id_team], attachment=photo3)
        else:
            await message.answer(first_part_special_thirteen[id_team])

        await asyncio.sleep(5)
        # await asyncio.sleep(3)
        await bot.state_dispenser.set(message.peer_id, PartOneStates.KEYBOARD_ONE)

    else:
        await message.answer("Ой, ошибка. 🤔 Попробуй еще раз 😊")


@labeler.message(state=PartOneStates.KEYBOARD_ONE)
async def part_one_pass_three_handler(message):
    id_team = ctx_storage.get(f"{message.peer_id}_team")
    db.set_answer_three(message.peer_id, message.text)

    if message.text == keyboard_first_part_one_answer[id_team]:
        await message.answer("Даа, все верно 😊")
    else:
        await message.answer(first_part_special_fifteen[id_team])

    await asyncio.sleep(2)
    await bot.state_dispenser.set(message.peer_id, PartOneStates.KEYBOARD_TWO)
    keyboard = await message.answer(first_part_special_sixteen[id_team], keyboard=keyboard_first_part_two[id_team])
    return keyboard


@labeler.message(state=PartOneStates.KEYBOARD_TWO)
async def part_one_pass_four_handler(message):
    id_team = ctx_storage.get(f"{message.peer_id}_team")
    db.set_answer_four(message.peer_id, message.text)
    if message.text == keyboard_first_part_two_answer[id_team]:
        await message.answer("Даа, верно!")
    else:
        await message.answer(first_part_special_seventeen[id_team])

    await asyncio.sleep(2)
    await bot.state_dispenser.set(message.peer_id, PartOneStates.KEYBOARD_THREE)
    keyboard = await message.answer(first_part_special_eighteen[id_team], keyboard=keyboard_first_part_three[id_team])
    return keyboard


@labeler.message(state=PartOneStates.KEYBOARD_THREE)
async def part_one_pass_five_handler(message):
    id_team = ctx_storage.get(f"{message.peer_id}_team")
    db.set_answer_five(message.peer_id, message.text)
    if message.text == keyboard_first_part_three_answer[id_team]:
        await message.answer("Даа, все верно! 😎")
    else:
        await message.answer(first_part_special_nineteen[id_team])

    await asyncio.sleep(2)

    await message.answer("Ну что ребята, пришло время завершать строительство ")
    await asyncio.sleep(3)
    await message.answer("Вы помните, что нефтеперерабатывающий завод - это единый механизм\n\n"
                         "Посмотрите на общую схему нашего завода, это поможет вам в расстановке ваших объектов")
    await asyncio.sleep(5)
    await message.answer("""Отправляю мини-инструкцию для твоей команды:

1️⃣Подойдите к большому столу и найдите участок с названиями ваших объектов 

2️⃣Перенесите ваши акриловые конструкции на этот участок

3️⃣Убедитесь, что они расположены правильно 

4️⃣Готово! Вы успешно справились 🤩


""")
    await asyncio.sleep(5)
    await bot.state_dispenser.set(message.peer_id, PartOneStates.NEW_PASSWORD_STATES)
    return "Для перехода на следующий этап введи пароль, его сообщит организатор"


@labeler.message(state=PartOneStates.NEW_PASSWORD_STATES)
async def part_one_pass_six_handler(message):
    if message.text == "1955":
        await message.answer(
            "Пароль верный! 😎"
            "\n\nНу что, строительство завершено. Я совсем скоро прилечу к вам и посмотрю, какой у вас получился завод")
        await asyncio.sleep(3)
        # general_scheme
        # photo = await photo_uploader.upload(
        #     file_source=f"img/general_scheme.png",
        #     peer_id=message.peer_id,
        # )
        await message.answer("""Ребята, нам сейчас срочно нужно показать постройки специальной комиссии. Только после этого наш завод будет официально открыт 

Вот по каким правилам будет строиться ваш рассказ 
условия:
1. У вас будете 2 минуты для рассказа
2.  Рассказывает один человек ""Вот моя команда..."" ;остальные члены команды могут подсказывать,помогать показывать
3. Нужно рассказывать громко и чётко ,чтобы тебя услышали участники и организаторы этого мероприятия
4. Во время рассказа нельзя никуда подглядывать. Запрещено читать 



У вас есть немного времени, чтобы подготовиться""")
        await asyncio.sleep(5)
        # id_team = ctx_storage.get(f"{message.peer_id}_team")
        # await message.answer(first_part_before_password[id_team])
        # # await asyncio.sleep(300)
        # await asyncio.sleep(120)
        await message.answer("""Что же должен содержать ваш рассказ?

1. Представить членов своей команды

2. Названия всех объектов,которые вы построили

3. Описание того, для чего нужен объект и как он работает """)
        await asyncio.sleep(10)

        await message.answer("""Ого,вот и подсказка ❗️❗️❗️

Где же ты можешь узнать ответы на свои вопросы?

1. Поискать в предыдущих сообщениях от меня

2. Спросить у экспертов в оранжевой жилетке""")
        await asyncio.sleep(5)
        await message.answer("Ну что же время для подготовки рассказа пошло,начинайте быстрее готовиться. У тебя и твоей команды есть на это всего 5 минут!!!")
        await asyncio.sleep(210)

        await message.answer("-Тик-так...")
        await asyncio.sleep(30)
        await message.answer("-Тик-так...")
        await asyncio.sleep(30)
        await message.answer("-Тик-таааакк❗️❗️❗️")
        await asyncio.sleep(30)
        await message.answer("Когда все команды выступят ,тебе нужно будет ввести пароль, который ты узнаешь от организатора")

        await bot.state_dispenser.set(message.peer_id, PartTwoStates.PASSWORD_START_TWO_STATES)
        return "Для продолжения введите пароль"
    else:
        await message.answer("Ой, ошибка. 🤔 Попробуй еще раз 😊")
