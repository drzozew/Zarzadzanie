from DB_funckje import DB_Python_czas as DB
from add_data_time import get_data, get_time


class Python_time_choises():

    def choice_1(self):
        data_base = DB()
        data_base.create_table()
        data_base.add_data(get_data(), get_time())
