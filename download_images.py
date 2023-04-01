import requests

from pathlib import Path
from os import environ
from dotenv import load_dotenv


def download_nasa_image(url, filename):
    folder = 'images'
    Path(folder).mkdir(exist_ok=True)
    load_dotenv()
    nasa_api_key = environ['NASA_API_KEY']
    params = {
        'api_key': nasa_api_key
    }
    response = requests.get(url, params)
    response.raise_for_status()

    with open(f'{folder}/{filename}', 'wb') as file:
        file.write(response.content)


def download_spacex_image(url, filename):
    folder = 'images'
    Path(folder).mkdir(exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()

    with open(f'{folder}/{filename}', 'wb') as file:
        file.write(response.content)
