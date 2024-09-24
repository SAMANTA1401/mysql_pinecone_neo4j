import mysql.connector
global cnx  

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mYsql@2022",
    database="test_db"
)

cursor = cnx.cursor()

query = f"select * from breast_cancer where diagnosis=malignant"

cursor.execute(query)

cursor.close()