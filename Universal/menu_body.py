import os


class Menu():
    """creating basic menu functions"""

    def is_number(self, options_len):
        """check is input number and in range of menu options"""
        error_msg = f"Wybór musi być liczbą od 1 do {options_len}"
        msg = f"Wprowadź liczbę od 1 do {options_len} aby przejść dalej: "
        try:
            choice = int(input(msg))
            if choice in range(1, options_len+1):
                return choice
            else:
                print(error_msg)
                return self.is_number(error_msg, msg, options_len)
        except ValueError:
            print(error_msg)
            return self.is_number(error_msg, msg, options_len)

    def clean(self): return os.system('clear')

    def menu_view(self, options, clear, menu_title):
        print(menu_title)
        for option in options:
            print(option)
        choice = self.is_number(len(options))
        if clear is True:
            self.clean()
        return(choice)
