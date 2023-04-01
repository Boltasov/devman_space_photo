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
        img_link = img_data['url']
        filename = get_apod_img_name(img_link)
        download_nasa_image(img_link, filename)


if __name__ == '__main__':
    fetch_nasa_apod_images()
    print(f'Изображения появятся в папке images')
