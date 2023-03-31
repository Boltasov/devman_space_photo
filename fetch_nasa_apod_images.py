import os.path
import requests
import os

from pathlib import Path
from urllib.parse import urlparse, unquote
from dotenv import load_dotenv


def download_photo(url, path, filename, api_key):
    Path(path).mkdir(exist_ok=True)
    params = {
        'api_key': api_key
    }
    response = requests.get(url, params)
    response.raise_for_status()

    with open(f'{path}/{filename}', 'wb') as file:
        file.write(response.content)


def get_nasa_img_name(img_link):
    photo_name = unquote(os.path.split(urlparse(img_link).path)[1])
    filename = f'nasa_{photo_name}'
    return filename


def fetch_nasa_apod_images():
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    nasa_apod_url = 'https://api.nasa.gov/planetary/apod'
    params = {
        "api_key": nasa_api_key,
        "count": 10,
    }

    response = requests.get(nasa_apod_url, params)
    response.raise_for_status()
    for img_data in response.json():
        dir = 'images'
        img_link = img_data['url']
        filename = get_nasa_img_name(img_link)
        download_photo(img_link, dir, filename, nasa_api_key)
    return len(img_data)


if __name__ == '__main__':
    img_count = fetch_nasa_apod_images()
    print(f'Количество изображений: {img_count}')
