import time
import telegram
import os
import random

from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    telegram_channel_id = os.environ['TELEGRAM_CHANNEL_ID']
    bot = telegram.Bot(token=telegram_bot_token)

    while True:
        path = 'images'
        folder = os.walk(path)
        print('iteration')
        for _, _, files in folder:
            random.shuffle(files)
            print(files)
            for file in files:
                file_path = f'{path}/{file}'
                bot.send_photo(chat_id=telegram_channel_id, photo=open(file_path, 'rb'))

                time_string = os.environ['POSTING_TIME']
                time_params = time.strptime(time_string, "%H:%M:%S")
                sleep_seconds = ((time_params.tm_hour * 60) + time_params.tm_min) * 60 + time_params.tm_sec
                time.sleep(sleep_seconds)

