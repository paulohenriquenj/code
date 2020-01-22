import logging 

class commands:

    def __init__(self):
        self.register_allowed_commans()

    def register_allowed_commans(self):
        self.allowed_commands = {
            '/status': 'camera_send_record',
            '/fan_off': 'fans_off',
            '/fan_on': 'fans_on',
            '/print_off': 'print_off',
        }

    def is_allowed_command(self, command):
        return command in self.allowed_commands

    def camera_send_record(self):
        print('la la la la')

    def fans_off(self):
        print('fans_off')

    def fans_on(self):
        print('fans_on')

    def print_off(self):
        print('print_off')

    def exec(self, update):
        print("\n")
        print(update)
        print("\n")

        if self.is_allowed_command(update.message.text):
            getattr(self, self.allowed_commands[update.message.text])()
            return
        
        logging.warning(f'Command [{update.message.text}] not found')
        
