from aiogram import Bot, Dispatcher, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from environs import Env


env = Env()
env.read_env()

bot_token = env('BOT_TOKEN2')


bot: Bot = Bot(token=bot_token)
dp: Dispatcher = Dispatcher(bot)

# Режим, при котором в тексте сообщений можно указывать некоторые HTML-теги
PARSE_MODE: str = 'HTML'

LEXICON: dict[str, str] = {'but_1': 'Кнопка 1',
                           'but_2': 'Кнопка 2',
                           'but_3': 'Кнопка 3',
                           'but_4': 'Кнопка 4',
                           'but_5': 'Кнопка 5',
                           'but_6': 'Кнопка 6',
                           'but_7': 'Кнопка 7', }

BUTTONS: dict[str, str] = {'btn_1': '1',
                           'btn_2': '2',
                           'btn_3': '3',
                           'btn_4': '4',
                           'btn_5': '5',
                           'btn_6': '6',
                           'btn_7': '7',
                           'btn_8': '8',
                           'btn_9': '9',
                           'btn_10': '10',
                           'btn_11': '11'}


# def create_inline_kb(row_width: int, *args, **kwargs) -> InlineKeyboardMarkup:
#    inline_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(row_width=row_width)
#    if args:
#        [inline_kb.insert(InlineKeyboardButton(
#            text=LEXICON[button], callback_data=button)) for button in args]
#    if kwargs:
#        [inline_kb.insert(InlineKeyboardButton(
#            text=text, callback_data=button)) for button, text in kwargs.items()]

#    return inline_kb
def create_inline_kb(row_width: int, *args, last_btn: str | None = None, **kwargs) -> InlineKeyboardMarkup:
    inline_kb: InlineKeyboardMarkup = InlineKeyboardMarkup(row_width=row_width)
    if args:
        [inline_kb.insert(InlineKeyboardButton(
            text=LEXICON[button],
            callback_data=button)) for button in args]
    if kwargs:
        [inline_kb.insert(InlineKeyboardButton(
            text=text,
            callback_data=button)) for button, text in kwargs.items()]
    if last_btn:
        inline_kb.add(InlineKeyboardButton(
            text=last_btn, callback_data='last_btn'))
    return inline_kb

# async def precess_start_command(message: Message):
#    keyboard = create_inline_kb(2, btn_tel='Телефон',
#                                btn_email='email',
#                                btn_website='Web-сайт',
#                                btn_vk='VK',
#                                btn_tgbot='Наш телеграм-бот')

#    await message.answer(text='Сгенерированная инлдайн клавиатура', reply_markup=keyboard)


async def precess_start_command(message: Message):
    keyboard = create_inline_kb(2, last_btn='Последняя кнопка', **BUTTONS)
    await message.answer(text='Сгенерированная инлдайн клавиатура', reply_markup=keyboard)

dp.register_message_handler(precess_start_command, commands='start')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
