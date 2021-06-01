from sys import argv
from src.data_base.data_base_functions import DataBase as DBF
from src.menu.menu import Menu

if len(argv) > 1 and argv[1] == '-p':
    print('Dodaje czas Python wczoraj')
