def index(lst, i):
    try:
        return lst[i]
    except IndexError as ex:
        print(f'{ex}: елементу із таким індексом на має')
        return -1


lst = [1, 2, 3, 4, 5, 6, 7]
print(index(lst, 7))