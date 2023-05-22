fibonachi_list = [1, 1, 2, 3, 5, 8, 13]
while True:
    num = fibonachi_list[-2] + fibonachi_list[-1]
    fibonachi_list.append(num)
    print(num)          # виводить числа по одинці
    if fibonachi_list[-1] >= 1500:   # Це ввів щоб корректно вивести числа
        break
print('Числа фібоначі: ', fibonachi_list)   # виводимо числа списком