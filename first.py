import sqlite3
import datetime
from sqlite3 import Error

def connect():
    
    try:
        connect = sqlite3.connect("DataBase.db")

        print("Соединение установлено: база данных создана в памяти")

    except Error:
        print(Error)   
    
    finally:
        connect.close()

def create_table(connect):
    
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
    connect.commit()

def insert_table1(connect):

    cursor = connect.cursor()
    cursor.execute("INSERT INTO employees VALUES(1, 'John', 700, 'HR', 'Manager', '2017-01-04')")
    connect.commit()

def insert_table2(connect):

    cursor = connect.cursor()
    entities = (2, 'Andrew', 800, 'IT', 'Tech', '2018-02-06')
    cursor.execute('''INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)''', entities)
    connect.commit()

def update_table(connect):

    cursor = connect.cursor()
    cursor.execute('UPDATE employees SET name = "Rogers" where id = 2')
    connect.commit()

def select1(connect):

    cursor = connect.cursor()
    cursor.execute('SELECT * FROM employees')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

def select2(connect):

    cursor = connect.cursor()
    cursor.execute('SELECT id, name FROM employees')
    row = cursor.fetchall()
    
    print(row)

def select3(connect):

    cursor = connect.cursor()
    cursor.execute('SELECT id, name FROM employees WHERE salary > 800.0')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

def count_row1(connect):

    cursor = connect.cursor()
    print(cursor.execute('SELECT * FROM employees').rowcount)

def count_row2(connect):

    cursor = connect.cursor()
    cursor.execute('SELECT * FROM employees')
    rows = cursor.fetchall()
    print(len(rows))

def list_table(connect):

    cursor = connect.cursor() 
    cursor.execute('SELECT name from sqlite_master where type= "table"') 
    print(cursor.fetchall())

def ok_table1(connect):

    cursor = connect.cursor() 
    cursor.execute('create table if not exists projects(id integer, name text)') 
    connect.commit()

def ok_table2(connect):

    cursor = connect.cursor() 
    cursor.execute('create table if not exists projects(id integer, name text)') 
    connect.commit()
    print(cursor.fetchall())

def delete_table(connect):

    cursor = connect.cursor() 
    cursor.execute('DROP table if exists employees') 
    connect.commit()

def mass_insetr_strings1(connect):

    cursor = connect.cursor() 
    cursor.execute('create table if not exists projects(id integer, name text)') 
    data = [(1, "Ridesharing"), (2, "Water Purifying"), (3, "Forensics"), (4, "Botany")] 
    cursor.executemany("INSERT INTO projects VALUES(?, ?)", data) 
    connect.commit()

def mass_insetr_strings2(connect):

    cursor = connect.cursor()
 
    cursor.execute('create table if not exists assignments(id integer, name text, date date)')
 
    data = [(1, "Ridesharing", datetime.date(2017, 1, 2)), (2, "Water Purifying", datetime.date(2018, 3, 4))]
 
    cursor.executemany("INSERT INTO assignments VALUES(?, ?, ?)", data)
 
    connect.commit()

def disconnect(connect):

    connect.close()

connect()
create_table(connect)
insert_table1(connect)
insert_table2(connect)
update_table(connect)
select1(connect)
select2(connect)
select3(connect)
count_row1(connect)
count_row2(connect)
list_table(connect)
ok_table1(connect)
ok_table2(connect)
delete_table(connect)
mass_insetr_strings1(connect)
mass_insetr_strings2(connect)
disconnect(connect)





