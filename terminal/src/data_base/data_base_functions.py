import sqlite3
from sys import argv


class DataBase:
    """creating database and tables from data input"""

    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    # def creat_tabel(self, tabel_name: str, *args: dict):
    #     sqlite_create_table_data = 
    #     sqlite_create_table_query = f"CREATE TABLE {tabel_name}"
    #                                 f"()"