import os.path
import requests
import datetime
import os

from pathlib import Path
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


def get_epic_img_name(img_info):
    img_name = img_info['image']
    img_name = f'{img_name}.png'
    return img_name


def get_epic_img_url(img_info, img_name):
    img_date = img_info['date']
    img_date = datetime.datetime.strptime(img_date, '%Y-%m-%d %H:%M:%S')
    img_url = 'https://api.nasa.gov/EPIC/archive/natural/{0:%Y}/{0:%m}/{0:%d}/png/{1}'.format(img_date, img_name)
    return img_url


def fetch_nasa_epic_photos():
    dir = 'images'
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    nasa_epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        "api_key": nasa_api_key,
    }

    response = requests.get(nasa_epic_url, params)
    img_list = response.json()[5:]
    for img_info in img_list:
        img_name = get_epic_img_name(img_info)
        img_url = get_epic_img_url(img_info, img_name)

        download_photo(img_url, dir, img_name, nasa_api_key)
    return len(img_list)


if __name__ == '__main__':
    img_count = fetch_nasa_epic_photos()
    print(f'Количество изображений: {img_count}')