import datetime


def get_data():
    try:
        date_entry = input("Podaj datę w formacje RRRR-MM-DD: ")
        year, month, day = map(int, date_entry.split('-'))
        date1 = datetime.date(year, month, day)
        return date1
    except ValueError:
        print("Nie ma takiej daty, wprowadź datę raz jeszcze.")
        return get_data()


def get_time():
    try:
        time_enter = input("Podaj czas w formacie GG-MM-SS: ").strip()
        hour, minute, second = map(int, time_enter.split('-'))
        get_time1 = datetime.time(hour, minute, second)
        return get_time1
    except ValueError:
        print("Nie ma takiej godziny, wprowadź godzinę raz jeszcze.")
        return get_time()


def add_cash():
    try:
        cash_enter = int(input("Wpisz wypłaconą kase: ").strip())
        return cash_enter
    except ValueError:
        print("Wprowadzona wartość musi być liczbą.")
        return add_cash()


def add_tak_nie():
    data_enter = input("Czy kupiłem słodki napój ?: ")
    if data_enter == 'tak' or data_enter == 'nie':
        return data_enter
    else:
        print('Wprowadzona wartość musi być "tak" lub "nie"/n/n')
        return add_tak_nie()


def add_tak_nie2():
    data_enter = input("Czy dostałem słodki napój ?: ")
    if data_enter == 'tak' or data_enter == 'nie':
        return data_enter
    else:
        print('Wprowadzona wartość musi być "tak" lub "nie"/n/n')
        return add_tak_nie2()
