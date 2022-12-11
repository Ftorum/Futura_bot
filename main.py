from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from environs import Env


env = Env()
env.read_env()


bot_token = env('BOT_TOKEN')


bot: Bot = Bot(token=bot_token)
dp: Dispatcher = Dispatcher(bot)

keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup()
button_1: KeyboardButton = KeyboardButton('Собак')
button_2: KeyboardButton = KeyboardButton('Огурцов')

keyboard.add(button_1, button_2)


async def process_start_command(message: types.Message):
    await message.answer('Чего бояться кошки?', reply_markup=keyboard)


async def process_dog_answer(message: types.Message):
    await message.answer('Да, так и есть', reply_markup=ReplyKeyboardRemove())


async def process_cucumber_answer(message: types.Message):
    await message.answer('Нет, попробуй снова!', reply_markup=ReplyKeyboardRemove())


dp.register_message_handler(process_start_command, commands='start')
dp.register_message_handler(process_dog_answer, text='Собак')
dp.register_message_handler(process_cucumber_answer, text='Огурцов')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
