from math import sqrt
def s_tr(a, b, c):
    try:
        if a > 0 and b > 0 and c > 0:
            p = (a + b + c)/2
            s = sqrt(p*(p-a)*(p-b)*(p-c))
            return s, p
        else:
            raise('сторони трикутника повинні бути більше 0')
        return -2
    except TypeError as ex:
        print(f'{ex}: введіть сторони трикутника')
        return -1

print(s_tr(13, 14, 15))


