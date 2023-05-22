def count_symbol():
    my_str = input('Введіть рядок: ')
    symbol = input('Введіть символ: ')
    print(my_str.count(symbol))

# count_symbol()


my_str2 = 'hello my dorter'
my_set = set(my_str2)
# print(my_set)

def giga_to_kilo(num):
    res = num * 1024 *1024
    return res

# print(giga_to_kilo(1))

def convert_age(ear, month= 0):
    age = ear * 12 + month
    return age

# print(convert_age(36, 7))

def bearning_peaple(day, hour, min, sec):
    res = sec + (min * 60) + (hour * 60 *60) + (day * 24 *60 *60)
    return res

print(bearning_peaple(13, 17, 35, 12))