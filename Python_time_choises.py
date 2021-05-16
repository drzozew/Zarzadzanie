from DB_funckje import DB_Python_czas as DB
from add_data_time import get_data, get_time, add_cash
from data_operation import *
from charts_options import wykres


class Python_time_choises():

    def __init__(self):
        self.db = DB()

    def seperator(self):
        print("\n"*2)
        print("-"*60)
        print("\n"*2)

    def choice_1(self):
        data_base = self.db
        data_base.create_table()
        data_base.add_data(get_data(), get_time())

    def choice_3_1(self):
        DB_fun = self.db
        print("Wybierz datę od: ")
        datafiltr_1 = get_data()
        print("Wybierz datę do: ")
        datafiltr_2 = get_data()
        time_list = DB_fun.selec_data(datafiltr_1, datafiltr_2)
        time_sum = time_paras(time_list)
        print(
            f"\nNa nauke Python od {datafiltr_1} do "
            f"{datafiltr_2} przeznaczyłeś {time_sum}\n")
        self.seperator()

    def choice_3_2(self):
        DB_fun = self.db
        time_list = DB_fun.selec_data()
        time_sum = time_paras(time_list)
        print(f"\nŁącznie na nauke Pythona przeznaczyłeś {time_sum}")
        self.seperator()

    def choice_3_3(self):
        DB_fun = self.db
        time_list = DB_fun.selec_data()
        lista_czasu = time_in_seconds_list(time_list)
        wykres(lista_czasu)

    def choice_4_1(self):
        DB_fun = self.db
        time_list = DB_fun.selec_data()
        money_per_hour = 0.2
        time_value = money_for_time(time_list, money_per_hour)
        if time_value == 0:
            pass
        else:
            result = round(time_value, 2)
            print(f"Łącznie za naukę przysługuje {result} zł.")
        self.seperator()

    def choice_4_2(self):
        DB_fun = self.db
        time_list = DB_fun.selec_data()
        money_per_hour = 0.2
        time_value = money_for_time(time_list, money_per_hour)
        cash_out_list = DB_fun.selec_cash()
        money_left(cash_out_list, time_value)
        self.seperator()

    def choice_4_3(self):
        DB_fun = self.db
        DB_fun.create_table_cash()
        data = get_data()
        cash = add_cash()
        DB_fun.add_cash(data, cash)
        self.seperator()
