1. Create a connection for DB and print the version using a python program

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234"
)
print(mydb)
import sys
cur = mydb.cursor()
cur.execute("SELECT VERSION()")
data = cur.fetchone()
print("DBMS Version :",str(data))

#-----------------------------------------------------------------------------
2. Create a multiple tables & insert data in table

dbse = mydb.cursor()
dbse.execute("CREATE DATABASE mydatabase")
dbse = mydb.cursor()
dbse.execute("SHOW DATABASES")
for entry in dbse:
  print(entry)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="mydatabase"
)
dbse = mydb.cursor()
dbse.execute("CREATE TABLE customers (Emp_name VARCHAR(255), Emp_dep VARCHAR(255), Emp_id VARCHAR(255))")
dbse = mydb.cursor()
dbse.execute("SHOW TABLES")

for value in dbse:
  print(value)
dbse = mydb.cursor()

dbse.execute("CREATE TABLE Office (emp_name VARCHAR(255), emp_id VARCHAR(255) ,emp_address VARCHAR(255))")
dbse =mydb.cursor()
dbse.execute("CREATE TABLE Student(Roll_no INT(24) , Stud_Name VARCHAR(255) , Mark INT(3))")
dbse = mydb.cursor()
dbse.execute("SHOW TABLES")

for value in dbse:
  print(value)
  
#-----------------------------------------------------------------------------------
3. Create a employee table and read all the employee name in the table using for loop

 mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="1234",
  database="mydatabase"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Emp1 (Id INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(255), Address VARCHAR(255))")
mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="1234",
  database="mydatabase"
)
mycursor = mydb.cursor()

sql = "INSERT INTO Emp1 (id, name, address) VALUES (%s, %s,%s)"
val = ("101","sherin","Suraj Nagar 56")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
mycursor = mydb.cursor()

sql = "INSERT INTO Emp1 (id, name, address) VALUES (%s, %s,%s)"
val = ("102","Ranjith","Anna Nagar 58")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
mycursor = mydb.cursor()

sql = "INSERT INTO Emp1 (id, name, address) VALUES (%s, %s,%s)"
val = ("103","Rajeev","T Nagar 58")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
mycursor = mydb.cursor()

sql = "INSERT INTO Emp1 (id,name, address) VALUES (%s,%s,%s)"
val = [
  ('001','Peter', 'Green Grass 1'),
  ('002','Amy', 'Sky st 331'),
  ('003','Hannah', 'One way 98'),
  ('004','Michael', 'Yellow Garden 2'),
  ('005','Sandy', 'Park Lane 38'),
  ('006','Betty', 'Central st 954')
]
mycursor.executemany(sql, val)

mydb.commit()
print(mycursor.rowcount, "was inserted.")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Emp1")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
mycursor = mydb.cursor()
mycursor.execute("SELECT name FROM Emp1")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
 
