lst = [1, 2, 3]
def func(*args):
    for i in args:
        if type(i) == type([]):
            for s in i:
                print(s)
        else:
            print(i)

func(1, lst, 4, 5)