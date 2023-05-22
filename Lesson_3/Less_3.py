a = list(range(1, 100))
print(a)
b = []
for i in range(1, 100):
    if i % 15 == 0:
        i = 'FizzBuzz'
        b.append(i)
    elif i% 5 == 0:
        i = 'Buzz'
        b.append(i)
    elif i % 3 == 0:
        i = 'Fizz'
        b.append(i)
    else:
        b.append(i)

print(b)

for year in range(1900, 2023):
    if year % 4 == 0 and year % 100 != 0:
        print(year)

text_list = ['one', 'tow', 'hello, my name is Oleksiy', 'second', 'what', 'Oil']
clear_list = [el for el in text_list if len(el) < 5 and el[0].lower() in 'aeiouy']
print(clear_list)
