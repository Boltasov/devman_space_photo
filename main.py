import os.path
import requests
import datetime
import os

from pathlib import Path
from urllib.parse import urlparse, unquote
from dotenv import load_dotenv


def download_photo(url, path, filename, api_key):
    Path(path).mkdir(exist_ok=True)
    if api_key:
        params = {
            'api_key': api_key
        }
        response = requests.get(url, params)
        response.raise_for_status()
    else:
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


# Получает 10 NASA APOD (Astronomy Picture of the Day) images
def fetch_nasa_APOD_photos():
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    nasa_apod_url = 'https://api.nasa.gov/planetary/apod'
    params = {
        "api_key": nasa_api_key,
        "count": 10,
    }

    response = requests.get(nasa_apod_url, params)
    response.raise_for_status()
    for photo_data in response.json():
        dir = 'images'
        photo_link = photo_data['url']
        photo_name = unquote(os.path.split(urlparse(photo_link).path)[1])
        filename = f'nasa_{photo_name}'
        download_photo(photo_link, dir, filename)


# Получает 10 NASA EPIC (Earth Polychromatic Imaging Camera) images
def fetch_nasa_EPIC_photos():
    dir = 'images'
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    nasa_epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        "api_key": nasa_api_key,
    }

    response = requests.get(nasa_epic_url, params)
    print(type(response.json()))
    img_list = response.json()[5:]
    print(len(img_list))
    for img in img_list:
        img_name, img_date = img['image'], img['date']
        img_name = f'{img_name}.png'
        img_date = datetime.datetime.strptime(img_date, '%Y-%m-%d %H:%M:%S')
        img_url = 'https://api.nasa.gov/EPIC/archive/natural/{0:%Y}/{0:%m}/{0:%d}/png/{1}'.format(img_date, img_name)
        print(img_url)
        download_photo(img_url, dir, img_name, nasa_api_key)


def get_extension(url):
    return os.path.splitext(url)[1]


if __name__ == '__main__':
    #fetch_spacex_last_launch()
    #get_extension('https://apod.nasa.gov/apod/image/2303/_GHR3094-venerelunafirma800.jpg')
    #fetch_nasa_APOD_photos()
    fetch_nasa_EPIC_photos()