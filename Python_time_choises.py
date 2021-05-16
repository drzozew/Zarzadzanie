from DB_funckje import DB_Python_czas as DB
from add_data_time import get_data, get_time
from data_operation import *


class Python_time_choises():

    def __init__(self):
        self.db = DB()

    def choice_1(self):
        data_base = self.db
        data_base.create_table()
        data_base.add_data(get_data(), get_time())

    def choice_3_1(self):
        DB_fun = self.db
        print("Wybierz datę od: ")
        data_filtr_1 = get_data()
        print("Wybierz datę do: ")
        data_filtr_2 = get_data()
        time_list = DB_fun.selec_data(data_filtr_1, data_filtr_2)
        time_sum = time_paras(time_list)
        print(
            f"Na nauke Python od {data_filtr_1} do {data_filtr_2} przeznaczyłeś {time_sum}")

        # elif choice == 2:
        #     DB_fun = DB_object
        #     time_list = DB_fun.selec_data()
        #     time_sum = time_paras(time_list)
        #     print(f"Łącznie na nauke Pythona przeznaczyłeś {time_sum}")
        #     self.come_back(3)
        # elif choice == 3:
        #     DB_fun = DB_object
        #     time_list = DB_fun.selec_data()
        #     lista_czasu = time_in_seconds_list(time_list)
        #     print(lista_czasu)
        #     wykres(lista_czasu)
        #     self.come_back(3)
        # elif choice == 4:
        #     self.run_menu()
