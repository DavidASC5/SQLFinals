import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Mysterious01",
  database="menagerie"
)


mycursor = mydb.cursor()
mycursor.execute("SELECT owner, COUNT(*) FROM pets GROUP BY owner")
#mycursor.execute("CREATE DATABASE menagerie")
#mycursor.execute("DROP DATABASE menagerie")
#mycursor.execute("CREATE TABLE pets (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex VARCHAR(1), birth DATE, death DATE));")
#mycursor.execute("SHOW TABLES")


for x in mycursor:
  print(x)
print(mydb)
 
