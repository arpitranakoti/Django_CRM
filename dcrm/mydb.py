import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd ='Arpit@2004'
    
    )

#cursor obj 
cursorObject = dataBase.cursor()

#create a db 
cursorObject.execute("CREATE DATABASE elderco ")
print("ALL Done ! ")