def open_file(path):
    with open(path, 'r') as f:
        lst_lines = f.readlines()
        lst_lines = [i.replace('\n', '').split(': ') for i in lst_lines]
        res_dict = {}
        for i in lst_lines:
            res_dict[i[0]] = i[1]
        return res_dict

print(open_file('dk.txt'))
