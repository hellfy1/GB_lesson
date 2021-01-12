# task 1

def cash(hour, rate, prize):
    return hour * rate + prize

print(cash(40, 80, 198))

# task 2

tList = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

def rList(tList):
    new_list = [ex for elem, ex in zip(tList, tList[1:]) if ex > elem]
    return new_list

print(rList(tList))

# task 3

print([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0])

# task 4

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print([el for el in my_list if my_list.count(el) == 1])

# task 5

from functools import reduce

def my_func(el_prev, el):
    return el_prev * el

print([el for el in range(99, 1001) if el % 2 == 0])
print(reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0]))

# task 6

from itertools import count
from itertools import cycle

for el in count(int(input('Введите число, с которого необходимо генерировать '))):
    print(el)

my_list = [12, 'Igot', None]
for el in cycle(my_list):
    print(el)

# task 7

from itertools import count
from math import factorial

def f_gen():
    for el in count(1):
        yield factorial(el)

n = 0
for i in f_gen():
    if n < 15:
        print(i)
        n += 1
    else:
        break
