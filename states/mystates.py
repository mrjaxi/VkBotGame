from vkbottle import BaseStateGroup


class WelcomeStatesStudent(BaseStateGroup):
    START_PASS_STATE = "nfs_start"


class AddNfsStates(BaseStateGroup):
    START_STATE = "nfs_start"


class WelcomeStates(BaseStateGroup):
    PASSWORD_START_STATE = "password_start"
    VOICE_HELLO_STATE = "voice_hello"
    FIO_STATE = "fio"
    CITY_STATE = "city"
    SCHOOL_STATE = "school"
    CLASS_STATE = "class"
    END_STATE_ONE = "end1"
    END_STATE_TWO = "end2"
    END_STATE_THREE = "end3"
    END_STATE_FOUR = "end4"


class PartOneStates(BaseStateGroup):
    START_STATE = "part_one_start"
    PASSWORD_GAME_STATES = "password_game"
    END_PASSWORD_GAME_STATES = "end_password_game"
    ANSWER_ONE_STATES = "answer_one"
    ANSWER_TWO_STATES = "answer_two"
    ANSWER_THREE_STATES = "answer_three"
    ANSWER_FOUR_STATES = "answer_four"
    ANSWER_FIVE_STATES = "answer_five"
    PASS_ONE = "pass_one"
    KEYBOARD_ONE = "keyboard_one"
    KEYBOARD_TWO = "keyboard_two"
    KEYBOARD_THREE = "keyboard_three"
    NEW_PASSWORD_STATES = "new_pass"


class PartTwoStates(BaseStateGroup):
    PASSWORD_START_TWO_STATES = "password_start_game_two"
    PASSWORD_START_THREE_STATES = "password_start_game_three"
    NFC_ID = "nfc_id"
    NFC_GET_ONE = "nfc_get_one"
    NFC_DIPLOM = "get_diplom"
    NFC_GET_TWO = "nfc_get_two"
    NFC_GET_THREE = "nfc_get_three"
    NFC_GET_FOUR = "nfc_get_four"
    FEEDBACK = "feedback"
    UPDATEFEEDBACK = "updatefeedback"
    NEXTGAME = "nextgame"

class PartThreeStates(BaseStateGroup):
    PASS = "pass"
    PASS_ONE = "pass_one"
class TestOneStates(BaseStateGroup):
    GO_STATES = "go"
    ONE_STATES = "one"
    TWO_STATES = "two"
    THREE_STATES = "three"
    FOUR_STATES = "four"
    FIVE_STATES = "five"
    SIX_STATES = "six"
    SEVEN_STATES = "seven"
    EIGHT_STATES = "eight"
    NINE_STATES = "nine"
    TEN_STATES = "ten"
    ELEVEN_STATES = "eleven"
    TWELVE_STATES = "twelve"


class TestTwoStates(BaseStateGroup):
    GO_STATES = "go"
    ONE_STATES = "one"
    TWO_STATES = "two"
    THREE_STATES = "three"
    FOUR_STATES = "four"
    FIVE_STATES = "five"
    SIX_STATES = "six"
    SEVEN_STATES = "seven"
