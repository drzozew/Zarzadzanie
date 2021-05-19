import sqlite3


class DB_Python_czas():
    def __init__(self, path="/home/drzozew/Desktop/Projekty/Zarzadzanie/SQLite_Python.db"):
        self.path = path

    def create_DB(self):
        try:
            sqliteConnection = sqlite3.connect(self.path)
        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            return sqliteConnection
            # if sqliteConnection:
            #     sqliteConnection.close()
            #     print("sqlite connection is closed")

    def create_table(self):

        sqliteConnection = self.create_DB()

        sqlite_create_table_query = '''CREATE TABLE SqliteDb_pythonTime (
                                        data datatime NOT NULL,
                                        time TEXT NOT NULL);'''

        cursor = sqliteConnection.cursor()
        # print("Successfully Connected to SQLite")
        try:
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            # print("SQLite table created")
        except sqlite3.OperationalError as error:
            pass

        if sqliteConnection:
            sqliteConnection.close()
            # print("sqlite connection is closed")

    def create_table_cash(self):

        sqliteConnection = self.create_DB()

        sqlite_create_table_query = '''CREATE TABLE SqliteDb_pythonCash (
                                        data datatime NOT NULL,
                                        cash TEXT NOT NULL);'''

        cursor = sqliteConnection.cursor()
        # print("Successfully Connected to SQLite")
        try:
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            # print("SQLite table created")
        except sqlite3.OperationalError as error:
            # print(error)
            pass

        if sqliteConnection:
            sqliteConnection.close()
            # print("sqlite connection is closed")

    def add_data(self, data, time):
        sqliteConnection = self.create_DB()
        cursor = sqliteConnection.cursor()
        # print("Successfully Connected to SQLite")

        sqlite_insert_query = """INSERT INTO SqliteDb_pythonTime
                                (data, time)
                                VALUES
                                (?,?);"""

        data_tuple = (str(data), str(time))
        count = cursor.execute(sqlite_insert_query, data_tuple)
        sqliteConnection.commit()
        cursor.close()

        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")

    def add_cash(self, data, cash):
        sqliteConnection = self.create_DB()
        cursor = sqliteConnection.cursor()
        # print("Successfully Connected to SQLite")

        sqlite_insert_query = """INSERT INTO SqliteDb_pythonCash
                                (data, cash)
                                VALUES
                                (?,?);"""

        cash_tuple = (str(data), str(cash))
        count = cursor.execute(sqlite_insert_query, cash_tuple)
        sqliteConnection.commit()
        cursor.close()

        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")

    def selec_data(self, data_filtr_1=0, data_filtr_2=0):
        data_list = []

        try:
            sqliteConnection = self.create_DB()
            cursor = sqliteConnection.cursor()

            sqlite_select_query = """SELECT * from SqliteDb_pythonTime WHERE data >= ? AND data <= ?"""
            sqlite_select_query_2 = """SELECT * from SqliteDb_pythonTime"""

            if data_filtr_1 == 0 and data_filtr_2 == 0:
                cursor.execute(sqlite_select_query_2)
            else:
                cursor.execute(sqlite_select_query,
                               (data_filtr_1, data_filtr_2))
            records = cursor.fetchall()
            cursor.close()

            for row in records:
                data = row[0]
                time = row[1]
                data_list.append(data)
                data_list.append(time)

            cursor.close()
            return data_list
            # print(f"Dnia {data} było {time} czasu nauki Pythona")
            # print("data typ", type(data))
            # print("time typ", type(time))

            if sqliteConnection:
                sqliteConnection.close()
                # print("sqlite connection is closed")
        except sqlite3.Error as e:
            print("W bazie nie ma danych, musisz wpierw coś wprowadzić")

    def selec_cash(self, data_filtr_1=0, data_filtr_2=0):
        data_list = []

        try:
            sqliteConnection = self.create_DB()
            cursor = sqliteConnection.cursor()

            sqlite_select_query = """SELECT * from SqliteDb_pythonCash WHERE data >= ? AND data <= ?"""
            sqlite_select_query_2 = """SELECT * from SqliteDb_pythonCash"""

            if data_filtr_1 == 0 and data_filtr_2 == 0:
                cursor.execute(sqlite_select_query_2)
            else:
                cursor.execute(sqlite_select_query,
                               (data_filtr_1, data_filtr_2))
            records = cursor.fetchall()
            cursor.close()

            for row in records:
                data = row[0]
                time = row[1]
                # dic = {data: time}
                # data_list.append(dic)
                data_list.append(time)

            cursor.close()
            return data_list
            # print(f"Dnia {data} było {time} czasu nauki Pythona")
            # print("data typ", type(data))
            # print("time typ", type(time))

            if sqliteConnection:
                sqliteConnection.close()
                # print("sqlite connection is closed")
        except sqlite3.Error as e:
            print("W bazie nie ma danych, musisz wpierw coś wprowadzić")

    def selec_data(self, data_filtr_1=0, data_filtr_2=0):
        data_list = []

        try:
            sqliteConnection = self.create_DB()
            cursor = sqliteConnection.cursor()

            sqlite_select_query = """SELECT * from SqliteDb_pythonTime WHERE data >= ? AND data <= ?"""
            sqlite_select_query_2 = """SELECT * from SqliteDb_pythonTime"""

            if data_filtr_1 == 0 and data_filtr_2 == 0:
                cursor.execute(sqlite_select_query_2)
            else:
                cursor.execute(sqlite_select_query,
                               (data_filtr_1, data_filtr_2))
            records = cursor.fetchall()
            cursor.close()

            for row in records:
                data = row[0]
                time = row[1]
                data_list.append(data)
                data_list.append(time)

            cursor.close()
            return data_list
            # print(f"Dnia {data} było {time} czasu nauki Pythona")
            # print("data typ", type(data))
            # print("time typ", type(time))

            if sqliteConnection:
                sqliteConnection.close()
                # print("sqlite connection is closed")
        except sqlite3.Error as e:
            print("W bazie nie ma danych, musisz wpierw coś wprowadzić")

    def selec_cash(self, data_filtr_1=0, data_filtr_2=0):
        data_list = []

        try:
            sqliteConnection = self.create_DB()
            cursor = sqliteConnection.cursor()

            sqlite_select_query = """SELECT * from SqliteDb_pythonCash WHERE data >= ? AND data <= ?"""
            sqlite_select_query_2 = """SELECT * from SqliteDb_pythonCash"""

            if data_filtr_1 == 0 and data_filtr_2 == 0:
                cursor.execute(sqlite_select_query_2)
            else:
                cursor.execute(sqlite_select_query,
                               (data_filtr_1, data_filtr_2))
            records = cursor.fetchall()
            cursor.close()

            for row in records:
                data = row[0]
                time = row[1]
                # dic = {data: time}
                # data_list.append(dic)
                data_list.append(time)

            cursor.close()
            return data_list
            # print(f"Dnia {data} było {time} czasu nauki Pythona")
            # print("data typ", type(data))
            # print("time typ", type(time))

            if sqliteConnection:
                sqliteConnection.close()
                # print("sqlite connection is closed")
        except sqlite3.Error as e:
            print("blad")


class DB_Niemiecki():
    def __init__(self, path="/home/drzozew/Desktop/Projekty/Zarzadzanie/SQLite_Python.db"):
        self.path = path

    def create_DB(self):
        try:
            sqliteConnection = sqlite3.connect(self.path)
        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            return sqliteConnection
            # if sqliteConnection:
            #     sqliteConnection.close()
            #     print("sqlite connection is closed")

    def create_table(self):

        sqliteConnection = self.create_DB()

        sqlite_create_table_query = '''CREATE TABLE SqliteDb_German_Time (
                                        data datatime NOT NULL,
                                        time TEXT NOT NULL);'''

        cursor = sqliteConnection.cursor()
        # print("Successfully Connected to SQLite")
        try:
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            # print("SQLite table created")
        except sqlite3.OperationalError as error:
            pass

        if sqliteConnection:
            sqliteConnection.close()
            # print("sqlite connection is closed")

    def create_table_cash(self):

        sqliteConnection = self.create_DB()

        sqlite_create_table_query = '''CREATE TABLE SqliteDb_GermanCash (
                                        data datatime NOT NULL,
                                        cash TEXT NOT NULL);'''

        cursor = sqliteConnection.cursor()
        # print("Successfully Connected to SQLite")
        try:
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            # print("SQLite table created")
        except sqlite3.OperationalError as error:
            # print(error)
            pass

        if sqliteConnection:
            sqliteConnection.close()
            # print("sqlite connection is closed")

    def add_data(self, data, time):
        sqliteConnection = self.create_DB()
        cursor = sqliteConnection.cursor()
        # print("Successfully Connected to SQLite")

        sqlite_insert_query = """INSERT INTO SqliteDb_German_Time
                                (data, time)
                                VALUES
                                (?,?);"""

        data_tuple = (str(data), str(time))
        count = cursor.execute(sqlite_insert_query, data_tuple)
        sqliteConnection.commit()
        cursor.close()

        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")

    def add_cash(self, data, cash):
        sqliteConnection = self.create_DB()
        cursor = sqliteConnection.cursor()
        # print("Successfully Connected to SQLite")

        sqlite_insert_query = """INSERT INTO SqliteDb_GermanCash
                                (data, cash)
                                VALUES
                                (?,?);"""

        cash_tuple = (str(data), str(cash))
        count = cursor.execute(sqlite_insert_query, cash_tuple)
        sqliteConnection.commit()
        cursor.close()

        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")

    def selec_data(self, data_filtr_1=0, data_filtr_2=0):
        data_list = []

        try:
            sqliteConnection = self.create_DB()
            cursor = sqliteConnection.cursor()

            sqlite_select_query = """SELECT * from SqliteDb_German_Time WHERE data >= ? AND data <= ?"""
            sqlite_select_query_2 = """SELECT * from SSqliteDb_German_Time"""

            if data_filtr_1 == 0 and data_filtr_2 == 0:
                cursor.execute(sqlite_select_query_2)
            else:
                cursor.execute(sqlite_select_query,
                               (data_filtr_1, data_filtr_2))
            records = cursor.fetchall()
            cursor.close()

            for row in records:
                data = row[0]
                time = row[1]
                data_list.append(data)
                data_list.append(time)

            cursor.close()
            return data_list
            # print(f"Dnia {data} było {time} czasu nauki Pythona")
            # print("data typ", type(data))
            # print("time typ", type(time))

            if sqliteConnection:
                sqliteConnection.close()
                # print("sqlite connection is closed")
        except sqlite3.Error as e:
            print("W bazie nie ma danych, musisz wpierw coś wprowadzić")

    def selec_cash(self, data_filtr_1=0, data_filtr_2=0):
        data_list = []

        try:
            sqliteConnection = self.create_DB()
            cursor = sqliteConnection.cursor()

            sqlite_select_query = """SELECT * from SqliteDb_GermanCash WHERE data >= ? AND data <= ?"""
            sqlite_select_query_2 = """SELECT * from SqliteDb_GermanCash"""

            if data_filtr_1 == 0 and data_filtr_2 == 0:
                cursor.execute(sqlite_select_query_2)
            else:
                cursor.execute(sqlite_select_query,
                               (data_filtr_1, data_filtr_2))
            records = cursor.fetchall()
            cursor.close()

            for row in records:
                data = row[0]
                time = row[1]
                # dic = {data: time}
                # data_list.append(dic)
                data_list.append(time)

            cursor.close()
            return data_list
            # print(f"Dnia {data} było {time} czasu nauki Pythona")
            # print("data typ", type(data))
            # print("time typ", type(time))

            if sqliteConnection:
                sqliteConnection.close()
                # print("sqlite connection is closed")
        except sqlite3.Error as e:
            print("W bazie nie ma danych, musisz wpierw coś wprowadzić")

    def selec_data(self, data_filtr_1=0, data_filtr_2=0):
        data_list = []

        try:
            sqliteConnection = self.create_DB()
            cursor = sqliteConnection.cursor()

            sqlite_select_query = """SELECT * from SqliteDb_German_Time WHERE data >= ? AND data <= ?"""
            sqlite_select_query_2 = """SELECT * from SqliteDb_German_Time"""

            if data_filtr_1 == 0 and data_filtr_2 == 0:
                cursor.execute(sqlite_select_query_2)
            else:
                cursor.execute(sqlite_select_query,
                               (data_filtr_1, data_filtr_2))
            records = cursor.fetchall()
            cursor.close()

            for row in records:
                data = row[0]
                time = row[1]
                data_list.append(data)
                data_list.append(time)

            cursor.close()
            return data_list
            # print(f"Dnia {data} było {time} czasu nauki Pythona")
            # print("data typ", type(data))
            # print("time typ", type(time))

            if sqliteConnection:
                sqliteConnection.close()
                # print("sqlite connection is closed")
        except sqlite3.Error as e:
            print("W bazie nie ma danych, musisz wpierw coś wprowadzić")

    def selec_cash(self, data_filtr_1=0, data_filtr_2=0):
        data_list = []

        try:
            sqliteConnection = self.create_DB()
            cursor = sqliteConnection.cursor()

            sqlite_select_query = """SELECT * from SqliteDb_GermanCash WHERE data >= ? AND data <= ?"""
            sqlite_select_query_2 = """SELECT * from SqliteDb_GermanCash"""

            if data_filtr_1 == 0 and data_filtr_2 == 0:
                cursor.execute(sqlite_select_query_2)
            else:
                cursor.execute(sqlite_select_query,
                               (data_filtr_1, data_filtr_2))
            records = cursor.fetchall()
            cursor.close()

            for row in records:
                data = row[0]
                time = row[1]
                # dic = {data: time}
                # data_list.append(dic)
                data_list.append(time)

            cursor.close()
            return data_list
            # print(f"Dnia {data} było {time} czasu nauki Pythona")
            # print("data typ", type(data))
            # print("time typ", type(time))

            if sqliteConnection:
                sqliteConnection.close()
                # print("sqlite connection is closed")
        except sqlite3.Error as e:
            print("blad")


class DB_Drink():
    def __init__(self, path="/home/drzozew/Desktop/Projekty/Zarzadzanie/SQLite_Python.db"):
        self.path = path

    def create_DB(self):
        try:
            sqliteConnection = sqlite3.connect(self.path)
        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            return sqliteConnection
            # if sqliteConnection:
            #     sqliteConnection.close()
            #     print("sqlite connection is closed")

    def create_table(self):

        sqliteConnection = self.create_DB()

        sqlite_create_table_query = '''CREATE TABLE SqliteDb_Drinks (
                                        data datatime NOT NULL,
                                        kupilem TEXT NOT NULL,
                                        dostalem TEXT NOT NULL);'''

        cursor = sqliteConnection.cursor()
        # print("Successfully Connected to SQLite")
        try:
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            # print("SQLite table created")
        except sqlite3.OperationalError as error:
            pass

        if sqliteConnection:
            sqliteConnection.close()
            # print("sqlite connection is closed")

    def create_table_cash(self):

        sqliteConnection = self.create_DB()

        sqlite_create_table_query = '''CREATE TABLE SqliteDb_DrinksCash (
                                        data datatime NOT NULL,
                                        cash TEXT NOT NULL);'''

        cursor = sqliteConnection.cursor()
        # print("Successfully Connected to SQLite")
        try:
            cursor.execute(sqlite_create_table_query)
            sqliteConnection.commit()
            # print("SQLite table created")
        except sqlite3.OperationalError as error:
            # print(error)
            pass

        if sqliteConnection:
            sqliteConnection.close()
            # print("sqlite connection is closed")

    def add_data(self, data, kupilem, dostalem):
        sqliteConnection = self.create_DB()
        cursor = sqliteConnection.cursor()
        # print("Successfully Connected to SQLite")

        sqlite_insert_query = """INSERT INTO SqliteDb_Drinks
                                (data, kupilem, dostalem)
                                VALUES
                                (?,?,?);"""

        data_tuple = (str(data), str(kupilem), str(dostalem))
        count = cursor.execute(sqlite_insert_query, data_tuple)
        sqliteConnection.commit()
        cursor.close()

        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")

    def add_cash(self, data, cash):
        sqliteConnection = self.create_DB()
        cursor = sqliteConnection.cursor()
        # print("Successfully Connected to SQLite")

        sqlite_insert_query = """INSERT INTO SqliteDb_DrinksCash
                                (data, cash)
                                VALUES
                                (?,?);"""

        cash_tuple = (str(data), str(cash))
        count = cursor.execute(sqlite_insert_query, cash_tuple)
        sqliteConnection.commit()
        cursor.close()

        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")

    def selec_data_drinks(self, data_filtr_1=0, data_filtr_2=0):
        data_list = []

        try:
            sqliteConnection = self.create_DB()
            cursor = sqliteConnection.cursor()

            sqlite_select_query = """SELECT * from SqliteDb_Drinks WHERE data >= ? AND data <= ?"""
            sqlite_select_query_2 = """SELECT * from SqliteDb_Drinks"""

            if data_filtr_1 == 0 and data_filtr_2 == 0:
                cursor.execute(sqlite_select_query_2)
            else:
                cursor.execute(sqlite_select_query,
                               (data_filtr_1, data_filtr_2))
            records = cursor.fetchall()
            cursor.close()

            for row in records:
                data = row[1]
                time = row[2]
                # dic = {data: time}
                # data_list.append(dic)
                data_list.append(data)
                data_list.append(time)

            cursor.close()
            return data_list
            # print(f"Dnia {data} było {time} czasu nauki Pythona")
            # print("data typ", type(data))
            # print("time typ", type(time))

            if sqliteConnection:
                sqliteConnection.close()
                # print("sqlite connection is closed")
        except sqlite3.Error as e:
            print("W bazie nie ma danych, musisz wpierw coś wprowadzić")

    def selec_cash(self, data_filtr_1=0, data_filtr_2=0):
        data_list = []

        try:
            sqliteConnection = self.create_DB()
            cursor = sqliteConnection.cursor()

            sqlite_select_query = """SELECT * from SqliteDb_DrinksCash WHERE data >= ? AND data <= ?"""
            sqlite_select_query_2 = """SELECT * from SqliteDb_DrinksCash"""

            if data_filtr_1 == 0 and data_filtr_2 == 0:
                cursor.execute(sqlite_select_query_2)
            else:
                cursor.execute(sqlite_select_query,
                               (data_filtr_1, data_filtr_2))
            records = cursor.fetchall()
            cursor.close()

            for row in records:
                data = row[0]
                time = row[1]
                # dic = {data: time}
                # data_list.append(dic)
                data_list.append(time)

            cursor.close()
            return data_list
            # print(f"Dnia {data} było {time} czasu nauki Pythona")
            # print("data typ", type(data))
            # print("time typ", type(time))

            if sqliteConnection:
                sqliteConnection.close()
                # print("sqlite connection is closed")
        except sqlite3.Error as e:
            print("W bazie nie ma danych, musisz wpierw coś wprowadzić")

    def selec_data(self, data_filtr_1=0, data_filtr_2=0):
        data_list = []

        try:
            sqliteConnection = self.create_DB()
            cursor = sqliteConnection.cursor()

            sqlite_select_query = """SELECT * from SqliteDb_Drinks WHERE data >= ? AND data <= ?"""
            sqlite_select_query_2 = """SELECT * from SqliteDb_Drinks"""

            if data_filtr_1 == 0 and data_filtr_2 == 0:
                cursor.execute(sqlite_select_query_2)
            else:
                cursor.execute(sqlite_select_query,
                               (data_filtr_1, data_filtr_2))
            records = cursor.fetchall()
            cursor.close()

            for row in records:
                data = row[0]
                time = row[1]
                data_list.append(data)
                data_list.append(time)

            cursor.close()
            return data_list
            # print(f"Dnia {data} było {time} czasu nauki Pythona")
            # print("data typ", type(data))
            # print("time typ", type(time))

            if sqliteConnection:
                sqliteConnection.close()
                # print("sqlite connection is closed")
        except sqlite3.Error as e:
            print("W bazie nie ma danych, musisz wpierw coś wprowadzić")

    def selec_cash(self, data_filtr_1=0, data_filtr_2=0):
        data_list = []

        try:
            sqliteConnection = self.create_DB()
            cursor = sqliteConnection.cursor()

            sqlite_select_query = """SELECT * from SqliteDb_DrinksCash WHERE data >= ? AND data <= ?"""
            sqlite_select_query_2 = """SELECT * from SqliteDb_DrinksCash"""

            if data_filtr_1 == 0 and data_filtr_2 == 0:
                cursor.execute(sqlite_select_query_2)
            else:
                cursor.execute(sqlite_select_query,
                               (data_filtr_1, data_filtr_2))
            records = cursor.fetchall()
            cursor.close()

            for row in records:
                data = row[0]
                time = row[1]
                # dic = {data: time}
                # data_list.append(dic)
                data_list.append(time)

            cursor.close()
            return data_list
            # print(f"Dnia {data} było {time} czasu nauki Pythona")
            # print("data typ", type(data))
            # print("time typ", type(time))

            if sqliteConnection:
                sqliteConnection.close()
                # print("sqlite connection is closed")
        except sqlite3.Error as e:
            pass
