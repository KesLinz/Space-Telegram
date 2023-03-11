import argparse
import os
from random import shuffle
from time import sleep

import telegram
from dotenv import load_dotenv
from pytimeparse import parse


def main():
    load_dotenv()
    bot = telegram.Bot(token=os.environ['TELEGRAM_BOT_TOKEN'])
    chat_id = os.environ['TELEGRAM_CHAT_ID']

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'time_interval',
        type=str,
        help='Enter the time interval with which the bot will send pictures.',
        default='4h',
        nargs='?',
    )
    args = parser.parse_args()

    photos = os.listdir('images')
    while True:
        shuffle(photos)
        for rand_photo in photos:
            with open(os.path.join('images', rand_photo), 'rb') as photo:
                bot.send_photo(chat_id=chat_id, photo=photo)
            sleep(parse(args.time_interval))


if __name__ == '__main__':
    main()
