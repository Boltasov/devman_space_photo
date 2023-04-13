import telegram
import os
import argparse
import random

from dotenv import load_dotenv
from pathlib import Path


def publish_photo(photo_path, telegram_bot_token, telegram_channel_id):
    bot = telegram.Bot(token=telegram_bot_token)
    with open(photo_path, 'rb') as photo:
        bot.send_photo(chat_id=telegram_channel_id, photo=photo)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Программа публикует в телеграм канале фото, найденное по заданному пути.\n'
                    'Еcли путь не указан, начинает публикацию всех фото из папки images в этой директории.'
    )
    parser.add_argument('--path', help='Укажите путь к фотографии, которую хотите опубликовать.', required=False)
    args = parser.parse_args()
    path = args.path

    load_dotenv()
    telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    telegram_channel_id = os.environ['TELEGRAM_CHANNEL_ID']

    if not path:
        folder_path = 'images'
        folder = os.walk(folder_path)
        for _, _, files in folder:
            path = os.path.join(folder_path, random.choice(files))
    publish_photo(path, telegram_bot_token, telegram_channel_id)
