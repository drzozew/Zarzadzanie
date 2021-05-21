from sys import argv
from python_time.python_time_choises import Python_time_choises as PTC


if len(argv) > 1 and argv[1] == 'python_chart':
    x = PTC()
    x.choice_2_3()

if len(argv) > 1 and argv[1] == 'python':
    x = PTC()
    x.choice_1_1()