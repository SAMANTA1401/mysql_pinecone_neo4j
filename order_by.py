import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Root@123",
    database = "crudapi"
)

cursor = conn.cursor()

#retrieving specific records using the order by cluse
cursor.execute("select * from EMPLOYEE order by AGE")
print(cursor.fetchall())

#order by descending
cursor.execute("select * from EMPLOYEE order by INCOME desc")
print(cursor.fetchall())

#closing the connection
conn.close()

