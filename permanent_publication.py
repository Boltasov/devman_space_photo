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
        for _, _, files in folder:  # Only one iteration. Get files list from generator
            random.shuffle(files)
            for photo in files:
                photo_path = f'{path}/{photo}'
                bot.send_photo(chat_id=telegram_channel_id, photo=open(photo_path, 'rb'))

                time_string = os.getenv('POSTING_TIME')
                if time_string:
                    time_params = time.strptime(time_string, "%H:%M:%S")
                    sleep_seconds = ((time_params.tm_hour * 60) + time_params.tm_min) * 60 + time_params.tm_sec
                else:
                    sleep_seconds = 4 * 60 * 60

                time.sleep(sleep_seconds)
