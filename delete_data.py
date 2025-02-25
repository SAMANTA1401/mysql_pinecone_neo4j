import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Root@123",
    database = "crudapi"
)
#creating cursor object using the cursor() method
cursor = conn.cursor()

#preparing the query to delete records
sql = "delete from EMPLOYEE where AGE > 40"

try:
    #Executing the SQL command
    cursor.execute(sql)
    conn.commit()
except:
    print("Error in executing sql")
    conn.rollback()

#retrieve data
print("contents of the table after delete operation ")
cursor.execute("select * from EMPLOYEE")

print(cursor.fetchall())


#close
conn.close()

