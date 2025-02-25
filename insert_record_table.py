import mysql.connector

#establishing the connection

conn = mysql.connector.connect(
    host="localhost",
    user='root',
    password='Root@123',
    database='crudapi'
)

#creating a cursor object using the cursor() method 

cursor = conn.cursor()

#show tables in the databse
cursor.execute("show tables")

for x in cursor: # show as tuple or set
    print(x)

# print(cursor.fetchall()) # show as the list

#preparing sql query to insert a record into the database crudapi table emplyee

# sql = '''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
#          VALUES('SOurav', 'khanra', 28, 'M', 20000.0)'''

# insert data dynamicallly 
sql = '''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
         VALUES(%s, %s, %s, %s, %s)'''

data_values = ('pk','konar', 29, 'M', 19000)
try:
    #executing the sql command
    # cursor.execute(sql)
    cursor.execute(sql,data_values)
    #commit your changes in the database
    conn.commit()
except:
    #rolling back in case of error
    print("Error occured while inserting data.")
    conn.rollback()

#closing the connection
conn.close()