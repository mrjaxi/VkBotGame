import pandas as pd
from vkbottle.bot import BotLabeler, Message, rules
from environs import Env

from config import excel_uploader
from database.db import Database

env = Env()
env.read_env(".env")
admin_labeler = BotLabeler()
admin_labeler.auto_rules = [
    rules.FromPeerRule(list(map(int, env.list("ADMINS"))))]  # Допустим, вы являетесь Павлом Дуровым

db = Database('database.db')


@admin_labeler.message(command="set_status")
async def excel(message):
    db.set_status_all()
    await message.answer("Статусы для всех установлены")


@admin_labeler.message(command="help")
async def help(message):
    await message.answer("""После каждой игры нужно вводить команду /set_status
    
Чтобы добавить новые номера меток введи команду /add_nfc
Как закончишь вводить метки введи команду /nfc_stop

Для выгрузки данных Excel введи команду /excel

Если уже проходили тестирование, то нужно удалить свои данные из бд командой /dell""")


@admin_labeler.message(command="excel")
async def excel(message):
    if bool(len(db.search_user_all())):
        await message.answer('Данные за все время')
        users_all = db.search_user_all()

        id = []
        date = []
        fio = []
        city = []
        school = []
        user_class = []
        team = []
        nfc_id = []
        ans_one = []
        ans_two = []
        ans_six = []
        ans_seven = []
        ans_eight = []
        ans_three = []
        ans_four = []
        ans_five = []
        subj = []
        feedback = []
        update = []
        nextgame = []

        for user in users_all:
            id.append(user[0])
            date.append(user[1])
            fio.append(user[2])
            city.append(user[3])
            school.append(user[4])
            user_class.append(user[5])
            team.append(user[6])
            nfc_id.append(user[7])
            ans_one.append(user[8])
            ans_two.append(user[9])
            ans_six.append(user[10])
            ans_seven.append(user[11])
            ans_eight.append(user[12])
            ans_three.append(user[13])
            ans_four.append(user[14])
            ans_five.append(user[15])
            subj.append(user[16])
            feedback.append(user[17])
            update.append(user[18])
            nextgame.append(user[19])

        users_all_test = db.search_test_one_user_all()

        test_one_date = []
        test_one_fio = []
        test_one_school = []
        test_one_class = []
        test_one_ans_one = []
        test_one_ans_one_ball = []
        test_one_ans_two = []
        test_one_ans_two_ball = []
        test_one_ans_three = []
        test_one_ans_three_ball = []
        test_one_ans_four = []
        test_one_ans_four_ball = []
        test_one_ans_five = []
        test_one_ans_five_ball = []
        test_one_ans_six = []
        test_one_ans_six_ball = []
        test_one_ans_seven = []
        test_one_ans_seven_ball = []
        test_one_ans_eight = []
        test_one_ans_eight_ball = []
        test_one_ans_nine = []
        test_one_ans_nine_ball = []
        test_one_ans_ten = []
        test_one_ans_ten_ball = []
        test_one_ans_eleven = []
        test_one_ans_eleven_ball = []
        test_one_ans_twelve = []
        test_one_ans_twelve_ball = []

        test_end_ans_one = []
        test_end_ans_one_ball = []
        test_end_ans_two = []
        test_end_ans_two_ball = []
        test_end_ans_three = []
        test_end_ans_three_ball = []
        test_end_ans_four = []
        test_end_ans_four_ball = []
        test_end_ans_five = []
        test_end_ans_five_ball = []
        test_end_ans_six = []
        test_end_ans_six_ball = []

        count = []
        size = 1
        for user in users_all_test:
            count.append(size)
            size += 1
            test_one_date.append(user[0])
            test_one_fio.append(user[1])
            test_one_school.append(user[2])
            test_one_class.append(user[3])
            test_one_ans_one.append(user[4])
            test_one_ans_one_ball.append(user[5])
            test_one_ans_two.append(user[6])
            test_one_ans_two_ball.append(user[7])
            test_one_ans_three.append(user[8])
            test_one_ans_three_ball.append(user[9])
            test_one_ans_four.append(user[10])
            test_one_ans_four_ball.append(user[11])
            test_one_ans_five.append(user[12])
            test_one_ans_five_ball.append(user[13])
            test_one_ans_six.append(user[14])
            test_one_ans_six_ball.append(user[15])
            test_one_ans_seven.append(user[16])
            test_one_ans_seven_ball.append(user[17])
            test_one_ans_eight.append(user[18])
            test_one_ans_eight_ball.append(user[19])
            test_one_ans_nine.append(user[20])
            test_one_ans_nine_ball.append(user[21])
            test_one_ans_ten.append(user[22])
            test_one_ans_ten_ball.append(user[23])
            test_one_ans_eleven.append(user[24])
            test_one_ans_eleven_ball.append(user[25])
            test_one_ans_twelve.append(user[26])
            test_one_ans_twelve_ball.append(user[27])

            test_end_ans_one.append(user[28])
            test_end_ans_one_ball.append(user[29])
            test_end_ans_two.append(user[30])
            test_end_ans_two_ball.append(user[31])
            test_end_ans_three.append(user[32])
            test_end_ans_three_ball.append(user[33])
            test_end_ans_four.append(user[34])
            test_end_ans_four_ball.append(user[35])
            test_end_ans_five.append(user[36])
            test_end_ans_five_ball.append(user[37])
            test_end_ans_six.append(user[38])
            test_end_ans_six_ball.append(user[39])

        df = pd.DataFrame({"Номер": id,
                           "Дата": date,
                           "ФИО": fio,
                           "Город": city,
                           "Класс": user_class,
                           "Команда": team,
                           "NFC_ID": nfc_id,
                           "Ответ на вопрос 1": ans_one,
                           "Ответ на вопрос 2": ans_two,
                           "Ответ на вопрос 3": ans_six,
                           "Ответ на вопрос 4": ans_seven,
                           "Ответ на вопрос 5": ans_eight,
                           "Ответ на вопрос 6": ans_three,
                           "Ответ на вопрос 7": ans_four,
                           "Ответ на вопрос 8": ans_five,
                           "Предметы": subj,
                           "Отзывы": feedback,
                           "Пожелания": update,
                           "Следующая игра": nextgame})

        df_test_one = pd.DataFrame({"Номер": count,
                                    "Дата": test_one_date,
                                    "ФИО": test_one_fio,
                                    "Класс": test_one_class,
                                    "1. Как ты относишься к техническим и инжинерным специальностям?": test_one_ans_one,
                                    "Баллы1": test_one_ans_one_ball,
                                    "2. Нравится ли тебе делать поделки ?": test_one_ans_two,
                                    "Баллы2": test_one_ans_two_ball,

                                    "3.Чем занимаются люди на промышленных предприятиях?": test_one_ans_three,
                                    "Баллы3": test_one_ans_three_ball,

                                    "1. Нравится тебе сфера нефти": test_one_ans_four,
                                    "Баллы4": test_one_ans_four_ball,

                                    "2. Для чего используется нефть?": test_one_ans_five,
                                    "Баллы5": test_one_ans_five_ball,

                                    "3.Хотелось бы тебе больше узнать о нефти?": test_one_ans_six,
                                    "Баллы6": test_one_ans_six_ball,

                                    "1. Нравится ли тебе компания которые занимается нефтью ?": test_one_ans_seven,
                                    "Баллы7": test_one_ans_seven_ball,

                                    "2.Хотел бы ты быть сотрудником нефтяной компаний?": test_one_ans_eight,
                                    "Баллы8": test_one_ans_eight_ball,

                                    "3. Нравится ли тебе что нефтяные компания  делает для сотрудников и жителей городов присудствия?": test_one_ans_nine,
                                    "Баллы9": test_one_ans_nine_ball,

                                    "1.Нравится ли тебе регион в котором ты живешь?": test_one_ans_ten,
                                    "Баллы10": test_one_ans_ten_ball,

                                    "2  Хотел бы ты работать в своем регионе?": test_one_ans_eleven,
                                    "Баллы11": test_one_ans_eleven_ball,

                                    "3. На твой взгляд люди, работающие в своем регионе это": test_one_ans_twelve,
                                    "Баллы12": test_one_ans_twelve_ball,
                                    })

        df_test_two = pd.DataFrame({"Номер": count,
                                    "Дата": test_one_date,
                                    "ФИО": test_one_fio,
                                    "Класс": test_one_class,
                                    "1. Понравилась ли тебе программа?": test_end_ans_one,
                                    "Баллы1": test_end_ans_one_ball,
                                    "2. Расскажешь о программе своим друзьям?": test_end_ans_two,
                                    "Баллы2": test_end_ans_two_ball,

                                    "3. Как изменилось твое отношение к промышленности?": test_end_ans_three,
                                    "Баллы3": test_end_ans_three_ball,

                                    "4. Понравились ли тебе «человечки», которыми ты пользовался во время прохождения игры?": test_end_ans_four,
                                    "Баллы4": test_end_ans_four_ball,

                                    "5. Помогли ли «человечки» лучше узнать промышленность?": test_end_ans_five,
                                    "Баллы5": test_end_ans_five_ball,

                                    "6. Понравилось ли тебе работать в команде?": test_end_ans_six,
                                    "Баллы6": test_end_ans_six_ball,
                                    })
        print(users_all_test)
        # writer = pd.ExcelWriter('./database_exel_test.xlsx', engine='xlsxwriter')
        # print(writer)
        with pd.ExcelWriter("database_exel_test.xlsx", engine="xlsxwriter") as writer:
            df_test_one.to_excel(writer,  sheet_name="Отраслевая Мотивация 1")
            df_test_two.to_excel(writer,  sheet_name="Отраслевая Мотивация 2")
        # df_test_one.to_excel(writer,  sheet_name="Отраслевая Мотивация 1")
        # df_test_two.to_excel(writer,  sheet_name="Отраслевая Мотивация 2")
        print(df_test_one)
        writer.save()
        print(writer)
        print(excel_uploader)
        excel_test = await excel_uploader.upload(
            file_source='database_exel_test.xlsx',
            peer_id=message.peer_id,
            title='Тест по отраслевой мотивации.xlsx'
        )
        await message.answer(attachment=excel_test)

        with pd.ExcelWriter("database_exel_test.xlsx", engine="xlsxwriter") as writer:
            df.to_excel(writer,  sheet_name="Участники")
        # df.to_excel('./database_exel.xlsx', index=False, sheet_name="Участники")
        print(users_all)
        excel = await excel_uploader.upload(
            file_source='database_exel.xlsx',
            peer_id=message.peer_id,
            title='Данные по пользователям.xlsx'
        )
        await message.answer(attachment=excel)
    else:
        await message.answer('Никто не проходил интерактив')
