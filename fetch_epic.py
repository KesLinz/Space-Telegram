import os

import requests
from dotenv import load_dotenv

from tools import download_image


def fetch_epic(token, folder_name):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {'api_key': token}
    response = requests.get(url, params=payload)
    response.raise_for_status()

    for image_dict in response.json():
        image_name = image_dict['image']
        date, time = image_dict['date'].split(' ')
        year, month, day = date.split('-')

        url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image_name}.png'
        file_path = os.path.join(folder_name, f'{image_name}.png')
        download_image(url, file_path, params=payload)


def main():
    load_dotenv()
    token = os.environ['NASA_TOKEN']

    folder_name = 'images'
    os.makedirs(folder_name, exist_ok=True)

    fetch_epic(token, folder_name)


if __name__ == '__main__':
    main()
