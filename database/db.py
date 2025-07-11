import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id, date, number):
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO `user` (`user_id`, `date`, `status`, `number`) VALUES ( ?, ?, ?, ?)",
                (user_id, date, 0, number,))

    def set_name_and_team(self, user_id, name, team):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `user_fio` = ?, `team` = ? WHERE `user_id` = ?",
                                       (name, team, user_id,))

    # подсчет количества вариантов в одной команде
    def counting_variant_team(self, team, date):
        with self.connection:
            result = self.cursor.execute(
                "SELECT COUNT(`number`) FROM `user` WHERE `date` = ? and `team` = ? and `status` = ?",
                (date, team, 0,)).fetchall()
            return result

    # добавление команды
    def set_number(self, user_id, number):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `number` = ? WHERE `user_id` = ?",
                                       (number, user_id,))

    # добавление города
    def set_city(self, user_id, city):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `city` = ? WHERE `user_id` = ?",
                                       (city, user_id,))

    # добавление школы
    def set_school(self, user_id, school):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `school` = ? WHERE `user_id` = ?",
                                       (school, user_id,))

    # добавление класса
    def set_user_class(self, user_id, user_class):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `user_class` = ? WHERE `user_id` = ?",
                                       (user_class, user_id,))

    # добавление команды
    def set_team(self, user_id, team):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `team` = ? WHERE `user_id` = ?",
                                       (team, user_id,))

    # добавление ответа на вопрос 1
    def set_answer_one(self, user_id, answer):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `answer_one` = ? WHERE `user_id` = ?",
                                       (answer, user_id,))

    # добавление ответа на вопрос 2
    def set_answer_two(self, user_id, answer):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `answer_two` = ? WHERE `user_id` = ?",
                                       (answer, user_id,))

    # добавление ответа на вопрос 3
    def set_answer_three(self, user_id, answer):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `answer_three` = ? WHERE `user_id` = ?",
                                       (answer, user_id,))

    # добавление ответа на вопрос 4
    def set_answer_four(self, user_id, answer):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `answer_four` = ? WHERE `user_id` = ?",
                                       (answer, user_id,))

    # добавление ответа на вопрос 5
    def set_answer_five(self, user_id, answer):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `answer_five` = ? WHERE `user_id` = ?",
                                       (answer, user_id,))

    # добавление ответа на вопрос 6
    def set_answer_six(self, user_id, answer):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `answer_six` = ? WHERE `user_id` = ?",
                                       (answer, user_id,))

    # добавление ответа на вопрос 7
    def set_answer_seven(self, user_id, answer):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `answer_seven` = ? WHERE `user_id` = ?",
                                       (answer, user_id,))

    # добавление ответа на вопрос 8
    def set_answer_eight(self, user_id, answer):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `answer_eight` = ? WHERE `user_id` = ?",
                                       (answer, user_id,))

    # добавление города
    def set_nfc(self, user_id, nfc_id):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `nfc_id` = ? WHERE `user_id` = ?",
                                       (nfc_id, user_id,))

    # добавление предметов
    def set_subject(self, user_id, subj):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `subject` = ? WHERE `user_id` = ?",
                                       (subj, user_id,))

    # добавление предметов
    def set_status(self, user_id):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `status` = ? WHERE `user_id` = ?",
                                       (1, user_id,))

    # добавление предметов
    def set_status_all(self):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `status` = ? WHERE `status` = ?",
                                       (1, 0,))

    # добавление отзыва
    def set_feedback(self, used_id, feedback):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `feedback` = ? WHERE `user_id` = ?",
                                       (feedback, used_id,))

    # добавление отзыва
    def set_updatefeedback(self, used_id, feedback):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `updatefeedback` = ? WHERE `user_id` = ?",
                                       (feedback, used_id,))
    # добавление отзыва
    def set_nextgame(self, used_id, feedback):
        with self.connection:
            return self.cursor.execute("UPDATE `user` SET `nextgame` = ? WHERE `user_id` = ?",
                                       (feedback, used_id,))

    # поиск пользователя по его ID
    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `user` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    # поиск пользователей по команде
    def search_user_team(self, team, number):
        with self.connection:
            result = self.cursor.execute(
                "SELECT `user_fio` FROM `user` WHERE `team` = ? and `number` = ? and `status` = ?",
                (team, number, 0,)).fetchall()
            return result

    # поиск номера пользователя в команде
    def get_user_number_in_team(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `number` FROM `user` WHERE `user_id` = ?",
                                         (user_id,)).fetchall()
            return result

    # вывод user_id юзера
    def get_user_id(self, user_id):
        with self.connection:
            result = self.cursor.execute(
                "SELECT `id` FROM `user` WHERE  `user_id` = ?",
                (user_id,)).fetchall()
            return result

    # вывод user_id юзера
    def get_user_team(self, user_id):
        with self.connection:
            result = self.cursor.execute(
                "SELECT `team` FROM `user` WHERE  `user_id` = ?",
                (user_id,)).fetchall()
            return result

    def del_user(self, user_id):
        with self.connection:
            return self.cursor.execute("DELETE FROM `user` WHERE user_id = ?", (user_id,))

    # подсчет количества нфс кодов
    def counting_nfc_id(self, card_id):
        with self.connection:
            result = self.cursor.execute(
                "SELECT COUNT(`id`) FROM `card` WHERE `card_id` = ? ",
                (card_id,)).fetchall()
            return result

        # поиск пользователя по его ID

    def nfc_exists(self, card_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `card` WHERE `card_id` = ?", (card_id,)).fetchall()
            return bool(len(result))

    # поиск пользователей по команде
    def search_user_all(self, ):
        with self.connection:
            result = self.cursor.execute(
                "SELECT `id`, `date`, `user_fio`, `city`, `school`, `user_class`, `team`, `nfc_id`, `answer_one`, `answer_two`, `answer_six`, `answer_seven`, `answer_eight`, `answer_three`, `answer_four`, `answer_five`, `subject`, `feedback`, `updatefeedback`, `nextgame` FROM `user` ").fetchall()
            return result

    # добавление метки
    def set_nfc_id(self, card_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO `card` (`card_id`) VALUES (?)",
                                       (card_id,))

    # поиск метки по его ID
    def card_exists(self, card_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `card` WHERE `card_id` = ?", (card_id,)).fetchall()
            return bool(len(result))

    # -------------------------Блок тестов 1 Начало-----------------------------------------------

    def add_user_test_one(self, user_id, date, fio):
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO `user_test` (`user_id`, `date`, `fio`) VALUES ( ?, ?, ?)",
                (user_id, date, fio,))

    def set_school_test_one(self, user_id, pol):
        with self.connection:
            return self.cursor.execute("UPDATE `user_test` SET `school` = ? WHERE `user_id` = ?",
                                       (pol, user_id,))

    def set_number_class(self, user_id, age):
        with self.connection:
            return self.cursor.execute("UPDATE `user_test` SET `number_class` = ? WHERE `user_id` = ?",
                                       (age, user_id,))

    def set_test_answer_one(self, user_id, answer, ball):
        with self.connection:
            return self.cursor.execute(
                "UPDATE `user_test` SET `answer_one` = ?,`answer_one_ball` = ? WHERE `user_id` = ?",
                (answer, ball, user_id,))

    def set_test_answer_two(self, user_id, answer, ball):
        with self.connection:
            return self.cursor.execute(
                "UPDATE `user_test` SET `answer_two` = ?,`answer_two_ball` = ? WHERE `user_id` = ?",
                (answer, ball, user_id,))

    def set_test_answer_three(self, user_id, answer, ball):
        with self.connection:
            return self.cursor.execute(
                "UPDATE `user_test` SET `answer_three` = ?,`answer_three_ball` = ? WHERE `user_id` = ?",
                (answer, ball, user_id,))

    def set_test_answer_four(self, user_id, answer, ball):
        with self.connection:
            return self.cursor.execute(
                "UPDATE `user_test` SET `answer_four` = ?,`answer_four_ball` = ? WHERE `user_id` = ?",
                (answer, ball, user_id,))

    def set_test_answer_five(self, user_id, answer, ball):
        with self.connection:
            return self.cursor.execute(
                "UPDATE `user_test` SET `answer_five` = ?,`answer_five_ball` = ? WHERE `user_id` = ?",
                (answer, ball, user_id,))

    def set_test_answer_six(self, user_id, answer, ball):
        with self.connection:
            return self.cursor.execute(
                "UPDATE `user_test` SET `answer_six` = ?,`answer_six_ball` = ? WHERE `user_id` = ?",
                (answer, ball, user_id,))

    def set_test_answer_seven(self, user_id, answer, ball):
        with self.connection:
            return self.cursor.execute(
                "UPDATE `user_test` SET `answer_seven` = ?,`answer_seven_ball` = ? WHERE `user_id` = ?",
                (answer, ball, user_id,))

    def set_test_answer_eight(self, user_id, answer, ball):
        with self.connection:
            return self.cursor.execute(
                "UPDATE `user_test` SET `answer_eight` = ?,`answer_eight_ball` = ? WHERE `user_id` = ?",
                (answer, ball, user_id,))

    def set_test_answer_nine(self, user_id, answer, ball):
        with self.connection:
            return self.cursor.execute(
                "UPDATE `user_test` SET `answer_nine` = ?,`answer_nine_ball` = ? WHERE `user_id` = ?",
                (answer, ball, user_id,))

    def set_test_answer_ten(self, user_id, answer, ball):
        with self.connection:
            return self.cursor.execute(
                "UPDATE `user_test` SET `answer_ten` = ?,`answer_ten_ball` = ? WHERE `user_id` = ?",
                (answer, ball, user_id,))

    def set_test_answer_eleven(self, user_id, answer, ball):
        with self.connection:
            return self.cursor.execute(
                "UPDATE `user_test` SET `answer_eleven` = ?,`answer_eleven_ball` = ? WHERE `user_id` = ?",
                (answer, ball, user_id,))

    def set_test_answer_twelve(self, user_id, answer, ball):
        with self.connection:
            return self.cursor.execute(
                "UPDATE `user_test` SET `answer_twelve` = ?,`answer_twelve_ball` = ? WHERE `user_id` = ?",
                (answer, ball, user_id,))

        # поиск пользователей по команде

    def search_test_one_user_all(self, ):
        with self.connection:
            result = self.cursor.execute(
                "SELECT `date`, `fio`, `school`, `number_class`, `answer_one`,`answer_one_ball`, `answer_two`, `answer_two_ball`,`answer_three`, `answer_three_ball`, `answer_four`,`answer_four_ball`, `answer_five`, `answer_five_ball`, `answer_six`, `answer_six_ball`, `answer_seven`, `answer_seven_ball`,`answer_eight`, `answer_eight_ball`, `answer_nine`, `answer_nine_ball`,`answer_ten`, `answer_ten_ball`,`answer_eleven`, `answer_eleven_ball`, `answer_twelve`, `answer_twelve_ball`, `answer_end_one`, `answer_end_one_ball`, `answer_end_two`, `answer_end_two_ball`, `answer_end_three`, `answer_end_three_ball`, `answer_end_four`, `answer_end_four_ball`, `answer_end_five`, `answer_end_five_ball`, `answer_end_six`, `answer_end_six_ball` FROM `user_test` ").fetchall()
            return result

    # -------------------------Блок тестов 1 Завершение-----------------------------------------------

    # -------------------------Блок тестов 2 Начало-----------------------------------------------
    def set_end_answer_one(self, user_id, answer, ball):
        with self.connection:
            return self.cursor.execute(
                "UPDATE `user_test` SET `answer_end_one` = ?,`answer_end_one_ball` = ? WHERE `user_id` = ?",
                (answer, ball, user_id,))

    def set_end_answer_two(self, user_id, answer, ball):
        with self.connection:
            return self.cursor.execute(
                "UPDATE `user_test` SET `answer_end_two` = ?,`answer_end_two_ball` = ? WHERE `user_id` = ?",
                (answer, ball, user_id,))

    def set_end_answer_three(self, user_id, answer, ball):
        with self.connection:
            return self.cursor.execute(
                "UPDATE `user_test` SET `answer_end_three` = ?,`answer_end_three_ball` = ? WHERE `user_id` = ?",
                (answer, ball, user_id,))

    def set_end_answer_four(self, user_id, answer, ball):
        with self.connection:
            return self.cursor.execute(
                "UPDATE `user_test` SET `answer_end_four` = ?,`answer_end_four_ball` = ? WHERE `user_id` = ?",
                (answer, ball, user_id,))

    def set_end_answer_five(self, user_id, answer, ball):
        with self.connection:
            return self.cursor.execute(
                "UPDATE `user_test` SET `answer_end_five` = ?,`answer_end_five_ball` = ? WHERE `user_id` = ?",
                (answer, ball, user_id,))

    def set_end_answer_six(self, user_id, answer, ball):
        with self.connection:
            return self.cursor.execute(
                "UPDATE `user_test` SET `answer_end_six` = ?,`answer_end_six_ball` = ? WHERE `user_id` = ?",
                (answer, ball, user_id,))
