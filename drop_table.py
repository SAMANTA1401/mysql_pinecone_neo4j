import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Root@123",
    database = "crudapi"
)
#creating cursor object using the cursor() method
cursor = conn.cursor()

#retrieving the list of tables
print("list of tables in  the database: ")
cursor.execute("show tables")
print(cursor.fetchall())


#dropping 'tbl_auize table if already exist
cursor.execute("drop table if exists tbl_quize")
print("table dropped....")

#retrieve the list of tables
print("list of tables after dropping the tbl_quize table: ")
cursor.execute("show tables")
print(cursor.fetchall())

#close
conn.close()



