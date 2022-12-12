from aiogram import Bot, Dispatcher, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from environs import Env


env = Env()
env.read_env()

bot_token = env('BOT_TOKEN')


bot: Bot = Bot(token=bot_token)
dp: Dispatcher = Dispatcher(bot)

keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup()

url_button_1: InlineKeyboardButton = InlineKeyboardButton(
    text='Курс по Python ботам', url='https://stepik.org/120924')
url_button_2: InlineKeyboardButton = InlineKeyboardButton(
    text='Документация Telegram Bot API', url='https://core.telegram.org/bots/api')


group_name = env('GROUP_NAME')
admin_id = env('ADMIN_ID')

button_3: InlineKeyboardButton = InlineKeyboardButton(
    text='Группа мейкеров', url=f'tg://user?id={admin_id}')

keyboard.add(url_button_1).add(url_button_2).add(button_3)


async def process_start_command(message: Message):
    await message.answer(text='Это инлайн книпки УРЛ', reply_markup=keyboard)

dp.register_message_handler(process_start_command, commands=['start'])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
