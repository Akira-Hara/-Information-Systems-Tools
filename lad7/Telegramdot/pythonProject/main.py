import asyncio
import os
import random

# import aiogram
from aiogram import Bot, types
from aiogram import Dispatcher
from aiogram import Router
from aiogram import F
from aiogram.types import FSInputFile


bot = Bot(token='6443841054:AAHclpKC-OmirbJ3OF2vO4rcqmWZ3soVHPQ') #место для телеграм-токена
dp = Dispatcher()
router = Router()


@dp.message(F.text.lower() == 'привет')
async def process_start_command(message: types.Message):
    await message.reply("Хай")
    await give_info(message)


@dp.message(F.text.lower() == 'помощь')
async def process_help_command(message: types.Message):
    await give_info(message)

@dp.message(F.text == '1')
async def picture_send_command(message: types.Message):
    pic = FSInputFile("C:\\anime\\Ai\\" + str(random.randint(1, 10)) + ".jpg")
    await bot.send_photo(chat_id=message.chat.id, photo=pic)


@dp.message(F.text == '2')
async def picture_send_command(message: types.Message):
    pic = FSInputFile("C:\\anime\\karma\\" + str(random.randint(1, 10)) + ".jpg")
    await bot.send_photo(chat_id=message.chat.id, photo=pic)


@dp.message(F.text == '3')
async def picture_send_command(message: types.Message):
    pic = FSInputFile("C:\\anime\\para\\" + str(random.randint(1, 10)) + ".jpg")
    await bot.send_photo(chat_id=message.chat.id, photo=pic)


@dp.message(F.text == '4')
async def picture_send_command(message: types.Message):
     pic = FSInputFile("C:\\anime\\gorod\\" + str(random.randint(1, 10)) + ".jpg")
     await bot.send_photo(chat_id=message.chat.id, photo=pic)


async def give_info(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="У меня есть арт картинки.\nВыбери категорию!")
    await bot.send_message(chat_id=message.chat.id, text="1 - Девушки\n2 - Парни\n3 - Звери\n4 - Города")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())