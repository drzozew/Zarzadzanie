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

    def menu_view(self, options, error_msg, message, clear, menu_title):
        print(menu_title)
        for option in options:
            print(option)
        choice = self.is_number(error_msg, message, len(options))
        if clear is True:
            self.clean()
        return(choice)


class Main_Menu(Menu):

    def __init__(self):
        self.menu_title = "Główe Menu\n"
        self.menu_options = ['1. Czas nauki Python',
                             '2. Czas nauki Niemiecki - TODO',
                             '3. Historia słodkich napojów - TODO',
                             '4. Zamknij program\n']
        self.error_msg = "Wybór musi być liczbą od 1 do 4"
        self.msg = "Wprowadź liczbę od 1 do 4 aby przejść dalej: "

    def choices(self):
        choice = self.menu_view(
            self.menu_options, self.error_msg, self.msg, True, self.menu_title)
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
        self.menu_title = "Python Czas\n"
        self.menu_options = ["1. Dodaj czas i datę nauki Pythona",
                             "2. Edytuj czas i datę nauki Pythona - TODO",
                             "3. Wyświetl dane",
                             "4. Kasa za czas nauki",
                             "5. Wyświetl podsumowanie danych - TODO",
                             "6. Wróć do głównego menu",
                             "7. Zamknij program\n"]
        self.error_msg = "Wybór musi być liczbą od 1 do 7"
        self.msg = "Wprowadź liczbę od 1 do 7 aby przejść dalej: "

    def choices(self):
        choice = self.menu_view(
            self.menu_options, self.error_msg, self.msg, True, self.menu_title)
        if choice == 1:
            x = Python_time_menu_choice_1()
            x.choices()
        elif choice == 2:
            print('do zrobienia')
        elif choice == 3:
            x = Python_time_menu_choice_3()
            x.choices()
        elif choice == 4:
            x = Python_time_menu_choice_4()
            x.choices()
        elif choice == 5:
            print('do zrobienia')
        elif choice == 6:
            x = Main_Menu()
            x.choices()
        elif choice == 7:
            exit()
        else:
            print('cos poszło nie tak z Main_Menu')
            self.choices()


class Python_time_menu_choice_1_1(Menu):

    def __init__(self):
        self.menu_title = ""
        self.menu_options = ['\n1. Dodać kolejne dane',
                             '2. Wrócić do poprzedniego menu',
                             '3. Zamknij program\n']
        self.error_msg = "Wybór musi być liczbą od 1 do 3"
        self.msg = "Wprowadź liczbę od 1 do 3 aby przejść dalej: "

    def choices(self):
        choice = self.menu_view(
            self.menu_options, self.error_msg, self.msg, True, self.menu_title)
        if choice == 1:
            x = PTC()
            x.choice_1()
            self.choices()
        elif choice == 2:
            x = Python_time_menu()
            x.choices()
        elif choice == 3:
            exit()
        else:
            print('cos poszło nie tak z Main_Menu')
            self.choices()


class Python_time_menu_choice_1(Menu):

    def __init__(self):
        self.menu_title = "Dodawanie czasu nauki\n"
        self.menu_options = ['\n1. Dodaj datę i czas',
                             '2. Wróć do poprzedniego menu',
                             '3. Zamknij program\n']
        self.error_msg = "Wybór musi być liczbą od 1 do 3"
        self.msg = "Wprowadź liczbę od 1 do 3 aby przejść dalej: "

    def choices(self):
        choice = self.menu_view(
            self.menu_options, self.error_msg, self.msg, True, self.menu_title)
        if choice == 1:
            y = PTC()
            y.choice_1()
            x = Python_time_menu_choice_1_1()
            x.choices()
        elif choice == 2:
            x = Python_time_menu()
            x.choices()
        elif choice == 3:
            exit()
        else:
            print('cos poszło nie tak z Main_Menu')
            self.choices()


class Python_time_menu_choice_3(Menu):

    def __init__(self):
        self.menu_title = "Wyświetlanie danych dotyczacych czasu nauki Python\n"
        self.menu_options = ['\n1. Wyświetl dane wg daty',
                             '2. Wyświetl łączny czas',
                             '3. Wyświetl wykres czasu',
                             '4. Wróć do poprzedniego menu',
                             '5. Zamknij program\n']
        self.error_msg = "Wybór musi być liczbą od 1 do 5"
        self.msg = "Wprowadź liczbę od 1 do 5 aby przejść dalej: "

    def choices(self):
        choice = self.menu_view(
            self.menu_options, self.error_msg, self.msg, True, self.menu_title)
        if choice == 1:
            x = PTC()
            x.choice_3_1()
            y = Python_time_menu_choice_3()
            y.choices()
        elif choice == 2:
            x = PTC()
            x.choice_3_2()
            y = Python_time_menu_choice_3()
            y.choices()
        elif choice == 3:
            x = PTC()
            x.choice_3_3()
            y = Python_time_menu_choice_3()
            y.choices()
        elif choice == 4:
            x = Python_time_menu()
            x.choices()
        elif choice == 5:
            exit()
        else:
            print('cos poszło nie tak z Main_Menu')
            self.choices()


class Python_time_menu_choice_4(Menu):

    def __init__(self):
        self.menu_title = "Wyświetlanie danych dotyczących kasy\n"
        self.menu_options = ['\n1. Wyświetl kase łącznie',
                             '2. Wyświetl ile jeszcze możesz wypłacić',
                             '3. Wypłać kase',
                             '4. Wróć do poprzedniego menu',
                             '5. Zamknij program\n']
        self.error_msg = "Wybór musi być liczbą od 1 do 5"
        self.msg = "Wprowadź liczbę od 1 do 5 aby przejść dalej: "

    def choices(self):
        choice = self.menu_view(
            self.menu_options, self.error_msg, self.msg, True, self.menu_title)
        if choice == 1:
            x = PTC()
            x.choice_4_1()
            y = Python_time_menu_choice_4()
            y.choices()
        elif choice == 2:
            x = PTC()
            x.choice_4_2()
            y = Python_time_menu_choice_4()
            y.choices()
        elif choice == 3:
            x = PTC()
            x.choice_4_3()
            y = Python_time_menu_choice_4()
            y.choices()
        elif choice == 4:
            x = Python_time_menu()
            x.choices()
        elif choice == 5:
            exit()
        else:
            print('cos poszło nie tak z Main_Menu')
            self.choices()


main_program = Main_Menu()
main_program.choices()


# przeniesc run_menu do clasy menu
# rozdzielic na pare plikow menu bo robi sie za gesto
# przeniesc eror msg do klasy menu ? i moze jakos msg tez
# mozna dodac linie celu w wykresie aby bylo wiadomo jak jestem blisko lub daleko celu
# rozbudowac sam wykres
# w python czas zajac sie 2 pkt czyli edycja, poprawi to moja prace na sqlite
# w python czas pomslec nad podsumowanie danych, nie wiem czy czasem tego nie usunac1
# wykres wg dat ?
# jak ogarne wszystko powzyej biore sie za niemiecki a potem za slodkie napoje
