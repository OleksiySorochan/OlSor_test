import random
from random_words import RandomWords

int_list = []
float_list = []
str_list = []

w = RandomWords()

for i in range(5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(random.uniform(0.1, 100.0))
    str_list.append(w.random_word())

print(int_list)
print('*'*100)
print(float_list)
print('*'*100)
print(str_list)