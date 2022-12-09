import requests
import time
from dotenv import load_dotenv
from dataclasses import dataclass
import os
load_dotenv()


@dataclass
class Config:
    API_URL: str
    BOT_TOKEN: str
    API_CATS_URL: str
    ERROR_TEXT: str


keys = Config(API_URL=os.environ.get("API_URL"),
              BOT_TOKEN=os.environ.get("BOT_TOKEN"),
              API_CATS_URL=os.environ.get('API_CATS_URL'),
              ERROR_TEXT=os.environ.get('ERROR_TEXT'))


TEXT: str = 'Ура! Классный апдейт!'
MAX_COUNTER: int = 100

offset: int = -2
counter = 0
counter_id: int
cat_response: requests.Response
cat_link: str

while counter < MAX_COUNTER:
    print('attempt =', counter)  # Show in console attempts
    updates = requests.get(
        f'{keys.API_URL}{keys.BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(keys.API_CATS_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()['file']
                requests.get(
                    f'{keys.API_URL}{keys.BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(
                    f'{keys.API_URL}{keys.BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={keys.ERROR_TEXT}')
    time.sleep(1)
    counter += 1
