import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Root@123",
    database = "crudapi"
)

cursor = conn.cursor()

#select data
cursor.execute("select * from EMPLOYEE")

rows = cursor.fetchall()

print(rows)

#read the data sql to dataframe
df = pd.DataFrame(rows)

print(df.head())


#create a empty csv file
data = open('output.csv','w')
#data frame to csv
df.to_csv(data, header=False)

#close
conn.close()