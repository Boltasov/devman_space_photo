import os.path
import requests
import os
import argparse

from urllib.parse import urlparse, unquote
from download_images import download_images


def get_spacex_filename(file_link):
    photo_name = unquote(os.path.split(urlparse(file_link).path)[1])
    filename = f'spacex_{photo_name}'
    return filename


def get_launch_img_links(launch_id='latest'):
    spacex_url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(spacex_url)
    response.raise_for_status()
    links = response.json()['links']['flickr']['original']
    return links


def fetch_spacex_images(links):
    for img_link in links:
        filename = get_spacex_filename(img_link)
        download_images(img_link, filename)


if __name__ == '__main__':
    ''' Для теста можно задать --id=5eb87d47ffd86e000604b38a '''

    parser = argparse.ArgumentParser(
        description='Программа загружает в папку "/images" фотографии запуска spacex,\n'
                    '- при указании id запуска будут загружены фотографии для этого запуска (если есть);\n'
                    '- если не указывать id, будут загружены фотографии c последнего запуска (если есть)\n'
    )
    parser.add_argument('--id', help='id запуска', required=False, default='latest')
    args = parser.parse_args()
    launch_id = args.id

    links = get_launch_img_links(launch_id)

    if not links:
        print('Нет фотографий с последнего запуска')
    else:
        fetch_spacex_images(links)
        print(f'Количество новых изображений: {len(links)}')
    print('Скрипт завершил работу')
