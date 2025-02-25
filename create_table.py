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

#Dropping Employee table if already exists
cursor.execute("drop table if exists EMPLOYEE")

#creating table as per requirement
sql = '''create table EMPLOYEE(
    FIRST_NAME char(20) NOT NULL,
    LAST_NAME char(20),
    AGE int,
    SEX char(1),
    INCOME float )'''

#execute the sql
cursor.execute(sql)


#closing the connection
conn.close()