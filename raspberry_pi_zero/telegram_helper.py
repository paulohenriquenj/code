import telegram
import os
from dotenv import load_dotenv
load_dotenv()


class telegram_helper:

    def __init__(self):
        self.bot = telegram.Bot(token=os.getenv('TELEGRAM_TOKEN'))
        self.chat_id = chat_id=os.getenv('CHAT_ID')

    def send_video(self, video_path='record_files/video.mp4'):
        ''' Send video to telegram chat '''
        self.bot.send_video(
            chat_id=self.chat_id,
            video=open('record_files/video.mp4', 'rb'),
            supports_streaming=True
        )

    def get_bot_updates(self):
        updates = self.bot.get_updates()
        print([u.message.text for u in updates])

    