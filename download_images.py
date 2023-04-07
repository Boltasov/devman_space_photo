import requests
import os

from pathlib import Path
from dotenv import load_dotenv





def download_nasa_image(url, filename, params):
    if is_picture(filename):
        folder = 'images'
        Path(folder).mkdir(exist_ok=True)

        response = requests.get(url, params)
        response.raise_for_status()

        path = Path.cwd() / folder / filename
        with open(path, 'wb') as file:
            file.write(response.content)


def download_spacex_image(url, filename):
    if is_picture(filename):
        folder = 'images'
        Path(folder).mkdir(exist_ok=True)
        response = requests.get(url)
        response.raise_for_status()

        path = Path.cwd() / folder / filename
        with open(path, 'wb') as file:
            file.write(response.content)


def is_picture(filename):
    extension = get_extension(filename)
    return extension in ['.png', '.jpg', '.jpeg', '.gif', '.svg']


def get_extension(filename):
    return os.path.splitext(filename)[1]
