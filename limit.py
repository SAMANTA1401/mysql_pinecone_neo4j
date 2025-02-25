import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Root@123",
    database = "crudapi"
)
#creating cursor object using the cursor() method
cursor = conn.cursor()

#retrieving single row
sql = '''select * from EMPLOYEE limit 2'''

#executing the query
cursor.execute(sql)

#fetching the data
result = cursor.fetchall()
print(result)

# close
conn.close()
