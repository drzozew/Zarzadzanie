import os
from Python_time_choises import Python_time_choises as PTC


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


class Main_Menu(Menu):

    def __init__(self):
        self.menu_options = ['\n1. Czas nauki Python',
                             '2. Czas nauki Niemiecki',
                             '3. Historia słodkich napojów',
                             '4. Zamknij program\n']
        self.error_msg = "Wybór musi być liczbą od 1 do 4"
        self.msg = "Wprowadź liczbę od 1 do 4 aby przejść dalej: "

    def run_menu(self):
        choice = self.menu_view(
            self.menu_options, self.error_msg, self.msg, True)
        return(choice)

    def choices(self):
        choice = self.run_menu()
        if choice == 1:
            x = Python_time_menu()
            x.choices()
        elif choice == 2:
            print("dwa")
        elif choice == 3:
            print("trzy")
        elif choice == 4:
            exit()
        else:
            print('cos poszło nie tak z Main_Menu')
            self.choices()


class Python_time_menu(Menu):

    def __init__(self):
        self.menu_options = ["1. Dodaj czas i datę nauki Pythona",
                             "2. Edytuj czas i datę nauki Pythona",
                             "3. Wyświetl dane",
                             "4. Kasa za czas nauki",
                             "5. Wyświetl podsumowanie danych",
                             "6. Wróć do głównego menu",
                             "7. Zamknij program\n"]
        self.error_msg = "Wybór musi być liczbą od 1 do 7"
        self.msg = "Wprowadź liczbę od 1 do 7 aby przejść dalej: "

    def run_menu(self):
        choice = self.menu_view(
            self.menu_options, self.error_msg, self.msg, True)
        return(choice)

    def choices(self):
        choice = self.run_menu()
        if choice == 1:
            print('pretu')
            x = Python_time_menu_choice_1()
            x.choices()
        elif choice == 2:
            print("dwa")
        elif choice == 3:
            print("trzy")
        elif choice == 4:
            print("trzy")
        elif choice == 5:
            print("trzy")
        elif choice == 6:
            x = Main_Menu()
            x.choices()
        elif choice == 7:
            exit()
        else:
            print('cos poszło nie tak z Main_Menu')
            self.choices()


class Python_time_menu_choice_1(Menu):

    def __init__(self):
        self.menu_options = ['\n1. Dodaj datę i czas',
                             '2. Wróć do poprzedniego menu',
                             '3. Zamknij program\n']
        self.error_msg = "Wybór musi być liczbą od 1 do 3"
        self.msg = "Wprowadź liczbę od 1 do 3 aby przejść dalej: "

    def run_menu(self):
        choice = self.menu_view(
            self.menu_options, self.error_msg, self.msg, True)
        return(choice)

    def choices(self):
        choice = self.run_menu()
        if choice == 1:
            print('tutaj')
            x = PTC()
            x.choice_1()
        elif choice == 2:
            x = Python_time_menu()
            x.choices()
        elif choice == 3:
            exit()
        else:
            print('cos poszło nie tak z Main_Menu')
            self.choices()


main_program = Main_Menu()
main_program.choices()
