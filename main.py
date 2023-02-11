import requests
import os
from urllib.parse import urlparse
from os.path import splitext
from dotenv import load_dotenv


def fetch_spacex_last_launch(folder_name):
    url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(url)
    response.raise_for_status()

    for n, url in enumerate(response.json()['links']['flickr']['original']):
        file_path = os.path.join(folder_name, f'spacex_{n}.jpg')
        download_image(url, file_path)


def fetch_nasa_apod(folder_name, token):
    url = 'https://api.nasa.gov/planetary/apod'
    payload = {'api_key': token,
               'start_date': '2023-01-28'}
    response = requests.get(url, params=payload)

    for n, apod_photos in enumerate(response.json()):
        file_path = os.path.join(folder_name, f'nasa_apod_{n}.jpg')
        if apod_photos['media_type'] != 'image':
            continue
        download_image(apod_photos['url'], file_path)


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


def download_image(url, file_path, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(file_path, 'wb') as file:
        file.write(response.content)


def get_extension(link):
    split_link = urlparse(link)
    extension = splitext(split_link.path)
    return extension[1]


def main():
    folder_name = 'images'
    os.makedirs(folder_name, exist_ok=True)

    load_dotenv()
    token = os.environ['NASA_TOKEN']

    # fetch_spacex_last_launch(folder_name)
    fetch_nasa_apod(folder_name, token)
    # fetch_epic(folder_name, token)


if __name__ == '__main__':
    main()
