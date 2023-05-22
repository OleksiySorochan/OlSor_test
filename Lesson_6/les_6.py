#
# def fibonachi_recus(max):
#     fibonachi_list = [1, 1, 2]
#
#     def recurcion():
#         fibonachi_list.append(fibonachi_list[-2] + fibonachi_list[-1])
#         if fibonachi_list[-1] < max:
#             recurcion()
#     recurcion()
#
#     return fibonachi_list
#
#
# # print(fibonachi_recus(100))
#
#
# lst = [ 20, -33, 16, 21, -5, -66, 74, -3, 27, 87, -4]
#
# def vid(lst):
#     a = 0
#     for i in lst:
#         # print(i)
#         if i < 0:
#             a += 1
#     return a
# # print(vid(lst))
#
# lst = ('c', 'd', 'b', 'a')
# print(sorted(lst))

# import os
#
# path = 'E:\it_ progect\SPASE_DATA_Siencetict'
#
# def go_file(path, level= 1):
#     print('level = ', level, 'conetent: ', os.listdir(path))
#     for i in os.listdir(path):
#         if os.path.isdir(path + '\\'+ i):
#             print('Спускаюсь нижче, шлях + "\\"' + i)
#             go_file(path + '\\' + i, level + 1)
#             print('Повертаюсь на рівень вижче...', path)
#
# go_file(path)




# Алгоритими пошуку

# Методи пошуку у послудовностях (вбудовані методи пошуку для послідовностей)
# оператори членства
# лінійний пошук
# бінаринй пошук
    # пошук стрибка
    # пошук фібоначі
    # експоненціальний пошук
    # інтерполяціний пошук


# оператори членства


# lst = ['Windows', 'Linux', 'McOs', 'FreeBSD', 'Solyaris' ]
# quest1 = 'Linux' in lst
# print(quest1)

# лінійний пошук
# def linear_search(lst, el):
#     res_list = []
#     for i in range(len(lst)):
#         if lst[i] == el:
#             res_list.append(i)
#     return -1 if res_list == [] else res_list
#
l1 = [1, 2, 3, 4 ,5, 2, 4, 5, 8, 11, 57, 1, 55]
# print(linear_search(l, 4))


# бінариний пошук

def binary_search(lys, val):
    first = 0
    last = len(lys) - 1
    index = -1
    while first <= last and  index == -1:
        mid = (first + last) // 2
        if lys[mid] == val:
            index = mid
        else:
            if val < lys[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index

# l = list(range(1, 101))
l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# l = sorted(l1)
print(binary_search(l, 4))