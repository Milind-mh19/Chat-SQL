import sqlite3 

## connection to sqllite 
connection = sqlite3.connect("student.db")

## create a cursor object to insert record, creat tabel 

cursor = connection.cursor()

## create the tabel 
table_info="""
create table STUDENT(NAME VARCHAR(25),CLASSS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)

## Insert some more recods
cursor.execute('''Insert Into STUDENT values('milind','Data Scinence','A',90)''')
cursor.execute('''Insert Into STUDENT values('kunal','Data Scinence','B',100)''')
cursor.execute('''Insert Into STUDENT values('kartik','Data Scinence','A',86)''')
cursor.execute('''Insert Into STUDENT values('Aanu','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('milind','DEVOPS','A',35)''')

## Diplay all the records
print("the ineted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)


## Commit you changes in the databese

connection.commit()
connection.close()