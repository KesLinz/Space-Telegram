import argparse
import os

import requests
from dotenv import load_dotenv

from tools import download_image


def fetch_nasa_apod(token, count, folder_name):
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': token,
               'count': count}
    response = requests.get(url, params=payload)

    for n, apod_photos in enumerate(response.json()):
        file_path = os.path.join(folder_name, f'nasa_apod_{n}.jpg')
        if apod_photos['media_type'] != 'image':
            continue
        download_image(apod_photos['url'], file_path)


def main():
    load_dotenv()
    token = os.environ['NASA_TOKEN']

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'count',
        type=int,
        help='Enter the number of pictures you want to download.',
        default=None,
    )
    args = parser.parse_args()

    folder_name = 'images'
    os.makedirs(folder_name, exist_ok=True)

    fetch_nasa_apod(token, args.count, folder_name)


if __name__ == '__main__':
    main()
