import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mYsql@2022",
    database = "crudapi"  # CREATE SCHEMA `crudapi` ;
)

cursor = conn.cursor()