import telegram
import os
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    telegram_channel_id = os.environ['TELEGRAM_CHANNEL_ID']

    bot = telegram.Bot(token=telegram_bot_token)
    bot.send_photo(chat_id=telegram_channel_id, photo=open('images/nasa_elnino4_jpl.jpg', 'rb'))

