from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from environs import Env


env = Env()
env.read_env()


bot_token = env('BOT_TOKEN')


bot: Bot = Bot(token=bot_token)
dp: Dispatcher = Dispatcher(bot)


keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

keyboard.add(*(str(i) for i in range(1, 8)))


async def process_start_command(message: types.Message):
    await message.answer('Чего бояться кошки?', reply_markup=keyboard)


dp.register_message_handler(process_start_command, commands='start')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
