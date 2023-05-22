def time_of_year(a):
    if a <= 12 and a > 0:
        if a == 12 or a == 1 or a == 2:
            return 'winter'
        elif a == 3 or a == 4 or a == 5:
            return 'Spring'
        elif a == 6 or a == 7 or a == 8:
            return 'Summer'
        else:
            return 'Autumn'
    else:
        return 'enter correct number'
# print(time_of_year(13))

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
dict3 = {'tree': 3}
dict = update_dict(dict1, dict2, dict3)
# print(dict)

def palindrom(st):
    return True if st == st[::-1] else False

# print(palindrom('випив'))

def number_sum(num):
    num_list = [int(i) for i in str(num)]
    return sum(num_list)

# print(number_sum(437))


def popular_lit(st):
    if type(st) == type('st'):
        res = 0
        lit = ''
        for l in st:
            if res < st.count(l):
                lit = l
                res = st.count(l)
        return lit, res
    else:
        return "only 'str' type argument"

def popular_lis2(st):
    lit_dict = {}
    lst = {}
    for l in st:
        lit_dict[l] = st.count(l)
    for k, v in lit_dict.items():

    print(lst)
    print(lit_dict)


text = "Lorem Ipsum is simply dummy text"
# print(popular_lit(text))
popular_lis2(text)