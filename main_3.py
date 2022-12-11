from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, KeyboardButtonPollType
from environs import Env


env = Env()
env.read_env()


bot_token = env('BOT_TOKEN')


bot: Bot = Bot(token=bot_token)
dp: Dispatcher = Dispatcher(bot)


keyboard: ReplyKeyboardMarkup = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True)


keyboard.add(KeyboardButton(text='Отправить телефон', request_contact=True))
keyboard.add(KeyboardButton(text='Отправть геолокацию', request_location=True))
keyboard.add(KeyboardButton(text='Создать опрос/викторину',
             request_poll=KeyboardButtonPollType()))


async def process_start_command(message: types.Message):
    await message.answer('Эксперимент со специальными кнопками', reply_markup=keyboard)


dp.register_message_handler(process_start_command, commands='start')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
