import mysql.connector
connection = mysql.connector.connect(
 host="localhost",
 user="root",
 password="root"
)

mycursor = connection.cursor()
mycursor.execute("CREATE database datarepresentation ")

connection.commit()
mycursor.close()
connection.close()
