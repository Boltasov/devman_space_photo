import time
import os
import random
import argparse
import telegram.error

from dotenv import load_dotenv
from pathlib import Path
from publish_image import publish_photo


def count_seconds(time_string):
    time_params = time.strptime(time_string, "%H:%M:%S")
    seconds = ((time_params.tm_hour * 60) + time_params.tm_min) * 60 + time_params.tm_sec
    return seconds


def permanent_publication(pause, telegram_bot_token, telegram_channel_id):
    sleep_seconds = count_seconds(pause)

    while True:
        path = 'images'
        folder = os.walk(path)
        for _, _, files in folder:
            random.shuffle(files)
            for photo_name in files:
                photo_path = Path.cwd() / path / photo_name
                while True:
                    try:
                        publish_photo(photo_path, telegram_bot_token, telegram_channel_id)
                        break
                    except telegram.error.NetworkError:
                        print('Пытаюсь восстановить связь...')
                        time.sleep(5)

                time.sleep(sleep_seconds)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                description='Программа публикует фотографии из папки images. По одной фотографии за раз '
                'в заданный промежуток времени.\n'
                'По умолчанию публикация происходит раз в 4 часа.\n'
                'Перед запуском убедитесь, что в папке images есть хотя бы одна фотография.'
    )
    parser.add_argument('--pause', help='Время между публикациями фотографий в формате HH:MM:SS',
                        required=False, default='04:00:00', type=str)
    args = parser.parse_args()
    pause = args.pause

    load_dotenv()
    telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    telegram_channel_id = os.environ['TELEGRAM_CHANNEL_ID']

    permanent_publication(pause, telegram_bot_token, telegram_channel_id)
