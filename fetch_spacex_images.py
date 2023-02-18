import os
import requests
import argparse
from tools import download_image
from dotenv import load_dotenv


def fetch_spacex_images(launch_id):
    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
    response = requests.get(url)
    response.raise_for_status()

    for n, url in enumerate(response.json()['links']['flickr']['original']):
        file_path = os.path.join('images', f'spacex_{n}.jpg')
        download_image(url, file_path)


def main():
    load_dotenv()
    launch_id = os.environ['SPACEX_LAUNCH_ID']
    os.makedirs('images', exist_ok=True)
    fetch_spacex_images(launch_id)


if __name__ == '__main__':
    main()
