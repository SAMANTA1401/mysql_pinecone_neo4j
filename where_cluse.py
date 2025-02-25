import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Root@123",
    database = "crudapi"
)

cursor = conn.cursor()

#computing the table
insert_stm = '''insert into EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME)
                values(%s, %s, %s, %s, %s )'''
data = [('a', 'b', 34, 'F', 23453),('er', 'fg', 45, 'F',365),('df','df',32, 'F',3455)]

try:

    cursor.executemany(insert_stm, data)

    conn.commit()

except:
    print('error occured')
    conn.rollback()


#retrdieving specific records using the where clause
cursor.execute("select * from EMPLOYEE where AGE <30")

print(cursor.fetchall())



#closing the connection
conn.close()