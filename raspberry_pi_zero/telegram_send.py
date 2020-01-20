import telegram
import os


bot = telegram.Bot(token=os.getenv('TELEGRAM_TOKEN'))


print(bot.get_me())


