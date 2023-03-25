import os.path

import requests
from pathlib import Path
from os.path import splitext, split
from urllib.parse import urlparse, unquote

def fetch_spacex_last_launch():
    spacex_url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'

    def download_photo(url, path, filename):
        Path(path).mkdir(exist_ok=True)
        response = requests.get(url)
        response.raise_for_status()

        with open(f'{path}/{filename}', 'wb') as file:
            file.write(response.content)

    response = requests.get(spacex_url)
    links_list = response.json()['links']['flickr']['original']

    for photo_number, photo_link in enumerate(links_list):
        dir = 'images'
        photo_name = unquote(split(urlparse(photo_link).path)[1])
        filename = f'spacex_{photo_name}'
        download_photo(photo_link, dir, filename)


def fetch_nasa_picture_of_a_day():
    url = ''


def get_extension(url):
    return splitext(url)[1]


if __name__ == '__main__':
    fetch_spacex_last_launch()
    #get_extension('https://apod.nasa.gov/apod/image/2303/_GHR3094-venerelunafirma800.jpg')
