import sqlite3
import csv


connection = sqlite3.connect('database.db')
c = connection.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS theTable(name TEXT, id INT, course TEXT, grade INT)')


def insert_data():
    f = open("Student_Data.txt", "r")
    for row in csv.DictReader(f):
        c.execute('''INSERT INTO theTable
              VALUES(:name, :id, :course, :grade)''', row)
        connection.commit()

def update_data():
    c.execute('SELECT * FROM theTable')
    c.execute('UPDATE theTable SET id= 1115 WHERE id= 1112')
    connection.commit()

def delete_data():
    c.execute('SELECT * FROM theTable')
    c.execute('DELETE FROM theTable WHERE id= 1115')
    connection.commit()

def find_column():
    data = c.fetchall()
    for row in data:
        print ('{0} : {1}, {2},{3}'.format(row[0], row[1], row[2], row[3]))


create_table()
insert_data()
update_data()
delete_data()
find_column()
    
    
