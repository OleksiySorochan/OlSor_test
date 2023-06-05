from multiprocessing import Pool
from math import sqrt
import os
import time


def sq_rt(n):
    return sqrt(n)

if __name__ == '__main__':
    s_t = time.time()
    time_list = []
    a = 0
    while a < 10:
        cpu = os.cpu_count()
        with Pool(cpu) as p:
            start_time = time.time()
            p.map(sq_rt, range(1, 10000000))
            t = time.time() - start_time
            time_list.append(t)
        a +=1

    print(sum(time_list)/len(time_list))

    time_list2 = []
    a2 = 0
    while a2 < 10:
        start_time = time.time()
        for el in range(1, 10000000):
            sq_rt(el)
        t2 = time.time() - start_time
        time_list2.append(t2)
        a2 += 1

    print(sum(time_list2)/len(time_list2))
    print(time.time() - s_t)

