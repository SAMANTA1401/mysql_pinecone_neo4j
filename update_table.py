import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Root@123",
    database = "crudapi"
)

cursor = conn.cursor()

#preparing the query to update the records
sql = '''update EMPLOYEE set AGE = AGE +1 where SEX = 'f' '''

try:
    #execute the sql command
    cursor.execute(sql)
    #commit your changes in the databse
    conn.commit()
except:
    print("Error")
    conn.rollback()

#retrieve data
sql = '''select * from EMPLOYEE'''

cursor.execute(sql)

print(cursor.fetchall())

#close
conn.close()


