#from dataclasses import dataclass
# def say_something(number: int, word: str) -> str:
#     word = word.capitalize()
#     return word*number


# print(say_something(5, 'say something '))


# class User():
#     def __init__(self, user_id, name, age, email):
#         self.user_id = user_id
#         self.name = name
#         self.age = age
#         self.email = email


# def get_user_info(user: User) -> str:
#     return f'Возраст пользователя {user.name} - {user.age}, '\
#         f'а email - {user.email}'


# user_1: User = User(42, 'Anton', '30', 'tony_makarony@gmail.com')
# print(get_user_info(user_1))


# @dataclass
# class User2:
#     user_id: int
#     name: str
#     age: int
#     email: str


# user_2: User2 = User2(4, 'Sergey', '35', 'makarony@gmail.com')
# print(get_user_info(user_2))


# @dataclass
# class DatabaseConfig:
#     db_host: str
#     db_user: str
#     db_password: str
#     database: str


# @dataclass
# class TgBot:
#     token: str
#     admin_ids: list[int]


# @dataclass
# class Config:
#     tg_bot: TgBot
#     db: DatabaseConfig


# config = Config(tg_bot=TgBot(token=BOT_TOKEN, admin_ids=ADMIN_IDS), db=DatabaseConfig(
#     db_host=DB_HOST, db_user=DB_USER, db_password=DB_PASSWORD, database=DATABASE))


import requests

api_url = 'http://numbersapi.com/43'
response = requests.get(api_url)
if response.status_code == 200:
    print(response.text)
else:
    print(response.status_code)
