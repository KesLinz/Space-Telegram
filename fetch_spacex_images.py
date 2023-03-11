import os

import requests
from dotenv import load_dotenv

from tools import download_image


def fetch_spacex_images(launch_id, folder_name):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()

    for n, url in enumerate(response.json()['links']['flickr']['original']):
        file_path = os.path.join(folder_name, f'spacex_{n}.jpg')
        download_image(url, file_path)


def main():
    load_dotenv()
    launch_id = os.environ['SPACEX_LAUNCH_ID']

    folder_name = 'images'
    os.makedirs(folder_name, exist_ok=True)

    fetch_spacex_images(launch_id, folder_name)


if __name__ == '__main__':
    main()
