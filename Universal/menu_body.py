import os


class Menu():
    """creating basic menu functions"""

    def is_number(self, error_msg, message, options_len):
        """check is input number and in range of menu options"""
        try:
            choice = int(input(message))
            if choice in range(1, options_len+1):
                return choice
            else:
                print(error_msg)
                return self.is_number(error_msg, message, options_len)
        except ValueError:
            print(error_msg)
            return self.is_number(error_msg, message, options_len)

    def clean(self): return os.system('clear')

    def menu_view(self, options, error_msg, message, clear):
        for option in options:
            print(option)
        choice = self.is_number(error_msg, message, len(options))
        if clear is True:
            self.clean()
        return(choice)
