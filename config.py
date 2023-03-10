TOKEN = '5834164548:AAHzMlogbI6k4ARkaWNsX_VGSIcgaX0uzKU'
from translate import Translator


helpach = """ <em>Вы использовали команду /help </em>

Список команд:

<b>Второстепенные: </b>
/start - перезапускает бота 🚀

/help - показывает этот список 🆘

<b>Основные: </b>

/translate - выбрать язык с которого переводить, затем выбрать язык на который переводить, и написать текст. Всё в одной команде

<b>Полезные штуки: </b>

У нас есть телеграм-канал с новостями по этому боту, поэтому, ну заходите: @SuprTranslateBotNews 

Также есть инструкция использования бота, https://t.me/SuprTranslateBotNews/3 """


# очень важная штука, проверяющая подписан ли ты на канал:
# if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):


# Translate function
def translate(fr: str, to: str, text: str):
	transl = Translator(from_lang=fr, to_lang=to)
	transl = transl.translate(text=text)
	return transl