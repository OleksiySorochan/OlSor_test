def update_dict(*dict):
    dc = {}
    for d in dict:
        if type(d) == type(dc):
            dc.update(d)
        else:
            return "only 'dict' type argument"
    return dc


dict1 = {'one': 1}
dict2 = {'two': 2}
dict3 = {'three': 3}
dict = update_dict(dict1, dict2, dict3)
print(dict)