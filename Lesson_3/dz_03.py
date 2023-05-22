# 1
fibonachi_list = [1, 1, 2, 3, 5, 8, 13]
while True:
    num = fibonachi_list[-2] + fibonachi_list[-1]
    fibonachi_list.append(num)
    print(num)
    if fibonachi_list[-1] >= 1500:   # Це ввів щоб корректно вивести числа
        break
# print('Числа фібоначі: ', fibonachi_list)

#2
my_lst = list(range(101))
my_lst2 = [i for i in my_lst if i % 3 == 0]
print(my_lst2)

# 3
number_list = []
for i in range(10):
    a = input('Введіть ціле число: ')
    number_list.append(int(a))
res = sum(number_list)
print(res)

# 4
while True:
    a = int(input('Введіть ціле число: '))
    if a < 0:
        break

#5
a = input('Ведіть змінну: ')
b = input('Ведіть змінну: ')
print(a, ' ', b)
a, b = b, a
print(a, ' ', b)