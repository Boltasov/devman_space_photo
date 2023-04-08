import time
import os
import random
import click

from dotenv import load_dotenv
from pathlib import Path
from publish_image import publish_photo


def count_seconds(time_string):
    time_params = time.strptime(time_string, "%H:%M:%S")
    seconds = ((time_params.tm_hour * 60) + time_params.tm_min) * 60 + time_params.tm_sec
    return seconds


@click.command()
@click.option('-p', '--pause', default='04:00:00', type=str, show_default=True,
              help='Пауза между публикациями в формате HH:MM:SS.')
def permanent_publication(pause, telegram_bot_token, telegram_channel_id):
    while True:
        path = 'images'
        folder = os.walk(path)
        for _, _, files in folder:
            random.shuffle(files)
            for photo_name in files:
                photo_path = Path.cwd() / path / photo_name
                publish_photo(photo_path, telegram_bot_token, telegram_channel_id)

                env_pause = os.getenv('POSTING_TIME')
                if env_pause:
                    time.sleep(count_seconds(env_pause))
                else:
                    time.sleep(count_seconds(pause))


if __name__ == '__main__':
    load_dotenv()
    telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    telegram_channel_id = os.environ['TELEGRAM_CHANNEL_ID']
    permanent_publication(telegram_bot_token=telegram_bot_token, telegram_channel_id=telegram_channel_id)
