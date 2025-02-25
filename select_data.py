import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Root@123",
    database = "crudapi"
)

cursor = conn.cursor()

cursor.execute("show tables")

print(cursor.fetchall())

#retreivng row
sql = '''select * from EMPLOYEE'''

#executing the query
cursor.execute(sql)

#fetching the 1st row from the table
# result = cursor.fetchone()
# print(result)

#fetching the two row from the table
result3 = cursor.fetchmany(size =2)
print(result3)

#fetching all the row from the table as list
# result2 = cursor.fetchall()
# print(result2)

#closing the connection
conn.close()