from sys import argv
from python_time.python_time_choises import Python_time_choises as PTC


if len(argv) > 1 and argv[1] == 'python_chart':
    x = PTC()
    x.choice_2_3()
    exit()

if len(argv) > 1 and argv[1] == 'python':
    x = PTC()
    x.choice_1_1()
    exit()

if len(argv) > 1:
    help = input("Nothing happend, for help input help or h: \n").strip()
    if help == 'help' or help == 'h':
        print("help")
    else:
        pass
