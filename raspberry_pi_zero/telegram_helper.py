import telegram
import os
from dotenv import load_dotenv
load_dotenv()


class telegram_helper:

    def __init__(self):
        self.bot = telegram.Bot(token=os.getenv('TELEGRAM_TOKEN'))
        self.chat_id = os.getenv('CHAT_ID')
        self.users = os.getenv('AUTHORIZED_USERS')

    def send_video(self, video_path='record_files/video.mp4'):
        ''' Send video to telegram chat '''
        self.bot.send_video(
            chat_id=self.chat_id,
            video=open('record_files/video.mp4', 'rb'),
            supports_streaming=True
        )

    def get_bot_updates(self):
        updates = self.bot.get_updates()

        for update in updates:

            if self.is_msg_from_authorized_user(update.message.from_user_name):
                self.exec_command(update)
            #print(dir(update.channel_post))
            print('------')
            print(update.update_id)
            print(update.message.text)
            print(update.username)
            #print(update.channel_post.chat.id)
            print('------')

        #print(dir(updates))
        #print([u.message.text for u in updates])

    def get_channel_msg(self):
        print(self.bot.get_updates())

    def is_msg_from_authorized_user(self, user_name):
        if self.users == '*':
            return True
        
        if user_name in self.users:
            return True

        return False

    def exec_command(self, update):
        pass


t = telegram_helper()
t.get_bot_updates()