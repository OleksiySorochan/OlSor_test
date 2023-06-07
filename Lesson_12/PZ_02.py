from multiprocessing import Pool
from math import sqrt
import os
import time
import threading

lst = []
def prt(a):
    print(a)
def sq_rt(n):
    return sqrt(n)

def ren(start=0, finish=0):
    for i in range(start, finish):
        el = sq_rt(i)
    lst.append(el)

if __name__ == '__main__':
    s_t = time.time()
    time_list = []
    a = 0
    while a < 10:
        cpu = os.cpu_count()
        with Pool(cpu) as p:
            start_time = time.time()
            p.map(sq_rt, range(1, 100))
            t = time.time() - start_time
            time_list.append(t)
        a +=1
    print('')
    print('multiprocessing: ',sum(time_list)/len(time_list))
    print('*' * 50)

    # threading
    time_list2 = []
    a2 = 0
    while a < 10:
        task_1 = threading.Thread(target=ren, kwargs={'finish': 500})
        task_2 = threading.Thread(target=ren, kwargs={'start': 1, 'finish': 1000})
        start_time2 = time.time()
        task_1.start()
        task_2.start()
        task_1.join()
        task_2.join()
        t2 = time.time() - start_time2
        time_list2.append(t2)
        a += 1

    print(time_list2)
    print(lst)

