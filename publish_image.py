import telegram
import os
import argparse
import random

from dotenv import load_dotenv


def publish_photo(photo_path):
    load_dotenv()
    telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    telegram_channel_id = os.environ['TELEGRAM_CHANNEL_ID']
    bot = telegram.Bot(token=telegram_bot_token)
    if not photo_path:
        path = 'images'
        folder = os.walk(path)
        for _, _, files in folder:
            photo_path = f'{path}/{random.choice(files)}'
    bot.send_photo(chat_id=telegram_channel_id, photo=open(photo_path, 'rb'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Программа публикует в телеграм канале фото, найденное по заданному пути.\n'
                    'Еcли путь не указан, начинает публикацию всех фото из папки images в этой директории.'
    )
    parser.add_argument('--path', help='Укажите путь к фотографии, которую хотите опубликовать.', required=False)
    args = parser.parse_args()
    path = args.path

    publish_photo(path)