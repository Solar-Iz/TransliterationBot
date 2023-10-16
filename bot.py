import os
import logging

from aiogram import Bot, Dispatcher, executor, types

# from config import TOKEN

# Задаем словарь для транслитерации
transliteration_dict = {
    'А': 'A',
    'Б': 'B',
    'В': 'V',
    'Г': 'G',
    'Д': 'D',
    'Е': 'E',
    'Ё': 'E',
    'Ж': 'ZH',
    'З': 'Z',
    'И': 'I',
    'Й': 'I',
    'К': 'K',
    'Л': 'L',
    'М': 'M',
    'Н': 'N',
    'О': 'O',
    'П': 'P',
    'Р': 'R',
    'С': 'S',
    'Т': 'T',
    'У': 'U',
    'Ф': 'F',
    'Х': 'KH',
    'Ц': 'TS',
    'Ч': 'CH',
    'Ш': 'SH',
    'Щ': 'SHCH',
    'Ы': 'Y',
    'Ъ': 'IE',
    'Э': 'E',
    'Ю': 'IU',
    'Я': 'IA'
}

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv('TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # Приветственное сообщение
    await message.answer("Привет! Этот бот транслитерирует ФИО в латиницу. Введите ваше ФИО на кириллице.")

# Обработчик текстовых сообщений
@dp.message_handler()
async def transliterate_message(message: types.Message):
    fio_cyrillic = message.text.upper()
    fio_latin = "".join([transliteration_dict.get(char, char) for char in fio_cyrillic])

    logging.info(f"Введенное ФИО: {fio_cyrillic}, Транслитерированное ФИО: {fio_latin}")

    # Отправьте результат пользователю
    await bot.send_message(message.chat.id, text=f"Транслитерированное ФИО: {fio_latin}")

    

if __name__ == '__main__':
    executor.start_polling(dp)