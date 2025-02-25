# print("hello")
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='Root@123'  # password for root account in MySQL server
)
print(mydb)
# creating an instance of cursor class which is use to execute d the sql
cursor = mydb.cursor()

# show databases
db = cursor.execute("SHOW DATABASES")


for x in cursor:
    print(x)

