from connector import mydb

val = []
def main():
    mycursor2 = mydb.cursor()
    while True:
        data = input("Ведіть ім'я та адресу через точу з кому: ")
        format_data = data.split('; ')
        print(format_data)
        if data != 'send':
            val.append((format_data[0], format_data[1]))
        print('Для того що відправити на базу данних використайте команду send заміть данних')
        if data == 'send':
            break
    print(val)
    sql = 'INSERT INTO costumers(name, address) VALUES ($s, %s)'
    mycursor2.executemany(sql, val)
    mydb.commit()
    print('Данні надіслані в базу данних')

if __name__ == '__main__':
    main()