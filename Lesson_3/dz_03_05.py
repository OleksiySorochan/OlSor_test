a = input('Ведіть змінну: ')
b = input('Ведіть змінну: ')
print(a, ' ', b)    # друкую змінні в порядку введення
a, b = b, a
print(a, ' ', b)