
def recuprsion(num):
    if num > 0:
        num -= 1
        print(num)
        recuprsion(num)

num = int(input("Введіть ціле число: "))
recuprsion(num)

