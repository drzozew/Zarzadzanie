from sys import argv
from python_time.python_time_choises import Python_time_choises as PTC
from datetime import date, timedelta
from lib.db_functions import DB_Python_czas as DBP
from lib.db_functions import DB_Niemiecki as DBN
from lib.db_functions import DB_Drink as DBD

if len(argv) > 1 and argv[1] == 'python_chart':
    x = PTC()
    x.choice_2_3()
    exit()

if len(argv) > 1 and argv[1] == 'python':
    x = PTC()
    x.choice_1_1()
    exit()

if len(argv) > 1 and argv[1] == '-p':
    print(f"Dodane czas nauki Python z wczoraj {argv[2]}")
    yesterday = date.today() - timedelta(days=1)
    # adding data to Python DB
    add_data = DBP()
    add_data.add_data(yesterday, argv[2])
    exit()

if len(argv) > 1 and argv[1] == '-p0':
    print("Dodane czas nauki Python z wczoraj 00:00:00")
    yesterday = date.today() - timedelta(days=1)
    # adding data to Python DB
    add_data = DBP()
    add_data.add_data(yesterday, '00:00:00')
    exit()

if len(argv) > 1 and argv[1] == '-n':
    print(f"Dodane czas nauki Niemiecki z wczoraj {argv[2]}")
    yesterday = date.today() - timedelta(days=1)
    # adding data to Niemiecki DB
    add_data = DBN()
    add_data.add_data(yesterday, argv[2])
    exit()

if len(argv) > 1 and argv[1] == '-n0':
    print(f"Dodane czas nauki Niemiecki z wczoraj 00:00:00")
    yesterday = date.today() - timedelta(days=1)
    # adding data to Niemiecki DB
    add_data = DBN()
    add_data.add_data(yesterday, '00:00:00')
    exit()

if len(argv) > 1 and argv[1] == '-d':
    print(f"Dodane napoje z wczoraj kupiłem: {argv[2]} dosałem: {argv[3]}")
    yesterday = date.today() - timedelta(days=1)
    # adding data to drinks DB
    add_data = DBD()
    add_data.add_data(yesterday, argv[2], argv[3])
    exit()

if argv[1] == 'help':
    print("* 'python_chart' odpala wykres czasy pythona")
    print("* 'python' odpala dodawanie czasu nauki dla pythona")
    print("* -p 00:00:00 lub -p0 jeżeli wczoraj nci nie było dla pythona")
    print("* -p 00:00:00 lub -d0 jeżeli wczoraj nic nie było dla niemieckiego")
    print("* -d nie nie doda z wczoraj dla dink")
