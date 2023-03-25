import requests
from pathlib import Path


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
        filename = f'spacex_{photo_number}.jpeg'
        download_photo(photo_link, dir, filename)


if __name__ == '__main__':
    fetch_spacex_last_launch()
