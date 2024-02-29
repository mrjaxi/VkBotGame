from vkbottle import API, BuiltinStateDispenser, CtxStorage, PhotoMessageUploader, DocMessagesUploader, \
    VoiceMessageUploader
from vkbottle.bot import BotLabeler
from environs import Env

env = Env()
env.read_env(".env")
api = API(env.str("BOT_TOKEN"))
photo_uploader = PhotoMessageUploader(api)
excel_uploader = DocMessagesUploader(api)
audio_uploader = VoiceMessageUploader(api)
labeler = BotLabeler()
state_dispenser = BuiltinStateDispenser()

