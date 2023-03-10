import logging
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN, helpach, translate
from markups import *
import keep_alive


API_TOKEN = TOKEN
CHANNEL_ID = "@SuprTranslateBotNews"
NOTSUB_MESSAGE = "Для доступа к фунционалу бота, подпишитесь на канал!"
CURRENT_LANG_FROM = 'en'
CURRENT_LANG_TO = 'ru'

# Configure logging
logging.basicConfig(level =logging.INFO)

# Initialize bot and dispatcher
bot  = Bot (token =API_TOKEN)
dp = Dispatcher (bot)

def check_sub_channel(chat_member):
   print(chat_member['status'])
   if chat_member['status'] != 'left':
      return True
   else:
      return False

# /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   if message.chat.type == 'private':
      if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
         await message.answer("Привет!\nЯ Супербот-переводчик\nПереведу любой текст. Комманда /help в помощь!")
      else:
         await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=checkSubMenu)

# /help
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
   if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
      await message.reply (text=helpach, parse_mode="HTML")
   else:
      await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=checkSubMenu)

# /translate
@dp.message_handler(commands=['translate'])
async def help_command(message: types.Message):
   if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
      await message.reply (text='Выбери язык, с которого нужно перевести', parse_mode="HTML", reply_markup=langFromMenu)
   else:
      await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=checkSubMenu)

# to lang
@dp.callback_query_handler(text='engfrom')
async def fromenglang(callback : types.CallbackQuery, message: types.Message):
   CURRENT_LANG_FROM = 'en'
   await bot.send_message(callback.from_user.id, text='Теперь выберите на какой язык переводить', reply_markup=langToMenu)

@dp.callback_query_handler(text='rusfrom')
async def fromruslang(callback : types.CallbackQuery):
   CURRENT_LANG_FROM = 'ru'
   await bot.send_message(callback.from_user.id, text='Теперь выберите на какой язык переводить', reply_markup=langToMenu)

@dp.callback_query_handler(text='frnfrom')
async def fromfrnlang(callback : types.CallbackQuery):
   CURRENT_LANG_FROM = 'fr'
   await bot.send_message(callback.from_user.id, text='Теперь выберите на какой язык переводить', reply_markup=langToMenu)

@dp.callback_query_handler(text='gerfrom')
async def fromgerlang(callback : types.CallbackQuery):
   CURRENT_LANG_FROM = 'de'
   await bot.send_message(callback.from_user.id, text='Теперь выберите на какой язык переводить', reply_markup=langToMenu)

   
# text
@dp.callback_query_handler(text='engto')
async def toenglang(callback : types.CallbackQuery):
   CURRENT_LANG_TO = 'en'
   await bot.send_message(callback.from_user.id, text='Отлично! Введите текст который нужно перевести')

@dp.callback_query_handler(text='rusto')
async def toruslang(callback : types.CallbackQuery):
   CURRENT_LANG_TO = 'ru'
   await call.message.answer(callback.from_user.id, text='Отлично! Введите текст который нужно перевести')

@dp.callback_query_handler(text='frnto')
async def tofrnlang(callback : types.CallbackQuery):
   CURRENT_LANG_TO = 'fr'
   await call.message.answer(callback.from_user.id, text='Отлично! Введите текст который нужно перевести')

@dp.callback_query_handler(text='gerto')
async def togerlang(callback : types.CallbackQuery):
   CURRENT_LANG_TO = 'de'
   await call.message.answer(callback.from_user.id, text='Отлично! Введите текст который нужно перевести')

@dp.message_handler()
async def send_echo(message: types.Message):
   await message.reply(translate(CURRENT_LANG_FROM, CURRENT_LANG_TO, message.text))


@dp.callback_query_handler(text = "subchanneldone")
async def subchanneldone(message:types.Message):
   await bot.delete_message(message.from_user.id, message.message.message_id)
   if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
         await message.answer("Привет!\nЯ Супербот-переводчик\nПереведу любой текст. Комманда /help в помощь!")
   else:
      await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=checkSubMenu)
   



keep_alive.keep_alive()
client.ru

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)