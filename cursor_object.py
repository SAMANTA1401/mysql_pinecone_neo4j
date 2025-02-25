import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Root@123",
    database = "crudapi"
)
#creating cursor object using the cursor() method
cursor = conn.cursor()


