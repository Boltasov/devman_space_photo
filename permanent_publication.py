import time
import telegram
import os
import random
import argparse

from dotenv import load_dotenv


def count_seconds(time_string):
    time_params = time.strptime(time_string, "%H:%M:%S")
    seconds = ((time_params.tm_hour * 60) + time_params.tm_min) * 60 + time_params.tm_sec
    return seconds


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Программа публикует в телеграм канале фото с заданной периодичностью.\n'
                    'Еcли период не указан, фото публикуются каждые 4 часа.'
    )
    parser.add_argument('--pause', help='Пауза между публикациями в формате HH:MM:SS.', required=False)
    args = parser.parse_args()
    pause = args.pause

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
                if pause:
                    count_seconds(pause)
                elif time_string:
                    count_seconds(time_string)
                else:
                    sleep_seconds = 4 * 60 * 60

                time.sleep(sleep_seconds)
