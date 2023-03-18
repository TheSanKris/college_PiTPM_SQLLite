import sqlite3
from sqlite3 import Error

def connect (name):

    try:
        connect = sqlite3.connect("{name}.db")

        print("Соединение установлено: база данных создана в памяти")

    except Error:
        print(Error)   
    
    finally:
        connect.close()

def create_table(name, connect):

    cursor = connect.cursor()
    cursor.execute("CREATE TABLE {name}(id integer PRIMARY KEY, name text)")
    connect.commit()
    print("Таблица {name} успешно создана!")

def insert(value, table, connect):

    cursor = connect.cursor()
    cursor.execute("INSERT INTO {table} VALUES({value})")
    connect.commit()
    print("Таблица {name} успешно создана!")

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
