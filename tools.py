import requests
from urllib.parse import urlparse
from os.path import splitext


def download_image(url, file_path, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(file_path, 'wb') as file:
        file.write(response.content)


def get_extension(link):
    split_link = urlparse(link)
    extension = splitext(split_link.path)
    return extension[1]
