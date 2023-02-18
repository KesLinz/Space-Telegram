import os
import requests
from tools import download_image
from dotenv import load_dotenv


def fetch_epic(folder_name, token):
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
    folder_name = 'images'
    os.makedirs(folder_name, exist_ok=True)

    load_dotenv()
    token = os.environ['NASA_TOKEN']
    fetch_epic(folder_name, token)


if __name__ == '__main__':
    main()
