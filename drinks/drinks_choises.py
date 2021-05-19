from lib.db_functions import DB_Drink as DB
from lib.add_data_time import *
from python_time.python_data_operation import *
from lib.charts_options import wykres2


class Drinks_choises():

    def __init__(self):
        self.db = DB()

    def seperator(self):
        print("\n"*2)
        print("-"*60)
        print("\n"*2)

    def choice_1_1(self):
        data_base = self.db
        data_base.create_table()
        data_base.add_data(get_data(), add_tak_nie(), add_tak_nie2())

    # def choice_2_1(self):
    #     DB_fun = self.db
    #     print("Wybierz datę od: ")
    #     datafiltr_1 = get_data()
    #     print("Wybierz datę do: ")
    #     datafiltr_2 = get_data()
    #     data = DB_fun.selec_data(datafiltr_1, datafiltr_2)
    #     time_list = [line for line in data[1::2]]
    #     time_sum = time_paras(time_list)
    #     print(
    #         f"\nNa nauke Niemieckiego od {datafiltr_1} do "
    #         f"{datafiltr_2} przeznaczyłeś {time_sum}\n")
    #     self.seperator()

    # def choice_2_2(self):
    #     DB_fun = self.db
    #     data = DB_fun.selec_data()
    #     time_list = [line for line in data[1::2]]
    #     time_sum = time_paras(time_list)
    #     print(f"\nŁącznie na nauke Niemieckiego przeznaczyłeś {time_sum}")
    #     self.seperator()

    # def choice_2_3(self):
    #     DB_fun = self.db
    #     data = DB_fun.selec_data()
    #     data_list = [line for line in data[0::2]]
    #     time_list = [line for line in data[1::2]]
    #     lista_czasu = time_in_mins_list(time_list)
    #     wykres2(lista_czasu, data_list)

    def choice_3_1(self):
        DB_fun = self.db
        data = DB_fun.selec_data_drinks()
        cash = 0
        try:
            yes = data.count('tak')
            no = data.count('nie')
            money_per_yes = 10
            money_per_no = 0.85
            cash = ((no*money_per_no)-(yes*money_per_yes))
        except AttributeError:
            pass
        if cash == 0:
            pass
        else:
            print(f"Łącznie za naukę przysługuje {cash} zł.")
        self.seperator()

    def choice_3_2(self):
        DB_fun = self.db
        data = DB_fun.selec_data_drinks()
        cash1 = 0
        try:
            yes = data.count('tak')
            no = data.count('nie')
            money_per_yes = 10
            money_per_no = 0.85
            cash1 = ((no*money_per_no)-(yes*money_per_yes))
        except AttributeError:
            pass
        cash_out = 0
        money_leftt = None
        try:
            cash_out_list = DB_fun.selec_cash()
            for cash in cash_out_list:
                cash_out = cash_out + int(cash)
            money_leftt = (cash1 - cash_out)
            print(f'Można jeszcze wypłacić {round(money_leftt, 2)} zł')
        except TypeError:
            pass

        self.seperator()

    def choice_3_3(self):
        DB_fun = self.db
        DB_fun.create_table_cash()
        data = get_data()
        cash = add_cash()
        DB_fun.add_cash(data, cash)
        self.seperator()
