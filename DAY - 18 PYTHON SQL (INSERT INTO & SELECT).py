1. Create a DB with doctor and doctor ID & patients visited

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234"
)
print(mydb)
dbse = mydb.cursor()
dbse.execute("CREATE DATABASE Doctors")
dbse = mydb.cursor()
dbse.execute("SHOW DATABASES")
for entry in dbse:
  print(entry)
  mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="Doctors"
)
dbse = mydb.cursor()
dbse.execute("CREATE TABLE Doctors (Dr_id VARCHAR(255), Patient_visited VARCHAR(255))")
dbse = mydb.cursor()
dbse.execute("SHOW TABLES")
for value in dbse:
  print(value)
dbse = mydb.cursor()
sql = "INSERT INTO Doctors (Dr_id , Patient_Visited) VALUES (%s,%s)"
val = [
    ('DID01','13'),
    ('DID02','5'),
    ('DID03','9'),
    ('DID04','0'),
    ('DID05','11'),
    ('DID06','7'),
    ('DID07','0'),
    ('DID08','0'),
    ('DID09','11'),
    ('DID10','8'),
    ('DID11','0'),
    ('DID12','0'), 
    ('DID13','12'),
    ('DID14','7'),
    ('DID15','0'),
    ('DID16','0')    
]
dbse.executemany(sql, val)
mydb.commit()
print(dbse.rowcount, "was inserted.")

#-----------------------------------------------------------------------------------------------
2. Get the doctor(s) who have more than 5 patients visited

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Doctors where Patient_Visited >5")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#-----------------------------------------------------------------------------------------------------
3. Get the doctors with no patients visit

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Doctors where Patient_Visited=0")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)
