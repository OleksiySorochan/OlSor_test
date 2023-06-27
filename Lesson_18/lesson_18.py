import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='pds7'
)

mycursor = mydb.cursor()
#
mycursor.execute('SHOW DATABASES')

for i in mycursor:
    print(i)

# mycursor2 = mydb.cursor()
# mycursor2.execute('SELECT * FROM countries')
# result2 = mycursor2.fetchall()
#
# for r in result2:
#     print(r)

# стоврення нової бази данних
# mycrsor = mydb.cursor()
# mycrsor.execute('CREATE DATABASE PDS7_test')

# mycursor = mydb.cursor()
# mycursor.execute('CREATE TABLE costomers(id INT AUTO_INCREMENT PRIMARY KEY,'
#                  'name VARCHAR(255), address VARCHAR(255))')

# sql = 'INSERT INTO costomers (name, address) VAsLUES (%s, %s)'
# val = [
#     ('Peter', 'Lowstreet 4'),
#     ('Amy', 'Apple st 652'),
#     ('Hannah', 'Mountain 21'),
#     ('Michael', 'Valley 345'),
#     ('Sandy', 'Ocean blvd 2'),
#     ('Betty', 'Green Grass 1'),
#     ('Richard', 'Sky st 331'),
#     ('Susan', 'One way 98'),
#     ('Vicky', 'Yellow Garden 2'),
#     ('Ben', 'Park Lane 38'),
#     ('William', 'Central st 954'),
#     ('Chuck', 'Main Road 989'),
#     ('Viola', 'Sideway 1633')
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, 'it was inserted')
# sql = 'DROP TABLE costomers'
# sql = 'DROP DATABASE pds7_test'
# mycursor.execute(sql)