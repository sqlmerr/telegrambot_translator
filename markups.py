from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btnUrlChannel = InlineKeyboardButton(text="ПОДПИСАТЬСЯ", url='https://t.me/SuprTranslateBotNews')
btnDoneSub = InlineKeyboardButton(text="ПРОВЕРИТЬ ПОДПИСКУ ✅", callback_data="subchanneldone")

checkSubMenu = InlineKeyboardMarkup(row_width=1)
checkSubMenu.insert(btnUrlChannel)
checkSubMenu.insert(btnDoneSub)


btnLangFromEng = InlineKeyboardButton(text="English", callback_data="engfrom")
btnLangFromRus = InlineKeyboardButton(text="Русский", callback_data="rusfrom")
btnLangFromFrn = InlineKeyboardButton(text="France", callback_data="frnfrom")
btnLangFromGer = InlineKeyboardButton(text="German", callback_data="gerfrom")

langFromMenu = InlineKeyboardMarkup(row_width=2)
langFromMenu.insert(btnLangFromEng)
langFromMenu.insert(btnLangFromRus)
langFromMenu.insert(btnLangFromFrn)
langFromMenu.insert(btnLangFromGer)

btnLangToEng = InlineKeyboardButton(text="English", callback_data="engto")
btnLangToRus = InlineKeyboardButton(text="Русский", callback_data="rusto")
btnLangToFrn = InlineKeyboardButton(text="France", callback_data="frnto")
btnLangToGer = InlineKeyboardButton(text="German", callback_data="gerto")

langToMenu = InlineKeyboardMarkup(row_width=2)
langToMenu.insert(btnLangToEng)
langToMenu.insert(btnLangToRus)
langToMenu.insert(btnLangToFrn)
langToMenu.insert(btnLangToGer)

