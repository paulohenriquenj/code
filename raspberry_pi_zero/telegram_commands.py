import logging 
import os.path

class telegram_commands:

    def __init__(self):
        self.register_allowed_commans()

    # def register_allowed_commans(self):
    #     self.allowed_commands = {
    #         '/status': 'camera_send_record',
    #         '/fan_off': 'fans_off',
    #         '/fan_on': 'fans_on',
    #         '/print_off': 'print_off',
    #     }

    # def is_allowed_command(self, command):
    #     return command in self.allowed_commands

    # def camera_send_record(self):

    #     record_video().record_video_time(10)

    #     logging.info('Send video!')
    #     self.telegram.send_video()

    # def fans_off(self):
    #     print('fans_off')

    # def fans_on(self):
    #     print('fans_on')

    # def print_off(self):
    #     print('print_off')

    def exec(self, update, telegram):
        self.telegram = telegram
        print("\n")
        print(update)
        print("\n")

        if self.is_msg_id_greater_than_last_executed(update):
            logging.info('Msg id is not grater than last executes id')
            return

        self.write_message_id(update)

        if self.is_allowed_command(update.message.text):
            getattr(self, self.allowed_commands[update.message.text])()
            return

        logging.warning(f'Command [{update.message.text}] not found')

    def is_msg_id_greater_than_last_executed(self, update):
        if os.path.isfile('msg_last_executed_id'):
            file_id = open('msg_last_executed_id', 'r')
            content = file_id.read()
            file_id.close()

            if content and  int(content) >= update.message.message_id:
                return True

        return False


    def write_message_id(self, update):
        file_id = open("msg_last_executed_id", 'w')
        file_id.write(str(update.message.message_id))
        file_id.close()
