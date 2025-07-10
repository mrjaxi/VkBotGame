import asyncio

from vkbottle import CtxStorage
from vkbottle import Keyboard, KeyboardButtonColor, \
    Text
import bot
from config import labeler, photo_uploader, audio_uploader, excel_uploader
from data.group import team_way
from data.partTwoMessage import second_part_one, second_part_rooms, second_part_ten, second_part_middle_two, \
    second_part_three, second_part_four, second_part_five, \
    second_part_six, second_part_seven, second_part_middle_five, second_part_eight, second_part_nine, second_part_eleven
from database.aiodb import user_info
from database.settings import settingsAio

from database.db import Database
from states.mystates import PartTwoStates, TestTwoStates, PartThreeStates

ctx_storage = CtxStorage()
db = Database('database.db')


@labeler.message(state=PartTwoStates.PASSWORD_START_TWO_STATES)
async def part_two_one_handler(message):
    if message.text == "Завод" or message.text == "завод":

        await message.answer("Верно! 😎"
                             "\n\nТы молодец!  Поздравляю, ты построил завод😏"
                             '\n\nТы прошел эту часть "Технология" и теперь получи наклейку')

        await asyncio.sleep(5)

        await bot.state_dispenser.set(message.peer_id, PartTwoStates.PASSWORD_START_THREE_STATES)
        return "Для перехода к следующему этапу введи пароль, а его можно узнать у специалистов оранжевой жилетке"
    else:
        await message.answer("Ой, ошибка. 🤔 Попробуй еще раз 😊")


@labeler.message(state=PartTwoStates.PASSWORD_START_THREE_STATES)
async def part_three_three_handler(message):
    if message.text == "Карьера" or message.text == "карьера":
        photo1 = await photo_uploader.upload(
            file_source=f"img/carier_part_2.png",
            peer_id=message.peer_id,
        )
        await message.answer('''Пароль подходит! 🤩

Часть со стройкой пройдена! 

А сейчас будет еще одна из интересных частей,и это "Карьера"''', attachment=photo1)

        try:
            audio = await audio_uploader.upload(
                file_source="voice/2-часть.mp3",
                peer_id=message.peer_id,
                title='название1'
            )
            await message.answer(attachment=audio)
        except Exception:
            await message("Ошибка аудио:(")

        await asyncio.sleep(5)

        await message.answer("Специально для тебя я приготовил коробочку с твоим персонажем ")

        await asyncio.sleep(5)

        await message.answer("""У тебя в коробочке есть человечек

Давай украсим его наклейками,которые лежат у тебя в чемоданчике""")

        await asyncio.sleep(5)

        await bot.state_dispenser.set(message.peer_id, PartTwoStates.NFC_ID)
        return """А теперь тебе нужно зарегистрировать человечка

Напиши номер человечка под QR-кодом и напиши его мне скорееее, а я расскажу много интересного 
"""

    else:
        await message.answer("Ой, ошибка. 🤔 Попробуй еще раз 😊")


@labeler.message(command="check2")
async def check2(message):
    print(db.get_user_id(message.peer_id))
    user_id = db.get_user_id(message.peer_id)[0][0]
    if bool(user_id):
        ctx_storage.set(f"{message.peer_id}_team", (int(user_id) % 10) + 5)

    await bot.state_dispenser.set(message.peer_id, PartTwoStates.NFC_ID)
    return f"Продолжайте {ctx_storage.get(f'{message.peer_id}_team')}"


@labeler.message(text=["установка", "Установка"], state=PartTwoStates.NFC_ID)
async def part_two_two_pass_handler(message):
    id_team = ctx_storage.get(f"{message.peer_id}_team")
    ctx_storage.set(f"{message.peer_id}_position_check", 1)
    await bot.state_dispenser.set(message.peer_id, PartTwoStates.NFC_GET_ONE)
    await message.answer("Давай отправимся в те времена, когда твой персонаж учился в школе ")
    await asyncio.sleep(3)
    return second_part_one[id_team]


@labeler.message(state=PartTwoStates.NFC_ID)
async def part_two_two_handler(message):
    if db.nfc_exists(message.text):
        id_team = ctx_storage.get(f"{message.peer_id}_team")
        ctx_storage.set(f"{message.peer_id}_position_check", 0)
        ctx_storage.set(f"{message.peer_id}_nfc", message.text)
        db.set_nfc(message.peer_id, message.text)
        await message.answer('Давай отправимся в те времена, когда твой персонаж учился в школе ')

        await asyncio.sleep(3)
        # await asyncio.sleep(3)
        await message.answer('''Приложи своего персонажа к считывателю куар кодов на участке "Школа, Дом творчества"
Жди сообщений от меня''')
        check = False
        my_position = team_way[id_team].split('-')[0]
        print(my_position)
        while not check:
            if ctx_storage.get(f"{message.peer_id}_position_check") == 1:
                break

            if bool(settingsAio.mass):
                for mas in settingsAio.mass:
                    if mas[1] == message.text and mas[2] == my_position:
                        check = True
                        break
            if check:
                break

            if not settingsAio.aiocheck:
                break

            await asyncio.sleep(2)

        if check:
            await bot.state_dispenser.set(message.peer_id, PartTwoStates.NFC_GET_ONE)
            return second_part_one[id_team]
    else:
        await message.answer("Вы ввели неправильный код")


@labeler.message(command="check1")
async def check1(message):
    user_id = db.get_user_id(message.peer_id)[0][0]
    if bool(user_id):
        ctx_storage.set(f"{message.peer_id}_team", (int(user_id) % 10))
    await bot.state_dispenser.set(message.peer_id, PartTwoStates.NFC_GET_ONE)
    return "Продолжайте"


@labeler.message(text=["реактор", "Реактор"], state=PartTwoStates.NFC_GET_ONE)
async def part_two_three_pass_handler(message):
    ctx_storage.set(f"{message.peer_id}_position_check", 1)
    id_team = ctx_storage.get(f"{message.peer_id}_team")
    # await bot.state_dispenser.set(message.peer_id, PartTwoStates.NFC_GET_TWO)
    await bot.state_dispenser.set(message.peer_id, PartTwoStates.NFC_DIPLOM)
    # await message.answer("Ура! Ты находишься на обучении!")
    # try:
    #     audio = await audio_uploader.upload(
    #         file_source="voice/univer.mp3",

    await message.answer(
        "В школьные годы у твоего персонажа часто появлялся вопрос, кем он станет, когда вырастет? Он думал, в какое учебное заведение ему пойти учиться"
        "\n\nПри этом он проходил профориентационные программы, чтобы понять, в каком направлении ему двигаться")
    await message.answer(10)
    await message.answer("Ура! Ты находишься на обучении!")
    await asyncio.sleep(2)
    await message.answer(second_part_middle_two[id_team])
    await asyncio.sleep(5)
    # await message.answer(second_part_two[id_team])

    await message.answer(
        "Поздравляем! Ты сейчас находишься на вручении дипломов! Твой персонаж успешно окончил учебное заведение 🧑‍🎓")
    await asyncio.sleep(5)
    await message.answer(
        "Ты отлично учился,проявлял внимание на профильных предметах и показывал себя только с хорошей стороны.")
    await asyncio.sleep(5)
    return "Кроме учебы, ты смог уделить время и своим навыкам, которые идут с тобой со школы. Иии... Поэтомууу... Именно тебя позвали на нефтеперерабатывающий завод !"


@labeler.message(state=PartTwoStates.NFC_GET_ONE)
async def part_two_three_handler(message):
    ctx_storage.set(f"{message.peer_id}_position_check", 0)
    id_team = ctx_storage.get(f"{message.peer_id}_team")
    db.set_subject(message.peer_id, message.text)
    await asyncio.sleep(1)
    await message.answer(
        "В школьные годы у твоего персонажа часто появлялся вопрос, кем он станет, когда вырастет? Он думал, в какое учебное заведение ему пойти учиться"
        "\n\nПри этом он проходил профориентационные программы, чтобы понять, в каком направлении ему двигаться")

    await asyncio.sleep(10)
    await message.answer(
        'Прошло какое-то время, и вот он уже поступил и начал учиться в университете. Давай же узнаем, что было дальше'
        ' \n\nПодойди к участку "Университет, Колледж" и приложи своего человечка к специальному блоку')

    check = False
    my_position = team_way[id_team].split('-')[1]
    while not check:
        # card = await user_info(ctx_storage.get(f"{message.peer_id}_nfc"))
        if ctx_storage.get(f"{message.peer_id}_position_check") == 1:
            break
        if bool(settingsAio.mass):
            for mas in settingsAio.mass:
                if mas[1] == ctx_storage.get(f"{message.peer_id}_nfc") and mas[2] == my_position:
                    check = True
                    break
        if check:
            break

        if not settingsAio.aiocheck:
            break

        await asyncio.sleep(2)

    if check:
        # await bot.state_dispenser.set(message.peer_id, PartTwoStates.NFC_GET_TWO)
        await bot.state_dispenser.set(message.peer_id, PartTwoStates.NFC_DIPLOM)
        await message.answer("Ура! Ты находишься на обучении!")
        await asyncio.sleep(2)
        # try:
        #     audio = await audio_uploader.upload(
        #         file_source="voice/univer.mp3",
        #         peer_id=message.peer_id,
        #         title='название'
        #     )
        #     await message.answer(attachment=audio)
        # except Exception:
        #     await message("Ошибка аудио:(")
        await message.answer(second_part_middle_two[id_team])
        await asyncio.sleep(10)
        # await message.answer(second_part_two[id_team])

        await message.answer(
            "Поздравляем! Ты сейчас находишься на вручении дипломов! Твой персонаж успешно окончил учебное заведение 🧑‍🎓")
        await asyncio.sleep(5)
        await message.answer(
            "Ты отлично учился,проявлял внимание на профильных предметах и показывал себя только с хорошей стороны.")
        await asyncio.sleep(5)
        await message.answer(
            "Кроме учебы, ты смог уделить время и своим навыкам, которые идут с тобой со школы. Иии... Поэтомууу... Именно тебя позвали на нефтеперерабатывающий завод !")
        await asyncio.sleep(5)

        keyboard = await message.answer(
            '''А теперь мы узнаем куда именно ты отправишься, мне стало интересно даже самому🤯''',
            keyboard=(
                Keyboard(inline=True)
                .add(Text("Готов!"), color=KeyboardButtonColor.POSITIVE)
            ).get_json()
        )

        return keyboard


@labeler.message(text=["куда", "Куда"], state=PartTwoStates.NFC_DIPLOM)
async def open_diplom_pass_handler(message):
    ctx_storage.set(f"{message.peer_id}_position_check", 1)

    await bot.state_dispenser.set(message.peer_id, PartTwoStates.NFC_GET_TWO)
    id_team = ctx_storage.get(f"{message.peer_id}_team")
    await message.answer('''Урааа,я тебя поздравляю, твой персонаж получил работу и сейчассс ты узнаешь гдеее...
🤩🤩🤩''')
    await asyncio.sleep(3)
    await message.answer(second_part_rooms[id_team])
    await asyncio.sleep(2)
    return second_part_three[id_team]


@labeler.message(text=["Готов!"], state=PartTwoStates.NFC_DIPLOM)
async def open_diplom_handler(message):
    id_team = ctx_storage.get(f"{message.peer_id}_team")
    ctx_storage.set(f"{message.peer_id}_position_check", 0)

    await message.answer('Поднеси своей человечка с куар кодом к считывателю на участке "Офис компании" и скорее давай узнай куда твой персонаж пойдёт работать')

    check = False
    my_position = team_way[id_team].split('-')[2]

    while not check:
        # card = await user_info(ctx_storage.get(f"{message.peer_id}_nfc"))
        if ctx_storage.get(f"{message.peer_id}_position_check") == 1:
            break
        if bool(settingsAio.mass):
            for mas in settingsAio.mass:
                print(my_position, ctx_storage.get(f"{message.peer_id}_nfc"), mas)
                if mas[1] == ctx_storage.get(f"{message.peer_id}_nfc") and mas[2] == my_position:
                    check = True
                    break
        if check:
            break

        if not settingsAio.aiocheck:
            break

        await asyncio.sleep(2)

    if check:
        await bot.state_dispenser.set(message.peer_id, PartTwoStates.NFC_GET_TWO)
        await message.answer('''Урааа,я тебя поздравляю, твой персонаж получил работу и сейчассс ты узнаешь гдеее...
    🤩🤩🤩''')
        await asyncio.sleep(5)
        keyboard = await message.answer(
            second_part_rooms[id_team],
            keyboard=(
                Keyboard(inline=True)
                .add(Text("Да 😎"), color=KeyboardButtonColor.POSITIVE)
            ).get_json()
        )
        return keyboard


@labeler.message(text=["Аппарат", "аппарат"], state=PartTwoStates.NFC_GET_TWO)
async def part_two_four_pass_handler(message):
    ctx_storage.set(f"{message.peer_id}_position_check", 1)
    id_team = ctx_storage.get(f"{message.peer_id}_team")
    await bot.state_dispenser.set(message.peer_id, PartTwoStates.NFC_GET_THREE)
    await message.answer(second_part_four[id_team])
    await asyncio.sleep(3)

    await message.answer(second_part_five[id_team])

    await asyncio.sleep(5)
    await message.answer("Ты усердно работал ,показывал себя с лучшей стороны,выполнял все намечанные показатели.")

    await asyncio.sleep(3)
    await message.answer(second_part_middle_five[id_team])

    await asyncio.sleep(5)
    await message.answer("Тебе наверное хочется все-таки стать главнее? Тогда может быть повысим разряд?")

    await asyncio.sleep(3)
    await message.answer(
        '''Так, где же можно повысить свой разряд? Дай мне подумать...\n\nАааа, дааа, я вспомнил!!! Это же можно сделать в учебном центре ОНПЗ🤩 Хочу тебе даже сказать по секрету,что у них есть такая прикольная программа и называется она даже по-необычному "Три рубежа". Там ведь даже есть много мероприятий и много-много интересной теории,которые помогают сотрудникам повышать свои знания и умения на заводе.''')

    await asyncio.sleep(10)
    await message.answer(
        '''Твой персонаж умело продемонстрироовал свои знания старшим коллегам и было принято решение по результатам повысить тебе разряд''')
    await asyncio.sleep(5)
    return '''Для повышения разряда приложи своего персонажа к куар код считывателю и скорееее узнай какой он разряд все-таки получил🤩'''


@labeler.message(text=["Да 😎"], state=PartTwoStates.NFC_GET_TWO)
async def part_two_four_handler(message):
    ctx_storage.set(f"{message.peer_id}_position_check", 0)
    id_team = ctx_storage.get(f"{message.peer_id}_team")

    await message.answer(second_part_three[id_team])

    check = False
    my_position = team_way[id_team].split('-')[3]
    while not check:
        # card = await user_info(ctx_storage.get(f"{message.peer_id}_nfc"))
        if ctx_storage.get(f"{message.peer_id}_position_check") == 1:
            break
        if bool(settingsAio.mass):
            for mas in settingsAio.mass:
                if mas[1] == ctx_storage.get(f"{message.peer_id}_nfc") and mas[2] == my_position:
                    check = True
                    break
        if check:
            break

        if not settingsAio.aiocheck:
            break

        await asyncio.sleep(2)

    if check:
        await bot.state_dispenser.set(message.peer_id, PartTwoStates.NFC_GET_THREE)
        await message.answer(second_part_four[id_team])
        await asyncio.sleep(3)

        await message.answer(second_part_five[id_team])

        await asyncio.sleep(5)
        await message.answer("Ты усердно работал ,показывал себя с лучшей стороны,выполнял все намечанные показатели.")

        await asyncio.sleep(3)
        await message.answer(second_part_middle_five[id_team])

        await asyncio.sleep(5)
        await message.answer("Тебе наверное хочется все-таки стать главнее? Тогда может быть повысим разряд?")

        await asyncio.sleep(3)
        await message.answer(
            '''Так, где же можно повысить свой разряд? Дай мне подумать...\n\nАааа, дааа, я вспомнил!!! Это же можно сделать в учебном центре ОНПЗ🤩 Хочу тебе даже сказать по секрету,что у них есть такая прикольная программа и называется она даже по-необычному "Три рубежа". Там ведь даже есть много мероприятий и много-много интересной теории,которые помогают сотрудникам повышать свои знания и умения на заводе.''')

        await asyncio.sleep(10)
        keyboard = await message.answer(
            '''Твой персонаж умело продемонстрироовал свои знания старшим коллегам и было принято решение по результатам повысить тебе разряд. Готов?😏''',
            keyboard=(
                    Keyboard(inline=True)
                    .add(Text("Конечно 😃"), color=KeyboardButtonColor.POSITIVE)
                ).get_json()
            )
        return keyboard


@labeler.message(text=["Разряд", "разряд"], state=PartTwoStates.NFC_GET_THREE)
async def part_two_five_pass_handler(message):
    ctx_storage.set(f"{message.peer_id}_position_check", 1)
    id_team = ctx_storage.get(f"{message.peer_id}_team")
    await bot.state_dispenser.set(message.peer_id, PartThreeStates.PASS)
    await message.answer(second_part_six[id_team])
    await asyncio.sleep(5)
    await message.answer(
        "Ну вот ты и узнал какой разряд получил твой персонаж! Пожелаю ему удачи в дальнейшем карьерном росте🤩")
    await asyncio.sleep(3)
    # await asyncio.sleep(3)

    await message.answer('''Ребята, нам сейчас нужно будет рассказать за круглым столом свой увлекательный рассказ про своего персонажа

    Вот по каким правилам будет строиться ваш рассказ 
    условия:
    1. У вас будете 2 минуты для рассказа
    2. Рассказывает один человек ""Вот моя команда..."" ;остальные члены команды могут подсказывать,помогать показывать
    3. Нужно рассказывать громко и чётко ,чтобы тебя услышали участники и организаторы этого мероприятия
    4. Во время рассказа нельзя никуда подглядывать. Запрещено читать 



    У вас есть немного времени, чтобы подготовиться"''')
    await asyncio.sleep(5)

    await message.answer("""Что же должен содержать ваш рассказ?

    1. Представить членов своей команды

    2. Хобби и увлечения, кроме учебы

    3. Описание того, кем работает твой персонаж""")
    await asyncio.sleep(10)

    await message.answer("""Ого,вот и подсказка ❗️❗️❗️

    Где же ты можешь узнать ответы на свои вопросы?

    1. Поискать в предыдущих сообщениях от меня

    2. Спросить у экспертов в оранжевой жилетке""")
    await asyncio.sleep(10)
    await message.answer("Ну что же время для подготовки рассказа пошло, начинайте быстрее готовиться. У тебя и твоей команды есть на это всего 5 минут!!!")
    await asyncio.sleep(255)

    await message.answer("-Тик-так...")
    await asyncio.sleep(15)
    await message.answer("-Тик-так...")
    await asyncio.sleep(15)
    await message.answer("-Тик-таааакк❗️❗️❗️")
    await asyncio.sleep(15)
    # TODO: Жду третьей части
    return "Когда все команды выступят, тебе нужно будет ввести пароль, который ты узнаешь от организатора"


@labeler.message(text=["Конечно 😃"], state=PartTwoStates.NFC_GET_THREE)
async def part_two_five_handler(message):
    ctx_storage.set(f"{message.peer_id}_position_check", 0)
    id_team = ctx_storage.get(f"{message.peer_id}_team")
    await message.answer('''Для повышения разряда приложи своего персонажа к куар код считывателю и скорееее узнай какой он разряд все-таки получил🤩''')
    check = False
    my_position = team_way[id_team].split('-')[4]
    while not check or ctx_storage.get(f"{message.peer_id}_position_check") == 0:
        # card = await user_info(ctx_storage.get(f"{message.peer_id}_nfc"))
        if ctx_storage.get(f"{message.peer_id}_position_check") == 1:
            break
        if bool(settingsAio.mass):
            for mas in settingsAio.mass:
                if mas[1] == ctx_storage.get(f"{message.peer_id}_nfc") and mas[2] == my_position:
                    check = True
                    break
        if check:
            break

        if not settingsAio.aiocheck:
            break

        await asyncio.sleep(2)

    if check:
        await bot.state_dispenser.set(message.peer_id, PartThreeStates.PASS)
        await message.answer(second_part_six[id_team])
        await asyncio.sleep(5)
        await message.answer(
            "Ну вот ты и узнал какой разряд получил твой персонаж! Пожелаю ему удачи в дальнейшем карьерном росте🤩")
        await asyncio.sleep(3)
        # await asyncio.sleep(3)

        await message.answer('''Ребята, нам сейчас нужно будет рассказать за круглым столом свой увлекательный рассказ про своего персонажа

Вот по каким правилам будет строиться ваш рассказ 
условия:
1. У вас будете 2 минуты для рассказа
2. Рассказывает один человек ""Вот моя команда..."" ;остальные члены команды могут подсказывать,помогать показывать
3. Нужно рассказывать громко и чётко ,чтобы тебя услышали участники и организаторы этого мероприятия
4. Во время рассказа нельзя никуда подглядывать. Запрещено читать 



У вас есть немного времени, чтобы подготовиться"''')
        await asyncio.sleep(5)

        await message.answer("""Что же должен содержать ваш рассказ?

1. Представить членов своей команды

2. Хобби и увлечения, кроме учебы

3. Описание того, кем работает твой персонаж""")
        await asyncio.sleep(10)

        await message.answer("""Ого,вот и подсказка ❗️❗️❗️

Где же ты можешь узнать ответы на свои вопросы?

1. Поискать в предыдущих сообщениях от меня

2. Спросить у экспертов в оранжевой жилетке""")
        await asyncio.sleep(10)
        await message.answer("Ну что же время для подготовки рассказа пошло, начинайте быстрее готовиться. У тебя и твоей команды есть на это всего 5 минут!!!")
        await asyncio.sleep(255)

        await message.answer("-Тик-так...")
        await asyncio.sleep(15)
        await message.answer("-Тик-так...")
        await asyncio.sleep(15)
        await message.answer("-Тик-таааакк❗️❗️❗️")
        await asyncio.sleep(15)
        # TODO: Жду третьей части
        return "Когда все команды выступят, тебе нужно будет ввести пароль, который ты узнаешь от организатора"


@labeler.message(text=["Поехали"], state=PartTwoStates.NFC_GET_FOUR)
async def part_two_six_handler(message):
    ctx_storage.set(f"{message.peer_id}_position_check", 0)
    id_team = ctx_storage.get(f"{message.peer_id}_team")
    await message.answer(second_part_seven[id_team])
    check = False
    my_position = team_way[id_team].split('-')[4]
    while not check or ctx_storage.get(f"{message.peer_id}_position_check") == 0:
        # card = await user_info(ctx_storage.get(f"{message.peer_id}_nfc"))
        if ctx_storage.get(f"{message.peer_id}_position_check") == 1:
            break
        if bool(settingsAio.mass):
            for mas in settingsAio.mass:
                if mas[1] == ctx_storage.get(f"{message.peer_id}_nfc") and mas[2] == my_position:
                    check = True
                    break
        if check:
            break

        if not settingsAio.aiocheck:
            break
        await asyncio.sleep(2)

    if check:
        await message.answer(second_part_eight[id_team])

        await asyncio.sleep(5)
        await message.answer(second_part_nine[id_team])

        await asyncio.sleep(50)
        # await asyncio.sleep(5)
        await message.answer("Так, а куда же ты отправишься дальше? Дай-ка подумать"
                             "\n\nХотя нет, это было заключительное перемещение по НПЗ"
                             "\n\nПолучается, что этот этап пройден! Ты молодец! 🎉😊")
        await asyncio.sleep(2)
        # ctx_storage.delete(f"{message.peer_id}_team")
        # ctx_storage.delete(f"{message.peer_id}_number")
        # ctx_storage.delete(f"{message.peer_id}_position_check")
        # ctx_storage.delete(f"{message.peer_id}_nfc")
        await bot.state_dispenser.set(message.peer_id, PartThreeStates.PASS)
        return "Для перехода на следующий этап введи пароль"


@labeler.message(text="check1")
async def check(message):
    user_id = db.get_user_id(message.peer_id)[0][0]
    if bool(user_id):
        ctx_storage.set(f"{message.peer_id}_team", (int(user_id) % 10))
    await bot.state_dispenser.set(message.peer_id, PartTwoStates.NFC_GET_FOUR)
    return "Продолжайте"


@labeler.message(text=["Печь", "печь"], state=PartTwoStates.NFC_GET_FOUR)
async def part_two_six_pass_handler(message):
    ctx_storage.set(f"{message.peer_id}_position_check", 1)
    id_team = ctx_storage.get(f"{message.peer_id}_team")
    db.set_status(message.peer_id)
    await message.answer(second_part_eight[id_team])

    await asyncio.sleep(5)
    await message.answer(second_part_nine[id_team])

    await asyncio.sleep(50)
    # await asyncio.sleep(5)
    await message.answer("Так, а куда же ты отправишься дальше? Дай-ка подумать\n\n"
                         "Хотя нет, это было заключительное перемещение по НПЗ"
                         "\n\nПолучается, что этот этап пройден! Ты молодец! 🎉😊")
    # ctx_storage.delete(f"{message.peer_id}_team")
    # ctx_storage.delete(f"{message.peer_id}_number")
    # ctx_storage.delete(f"{message.peer_id}_position_check")
    # ctx_storage.delete(f"{message.peer_id}_nfc")
    await asyncio.sleep(2)
    await bot.state_dispenser.set(message.peer_id, PartThreeStates.PASS)
    return "Для перехода на следующий этап введи пароль"


@labeler.message(state=PartThreeStates.PASS)
async def part_three_one(message):
    if message.text == "Вызов" or message.text == "вызов":
        id_team = ctx_storage.get(f"{message.peer_id}_team")
        photo1 = await photo_uploader.upload(
            file_source=f"img/ЧАСТЬ 3 - ВЫЗОВЫ.png",
            peer_id=message.peer_id,
        )
        await message.answer('''Пароль подходит! 🤩

Часть с карьерой пройдена!

А сейчас будет еще одна из интересных частей, и это "Вызовы"
''', attachment=photo1)
        await asyncio.sleep(2)
        try:
            audio = await audio_uploader.upload(
                file_source="voice/3-часть.mp3",
                peer_id=message.peer_id,
                title='название'
            )
            await message.answer(attachment=audio)
        except Exception:
            await message("Ошибка аудио:(")
        await asyncio.sleep(5)

        await message.answer('''Ты уже создал завод и даже смог подняться по карьерной лестнице. Завод, как и любое большое предприятие, требует постоянной модернизации, чтобы идти в ногу с современными технологиями!

Третий этап нашей игры будет посвящен трендам и вызовам отрасли 😎

Но что же такое эти тренды и вызовы? 🤔

Тренд - это современная тенденция развития и изменения предприятиям, и любому заводу нужно ей следовать, чтобы оставаться востребаванным! А вызовами называются задачи промышленности, решения которых позволяют предприятию достигать поставленных целей и совершенствоваться! 
''')
        await asyncio.sleep(5)

        await message.answer("Сегодня именно тебе предстоит следовать трендам и принимать вызовы промышленности! Вместе с командой вы построите вспомогательные макеты, которые ответят поставленным задачам!")
        await asyncio.sleep(5)

        await message.answer("Давай же скорее приступим к самой творческой и занимательной части нашей игры!")

        await asyncio.sleep(3)
        await message.answer(second_part_ten[id_team])

        #TODO: Третья часть сделал 164 строчку
        await asyncio.sleep(5)
        await message.answer(second_part_eleven[id_team])

        await asyncio.sleep(5)
        await message.answer("Ну что? Возникли идеи? Давайте приступим к созданию вашего творческого объекта, подготовьте бумагу, картон, фломастеры, ножницы, скотч и вашу фантазию и воплотите вашу идею в реальность на макете! ✨")

        await asyncio.sleep(10)
        await message.answer("У вас есть немного времени, чтобы подготовиться к рассказу о вашем объекте!")

        await message.answer("""Что же должен содержать ваш рассказ?

        1. Представить членов своей команды

        2. Хобби и увлечения, кроме учебы

        3. Описание того, кем работает твой персонаж""")
        await asyncio.sleep(5)

        await message.answer("""Ого,вот и подсказка ❗️❗️❗️

        Где же ты можешь узнать ответы на свои вопросы?

        1. Поискать в предыдущих сообщениях от меня

        2. Спросить у экспертов в оранжевой жилетке""")
        await asyncio.sleep(5)
        await message.answer("Ну что же время для подготовки рассказа пошло, начинайте быстрее готовиться. У тебя и твоей команды есть на это всего 5 минут!!!")
        await asyncio.sleep(255)

        await message.answer("-Тик-так...")
        await asyncio.sleep(15)
        await message.answer("-Тик-так...")
        await asyncio.sleep(15)
        await message.answer("-Тик-таааакк❗️❗️❗️")
        await asyncio.sleep(15)
        await bot.state_dispenser.set(message.peer_id, PartThreeStates.PASS_ONE)

        return "Когда все команды выступят ,тебе нужно будет ввести пароль, который ты узнаешь от организатора"
    else:
        await message.answer("Ой, ошибка. 🤔 Попробуй еще раз 😊")


@labeler.message(state=PartThreeStates.PASS_ONE)
async def part_three_two(message):
    if message.text == "Анкета" or message.text == "анкета":
        await message.answer('''Так, а куда же ты отправишься дальше? Дай-ка подумать

Хотя нет, это было заключительное перемещение по НПЗ

Получается, что этот этап пройден! Ты молодец! 🎉😊''')
        await asyncio.sleep(5)
        await message.answer("Сейчас я отправлю тебе несколько вопросов об игре 😊")
        await bot.state_dispenser.set(message.peer_id, TestTwoStates.ONE_STATES)
        keyboard = (
            Keyboard(inline=True)
            .add(Text("Игра была превосходной"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Игра была хорошей"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Затрудняюсь ответить"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Отношусь нейтрально"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Не понравилась"), color=KeyboardButtonColor.POSITIVE)
        ).get_json()
        mess_key = await message.answer("Понравилась ли тебе игра?",
                                        keyboard=keyboard)
        return mess_key
    else:
        await message.answer("Ой, ошибка. 🤔 Попробуй еще раз 😊")

@labeler.message(text=["Игра была превосходной",
                       "Игра была хорошей",
                       "Затрудняюсь ответить",
                       "Отношусь нейтрально",
                       "Не понравилась"], state=TestTwoStates.ONE_STATES)
async def answer_test_two_handler(message):
    check = {
        "Не понравилась": 1,
        "Отношусь нейтрально": 2,
        "Затрудняюсь ответить": 3,
        "Игра была хорошей": 4,
        "Игра была превосходной": 5
    }
    db.set_end_answer_one(message.peer_id, message.text, check[message.text])
    await bot.state_dispenser.set(message.peer_id, TestTwoStates.TWO_STATES)
    keyboard = (
        Keyboard(inline=True)
        .add(Text("Поделюсь впечатлениями с ними"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Точно расскажу"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Не знаю"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Возможно"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Скорее нет"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()
    mess_key = await message.answer("Расскажешь о программе своим друзьям?", keyboard=keyboard)
    return mess_key


@labeler.message(text=["Поделюсь впечатлениями с ними",
                       "Точно расскажу",
                       "Не знаю",
                       "Возможно",
                       "Скорее нет"],
                 state=TestTwoStates.TWO_STATES)
async def answer_test_three_handler(message):
    check = {
        "Скорее нет": 1,
        "Возможно": 2,
        "Не знаю": 3,
        "Точно расскажу": 4,
        "Поделюсь впечатлениями с ними": 5
    }
    db.set_end_answer_two(message.peer_id, message.text, check[message.text])
    await bot.state_dispenser.set(message.peer_id, TestTwoStates.THREE_STATES)
    keyboard = (
        Keyboard(inline=True)
        .add(Text("Промышленность суперинтересна и полезна"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Промышленность – это интересно"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Никак не изменилось"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Промышленность – это скучная тема"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Промышленность сложная и неинтересная"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()
    mess_key = await message.answer("Как изменилось твое отношение к промышленности?", keyboard=keyboard)
    return mess_key


@labeler.message(text=["Промышленность сложная и неинтересная",
                       "Промышленность – это скучная тема",
                       "Никак не изменилось",
                       "Промышленность – это интересно",
                       "Промышленность суперинтересна и полезна"],
                 state=TestTwoStates.THREE_STATES)
async def answer_four_handler(message):
    check = {
        "Промышленность сложная и неинтересная": 1,
        "Промышленность – это скучная тема": 2,
        "Никак не изменилось": 3,
        "Промышленность – это интересно": 4,
        "Промышленность суперинтересна и полезна": 5
    }
    db.set_end_answer_three(message.peer_id, message.text, check[message.text])
    await bot.state_dispenser.set(message.peer_id, TestTwoStates.FOUR_STATES)
    keyboard = (
        Keyboard(inline=True)
        .add(Text("Человечки крутые!"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Человечки мне понравились"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Человечки были интересными"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Человечки были скучными"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Человечки мне не понравились"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()
    mess_key = await message.answer(
        "Понравились ли тебе «человечки», которыми ты пользовался во время прохождения игры?", keyboard=keyboard)
    return mess_key


@labeler.message(text=["Человечки крутые!",
                       "Человечки мне понравились",
                       "Человечки были интересными",
                       "Человечки были скучными",
                       "Человечки мне не понравились"],
                 state=TestTwoStates.FOUR_STATES)
async def answer_five_handler(message):
    check = {
        "Человечки мне не понравились": 1,
        "Человечки были скучными": 2,
        "Человечки были интересными": 3,
        "Человечки мне понравились": 4,
        "Человечки крутые!": 5
    }
    db.set_end_answer_four(message.peer_id, message.text, check[message.text])
    await bot.state_dispenser.set(message.peer_id, TestTwoStates.FIVE_STATES)
    keyboard = (
        Keyboard(inline=True)
        .add(Text("Они погрузили в процессы производства"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Они помогли узнать о промышленности"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("С ними было интереснее"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Они недостаточно были полезны"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Они совершенно не помогли"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()
    mess_key = await message.answer("Помогли ли «человечки» лучше узнать промышленность?", keyboard=keyboard)
    return mess_key


@labeler.message(text=["Они погрузили в процессы производства",
                       "Они помогли узнать о промышленности",
                       "С ними было интереснее",
                       "Они недостаточно были полезны",
                       "Они совершенно не помогли"],
                 state=TestTwoStates.FIVE_STATES)
async def answer_six_handler(message):
    check = {
        "Они совершенно не помогли": 1,
        "Они недостаточно были полезны": 2,
        "С ними было интереснее": 3,
        "Они помогли узнать о промышленности": 4,
        "Они погрузили в процессы производства": 5
    }
    db.set_end_answer_five(message.peer_id, message.text, check[message.text])
    await bot.state_dispenser.set(message.peer_id, TestTwoStates.SIX_STATES)
    keyboard = (
        Keyboard(inline=True)
        .add(Text("Работа в команде - это круто!"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Работа в команде - это здорово"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Работа в команде - это хорошо"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Работа в команде - это сложно"), color=KeyboardButtonColor.POSITIVE)
        .row()
        .add(Text("Работа в команде - это неинтересно"), color=KeyboardButtonColor.POSITIVE)
    ).get_json()
    mess_key = await message.answer("Понравилось ли тебе работать в команде?", keyboard=keyboard)
    return mess_key


@labeler.message(text=["Работа в команде - это круто!",
                       "Работа в команде - это здорово",
                       "Работа в команде - это хорошо",
                       "Работа в команде - это сложно",
                       "Работа в команде - это неинтересно"],
                 state=TestTwoStates.SIX_STATES)
async def answer_seven_handler(message):
    check = {
        "Работа в команде - это неинтересно": 1,
        "Работа в команде - это сложно": 2,
        "Работа в команде - это хорошо": 3,
        "Работа в команде - это здорово": 4,
        "Работа в команде - это круто!": 5
    }
    db.set_end_answer_six(message.peer_id, message.text, check[message.text])
    await bot.state_dispenser.set(message.peer_id, PartTwoStates.FEEDBACK)
    await asyncio.sleep(2)
    return "Напиши нам отзыв о том, как прошла эта игра с нами! 😊 "


# ------------------------------------------------------------------------------------------------

@labeler.message(text="check")
async def check(message):
    user_id = db.get_user_id(message.peer_id)[0][0]
    if bool(user_id):
        ctx_storage.set(f"{message.peer_id}_team", (int(user_id) % 10))
    await bot.state_dispenser.set(message.peer_id, PartTwoStates.FEEDBACK)
    return "Продолжайте"


@labeler.message(state=PartTwoStates.FEEDBACK)
async def part_two_six_pass_handler(message):
    if len(message.text) < 200:
        db.set_feedback(message.peer_id, message.text)
        await bot.state_dispenser.set(message.peer_id, PartTwoStates.UPDATEFEEDBACK)
        await asyncio.sleep(2)
        return "Что можно улучшить при проведении проектировочной игры? Мы всегда добавляем в нашу программу несколько предложений участников"
    else:
        await message.answer(f"Пожалуйста, введите менее 200 символов\nКоличество ваших символов: ${len(message.text)}")


@labeler.message(state=PartTwoStates.UPDATEFEEDBACK)
async def part_two_seven_pass_handler(message):
    if len(message.text) < 200:
        db.set_updatefeedback(message.peer_id, message.text)
        keyboard = (
            Keyboard(inline=True)
            .add(Text("Да"), color=KeyboardButtonColor.POSITIVE)
            .row()
            .add(Text("Нет"), color=KeyboardButtonColor.POSITIVE)
        ).get_json()
        await asyncio.sleep(2)
        messageForReturn = await message.answer("Хочешь попасть на нашу следующую игру «Производство будущего»?",
                                                keyboard=keyboard)
        await bot.state_dispenser.set(message.peer_id, PartTwoStates.NEXTGAME)
        return messageForReturn
    else:
        await message.answer(f"Пожалуйста, введите менее 200 символов\nКоличество ваших символов: ${len(message.text)}")


@labeler.message(text=["Да", "Нет"], state=PartTwoStates.NEXTGAME)
async def part_two_eight_pass_handler(message):
    db.set_nextgame(message.peer_id, message.text)
    photo_1 = await photo_uploader.upload(
        file_source=f"img/endgame.jpg",
        peer_id=message.peer_id,
    )
    document_pdf = await excel_uploader.upload(
        file_source=f"img/Листовка_Базовая_кафедра_ОмГТУ_2024_2025_2.pdf",
        peer_id=message.peer_id,
        title='Листовка_Базовая_кафедра_ОмГТУ_2024_2025_2.pdf'
    )
    await message.answer("Спасибо за ответы и участие в игре «Производство будущего» 🤗", attachment=photo_1)
    await asyncio.sleep(2)
    await message.answer("А теперь самая полезная информация, которую мы дарим тебе по результатам прохождения игры")
    await asyncio.sleep(2)
    await message.answer('Наше общение не прекращаетя! Если ты в этом году окончил школу, то у тебя есть возможность стать другом "Газпромнеть-ОНПЗ"')
    await asyncio.sleep(2)
    await message.answer('Это можно сделать, поступив на базовую кафедру "Газпром нефть" в ОмГТУ')
    await asyncio.sleep(2)
    await message.answer("И ты еще успеваешь это сделать, даже если уже подал документы в вуз!")
    await asyncio.sleep(2)
    await message.answer('''Для этого нужно сделать три действия:

1. Написать в ТГ или WhatsApp куратору базовой кафедры Анне Анатольевне по номеру 89136320877
2. Заполнить заявку, которую Анна Анатольевна тебе направит
3. Пройти проверку и стать студентом базовой кафедры "Газпром нефти" в ОмГТУ
''')
    await asyncio.sleep(2)
    await message.answer('''Сделать это можно только до 18 июля! Но лучше сегодня, пока еще есть такая возможность''')
    await asyncio.sleep(2)
    await message.answer('''А пока лови листовку, в которой про это подробнее написано ''', attachment=document_pdf)
    await asyncio.sleep(2)
    await message.answer('''Ну все, теперь ты знаешь все, что нужно! До встречи!''')

    await bot.state_dispenser.delete(message.peer_id)

