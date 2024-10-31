import mysql.connector

conn = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE review")

print("Success create database")

cursor.close()
conn.close()