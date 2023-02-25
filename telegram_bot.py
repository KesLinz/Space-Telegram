import telegram
import os
from dotenv import load_dotenv


def main():
    load_dotenv()
    bot = telegram.Bot(token=os.environ['TELEGRAM_BOT_TOKEN'])
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    bot.send_message(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")


if __name__ == '__main__':
    main()
