import os

dict = {'one': 1, 'two': 2, 'three': 3}

# for k, v in dict.items():
#     # print(k, v)

# def new_file(dict, name):
#         with open(name, 'w') as file:
#             for k, v in dict.items():
#                 file.write(f'{k}: {v}\n')


# new_file(dict, 'dk.txt')

# lst = [('one', 1),('two', 2),('tree', 3)]
# dc = dict(lst)
# print(dc)

# lst = [1, 2, 3, 4, 5]
# print(*lst, sep=' | ')

# print(os.name)
# print(os.listdir(path='C://Windows'))
# print(os.getcwd())  # Виводить поточну директорію
# print(os.system('pwd')) # os.sysetm - виконє системну команду
# print(os.path.abspath())

# f = open('file.txt', 'w')
# st = 'This is new srting in my file 333'
# f.write(st)
# f.close()

# with open('file.txt' , 'a') as f:
#     st = 'This is new srting number 4 \n'
#     f.write(st)

# with open('file.txt', 'r') as f:
#     t = f.readlines()
#     print(t)

def last_lines(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        len_last_line = len(lines[-1])
        return len_last_line

# print(last_lines('file.txt'))

# with open('new_file.txt', 'w') as f:
#     st = str([i for i in range(100) if i % 5 == 0])
#     f.write(st)

def len_file(path):
    with open(path, 'r') as f:
        st = f.read()
        return len(st)

# print(len_file('new_file.txt'))

p = 'E:\it_ progect\SPASE_DATA_Siencetict\Lesson_5'
# b = os.listdir(p)
# print(b)

def file_in_dir(path):
    return os.listdir(path)

# print(file_in_dir(p))
