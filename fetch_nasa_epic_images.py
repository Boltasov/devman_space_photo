import requests
import datetime
import os
import argparse

from dotenv import load_dotenv
from download_images import download_images


def get_epic_img_name(img_info):
    img_name = img_info['image']
    img_name = f'{img_name}.png'
    return img_name


def get_epic_img_url(img_info, img_name):
    img_date = img_info['date']
    img_date = datetime.datetime.strptime(img_date, '%Y-%m-%d %H:%M:%S')
    img_url = 'https://api.nasa.gov/EPIC/archive/natural/{0:%Y}/{0:%m}/{0:%d}/png/{1}'.format(img_date, img_name)
    return img_url


def fetch_nasa_epic_photos(nasa_params, photo_count):
    nasa_epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'

    response = requests.get(nasa_epic_url, nasa_params)
    images = response.json()[:photo_count]
    for img_info in images:
        img_name = get_epic_img_name(img_info)
        img_url = get_epic_img_url(img_info, img_name)

        download_images(img_url, img_name, nasa_params)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Программа загружает в папку "/images" фотографии NASA EPIC.'
    )
    parser.add_argument('--count', help='Количество фотографий', required=False, default=5, type=int)
    args = parser.parse_args()
    photo_count = args.count

    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    nasa_params = {
        "api_key": nasa_api_key,
    }
    fetch_nasa_epic_photos(nasa_params, photo_count)
    print(f'Изображения появятся в папке images')
