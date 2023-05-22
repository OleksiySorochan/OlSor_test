
def new_file(dic, name):
        with open(name, 'w') as file:
            for k, v in dic.items():
                file.write(f'{k}: {v}\n')


dic = {'one': 1, 'two': [2, 4, 5], 'three': 3}
new_file(dic, 'dk.txt')