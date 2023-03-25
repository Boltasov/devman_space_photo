import os.path

import requests
from pathlib import Path
import os
from urllib.parse import urlparse, unquote
from dotenv import load_dotenv


def download_photo(url, path, filename):
    Path(path).mkdir(exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()

    with open(f'{path}/{filename}', 'wb') as file:
        file.write(response.content)

def fetch_spacex_last_launch():
    spacex_url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'

    response = requests.get(spacex_url)
    response.raise_for_status()
    links_list = response.json()['links']['flickr']['original']

    for photo_number, photo_link in enumerate(links_list):
        dir = 'images'
        photo_name = unquote(os.path.split(urlparse(photo_link).path)[1])
        filename = f'spacex_{photo_name}'
        download_photo(photo_link, dir, filename)


def fetch_nasa_photos():
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    nasa_url = f'https://api.nasa.gov/planetary/apod?api_key={nasa_api_key}'
    params = {
        "api_key": nasa_api_key,
        "count": 30,
    }

    response = requests.get(nasa_url, params)
    response.raise_for_status()
    for photo_data in response.json():
        dir = 'images'
        photo_link = photo_data['url']
        photo_name = unquote(os.path.split(urlparse(photo_link).path)[1])
        filename = f'nasa_{photo_name}'
        download_photo(photo_link, dir, filename)


def get_extension(url):
    return os.path.splitext(url)[1]


if __name__ == '__main__':
    #fetch_spacex_last_launch()
    #get_extension('https://apod.nasa.gov/apod/image/2303/_GHR3094-venerelunafirma800.jpg')
    fetch_nasa_photos()
