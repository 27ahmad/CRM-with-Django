import mysql.connector

dataBase = mysql.connector.connect(
    host ='localhost',
    user ='root',
    passwd = 'admin'
)

#cursor object
cursorObject = dataBase.cursor()

#creating database
cursorObject.execute("CREATE DATABASE crm")

print("Done")