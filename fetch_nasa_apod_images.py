import os.path
import requests
import os
import argparse

from urllib.parse import urlparse, unquote
from dotenv import load_dotenv
from download_images import download_images


def get_apod_img_name(img_link):
    photo_name = unquote(os.path.split(urlparse(img_link).path)[1])
    filename = f'nasa_{photo_name}'
    return filename


def fetch_nasa_apod_images(nasa_params, photo_count):
    nasa_apod_url = 'https://api.nasa.gov/planetary/apod'
    params = nasa_params
    params['count'] = photo_count

    response = requests.get(nasa_apod_url, params)
    response.raise_for_status()
    for img_data in response.json():
        img_link = img_data['url']
        filename = get_apod_img_name(img_link)
        download_images(img_link, filename, nasa_params)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Программа загружает в папку "/images" фотографии NASA APOD'
    )
    parser.add_argument('--count', help='Количество фотографий', required=False, default='10')
    args = parser.parse_args()
    photo_count = args.count

    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    nasa_params = {
        "api_key": nasa_api_key,
    }
    fetch_nasa_apod_images(nasa_params, photo_count)
    print(f'Изображения появятся в папке images')
