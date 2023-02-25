import telegram
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    bot = telegram.Bot(token=os.environ['TELEGRAM_BOT_TOKEN'])
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    with open('images/spacex_4.jpg', 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo)


if __name__ == '__main__':
    main()
