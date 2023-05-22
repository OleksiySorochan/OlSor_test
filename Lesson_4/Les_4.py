import math
def street(*args):
    for i in args:
        return True if type(i) == type('i') else False
    

# print(street('one', '6', 'hfjd', ' hfdj', ''))
# print(type('one'))

def squear(a):
    p = a * 4
    s = a * a
    d = math.sqrt(2 * a * a)
    return p , s, d
# print(squear(53))


def recurs(a):
    print(a)
    if a < 100:
        a += 1
        recurs(a)

# print(recurs(67))
lst = [1, 2, 3]
def func(*args):
    for i in args:
        if type(i) == type([]):
            for s in i:
                print(s)
        else:
            print(i)

# func('one', lst, 'fore', 'five')

def f_a():
    a =100
    global a
    # a = 100
    return a

def f_x(x):

    return a * x

print(a)

