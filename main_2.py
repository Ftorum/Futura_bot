from aiogram import Bot, Dispatcher, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from environs import Env


env = Env()
env.read_env()

bot_token = env('BOT_TOKEN')


bot: Bot = Bot(token=bot_token)
dp: Dispatcher = Dispatcher(bot)


keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup()

button_1: InlineKeyboardButton = InlineKeyboardButton(
    text='Кнопка 1', callback_data='big_button_1_pressed')
button_2: InlineKeyboardButton = InlineKeyboardButton(
    text='Кнопка 2', callback_data='big_button_2_pressed')

keyboard.add(button_1).add(button_2)


async def processed_start_command(message: Message):
    await message.answer(text='Кнопка 1', reply_markup=keyboard)


async def process_button_1_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата Кнопка 1':
        await callback.message.edit_text(text='Была нажата Кнопка 1', reply_markup=callback.message.reply_markup)
    else:
        await callback.answer()


async def process_button_2_press(callback: CallbackQuery):
    if callback.message.text != 'Была нажата Кнопка 2':
        await callback.message.edit_text(text='Была нажата Кнопка 2', reply_markup=callback.message.reply_markup)
    else:
        await callback.answer()

dp.register_message_handler(processed_start_command, commands=['start'])
dp.register_callback_query_handler(process_button_1_press, text=[
                                   'big_button_1_pressed'])
dp.register_callback_query_handler(process_button_2_press, text=[
                                   'big_button_2_pressed'])

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
