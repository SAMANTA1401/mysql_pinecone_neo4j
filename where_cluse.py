import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mYsql@2022",
    database = "crudapi"  # CREATE SCHEMA `crudapi` ;
)

cursor = conn.cursor()

cursor.execute("""drop table if exists EMPLOYEE""")

cursor.execute("""CREATE TABLE EMPLOYEE (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                FIRST_NAME VARCHAR(255),
                LAST_NAME VARCHAR(255),
                AGE INT,
                SEX CHAR(1),
                INCOME FLOAT)""")

#computing the table
insert_stm = '''insert into EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME)
                values(%s, %s, %s, %s, %s )'''
data = [('a', 'b', 34, 'F', 23453),('er', 'fg', 45, 'F',365),('df','df',32, 'F',3455)]

try:

    cursor.executemany(insert_stm, data)

    conn.commit()

except:
    print('error occurred')
    conn.rollback()


#retrieving specific records using the where clause
cursor.execute("select * from EMPLOYEE where AGE <30")

print(cursor.fetchall())



#closing the connection
conn.close()