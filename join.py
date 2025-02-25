import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Root@123",
    database = "crudapi"
)
#creating cursor object using the cursor() method
cursor = conn.cursor()


#create another table
sql = '''create table CONTACT(
         ID INT NOT NULL,
         EMAIL CHAR(20) NOT NULL,
         PHONE LONG,
         CITY CHAR(20))'''

cursor.execute(sql)

print("Table created successfully")
#insert into second table
sql2 = '''insert int CONTACT(ID, EMAIL, PHONE, CITY)
            values (5,'<EMAIL>', 987645321 , 'Mumbai'),(101, 'Krishna@mymail.com', 
            'Hyderabad'), (102, 'Raja@mymail.com', 'Vishakhapatnam'), (103, 
            'Krishna@mymail.com', 'Pune'), (104, 'Raja@mymail.com', 'Mumbai')'''

cursor.execute(sql2)

cursor.execute("show tables")
print(cursor.fetchall())

#join these two tables
sqlJoin='''select * from EMPLOYEE inner join CONTACT on EMPLOYEE.ID = CONTACT.ID'''

cursor.execute(sqlJoin)

#
result = cursor.fetchall()
print(result)

#close
conn.close()