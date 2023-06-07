import random, time

my_list = []

for i in range(5000):
    # my_list.append(random.randrange(1, 1000))
    my_list.append(random.randint(1, 1000))

# print(my_list)
# print(my_list.count(8))

# Buule sort

def bubble_sort(data):
    length = len(data)
    for index in range(0, length):
        swapped = False
        for j_index in range(0, length - index -1):
            if data[j_index] > data[j_index +1]:
                data[j_index], data[j_index +1] = data[j_index +1], data[j_index]
                swapped = True
        if not swapped:
            break
    print('Sorted data: ', data)

cor_time = time.time()
bubble_sort(my_list)
print('*'*50)
print(time.time() - cor_time)
# 2.6467678546905518

# Quick sort
print('')
print('*'*50)
print('')
def partitions(nums, low, hight):
    pivot = nums[(low + hight) // 2]
    i = low - 1
    j = hight + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]

def quick_cort(nums):
    def _quick_sort(items, low, hight):
        if low < hight:
            split_index = partitions(items, low, hight)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, hight)
    _quick_sort(nums, 0, len(nums) - 1)
    print(f'Sorted data: {nums}')

cor_time = time.time()
quick_cort(my_list)
print('*'*50)
print(time.time() - cor_time)

# Вбудовані функціі сортування
print('')
print('*'*50)
print('')

cor_time = time.time()
m = sorted(my_list)
print(m)
print('*'*50)
print(time.time() - cor_time)