import requests

from pathlib import Path


def download_nasa_photo(url, filename, api_key):
    folder = 'images'
    Path(folder).mkdir(exist_ok=True)
    params = {
        'api_key': api_key
    }
    response = requests.get(url, params)
    response.raise_for_status()

    with open(f'{folder}/{filename}', 'wb') as file:
        file.write(response.content)


def download_spacex_photo(url, filename):
    folder = 'images'
    Path(folder).mkdir(exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()

    with open(f'{folder}/{filename}', 'wb') as file:
        file.write(response.content)
