import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database ='testdata'
)

# mycursor = mydb.cursor()
# mycursor.execute('SHOW DATABASES')
# for i in mycursor:
#     print(i)
#
# mycursor = mydb.cursor()
# mycursor.execute('CREATE DATABASE TestData')
# print('databse created')

# mycursor = mydb.cursor()
# mycursor.execute('CREATE TABLE customers(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), address VARCHAR(255))')
# print('table created')

mycursor = mydb.cursor()

