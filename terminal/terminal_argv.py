from sys import argv
from src.data_base.data_base_functions import DataBase as DBF
from src.menu.menu import Menu

if len(argv) > 1 and argv[1] == 'setup':
    print('Tworze baze danych')
    db = DBF('SQLite3.db')
