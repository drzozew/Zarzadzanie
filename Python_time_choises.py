from DB_funckje import DB_Python_czas as DB
from add_data_time import get_data, get_time


class Python_time_choises():

    def choice_1(self):
        print("tutaj2")
        data_base = DB()
        data_base.create_table()
        data_base.add_data(get_data(), get_time())
        # message = "Czy dodać kolejne dane ? 1 - TAK , 2 - NIE: "
        # error_msg = "Wybór musi być liczbą od 1 do 2."
        # choice = self.is_number(error_msg, message, 2)
