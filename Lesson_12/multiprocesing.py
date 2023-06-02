from multiprocessing import Pool
import  time
import os

def f(x):
    return x**x

if __name__ == '__main__':
    cpu = os.cpu_count()
    print(f'Ваш комп має {cpu} ядер')
    with Pool(cpu) as p:
        start_time = time.time()
        print(p.map(f, range(1, 100)))
        print(f'Time: {time.time() - start_time}')

    # start_time = time.time()
    # for i in range(1, 1000):
    #     print(f(i))
    # print(f'Time: {time.time() - start_time}')
