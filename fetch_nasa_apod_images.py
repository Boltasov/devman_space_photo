import os.path
import requests
import os

from urllib.parse import urlparse, unquote
from dotenv import load_dotenv
from download_images import download_nasa_image


def get_apod_img_name(img_link):
    photo_name = unquote(os.path.split(urlparse(img_link).path)[1])
    filename = f'nasa_{photo_name}'
    return filename


def fetch_nasa_apod_images(nasa_params):
    nasa_apod_url = 'https://api.nasa.gov/planetary/apod'
    params = nasa_params
    params['count'] = 10

    response = requests.get(nasa_apod_url, params)
    response.raise_for_status()
    for img_data in response.json():
        img_link = img_data['url']
        filename = get_apod_img_name(img_link)
        download_nasa_image(img_link, filename, nasa_params)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    nasa_params = {
        "api_key": nasa_api_key,
    }
    fetch_nasa_apod_images(nasa_params)
    print(f'Изображения появятся в папке images')
