number_list = []
for i in range(10):
    a = input('Введіть ціле число: ')
    number_list.append(int(a))
res = sum(number_list)
print(res)