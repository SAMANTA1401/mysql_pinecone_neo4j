import mysql.connector

mydb2 = mysql.connector.connect(  #establishing the connection
    host = "localhost",
    user="root",
    passwd = "mYsql@2022"
)
print(mydb2) #confirm the connection

#creating a instance of cursor object using cursor object() method
cursor = mydb2.cursor()

#Executing an MYSql function using execute method()
cursor.execute("SHOW DATABASES")
print("list of databases before drop:")
for x in cursor:
    print(x)


#dropping databases crudapi if already exist
cursor.execute("DROP DATABASE IF EXISTS sample2")

print("list of databases after drop:")

cursor.execute("SHOW DATABASES")
for x in cursor:
    print(x)

#preparing query to create a data base
sql = "create database sample2";

# #creating a database
cursor.execute(sql)

#list of databases after create
print("list of databases after create")

print("list of databases")

cursor.execute("show databases")

print(cursor.fetchall())

#closing the connection
mydb2.close()