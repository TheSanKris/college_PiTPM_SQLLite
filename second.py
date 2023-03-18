import sqlite3
from sqlite3 import Error

def connect (name):

    try:
        connect = sqlite3.connect(f"{name}.db")

        print("Соединение установлено: база данных создана в памяти")

    except Error:
        print(Error)   
    
    finally:
        connect.close()

def create_table(name, connect):

    cursor = connect.cursor()
    cursor.execute(f"CREATE TABLE {name}(id integer PRIMARY KEY, name text)")
    connect.commit()
    print(f"Таблица {name} успешно создана!")

def insert(value, table, connect):

    cursor = connect.cursor()
    cursor.execute(f"INSERT INTO {table} VALUES({value})")
    connect.commit()
    print(f"Значение {value} успешно добавлено в таблицу {table}!")

def disconnect(connect):

    connect.close()

connect("DataBase2")
create_table("Strits", connect)
insert("Советская", "Strits", connect)
insert("Ленина", "Strits", connect)
insert("Первомайская", "Strits", connect)
insert("Гоголя", "Strits", connect)
insert("Чехова", "Strits", connect)
disconnect()
