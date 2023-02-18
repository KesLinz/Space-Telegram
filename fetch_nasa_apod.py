import os
import requests
import argparse
from tools import download_image
from dotenv import load_dotenv


def fetch_nasa_apod(folder_name, token, count):
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
    folder_name = 'images'
    os.makedirs(folder_name, exist_ok=True)

    load_dotenv()
    token = os.environ['NASA_TOKEN']

    parser = argparse.ArgumentParser()
    parser.add_argument('count',
                        type=int,
                        help='Enter the number of pictures you want to download.',
                        default=None)
    args = parser.parse_args()

    fetch_nasa_apod(folder_name, token, args.count)


if __name__ == '__main__':
    main()
