# #31.Задайте натуральное число N. Напишите программу, которая составит список
# #  простых множителей числа N.

import os
os.system('cls')


n = int(input('Введите число: '))


def simple_multiplier(n):
    i = 2
    list = []
    while n != 1:
        if n % i == 0:
            list.append(i) 
            n = n / i
            i = 2
        else:
            i += 1
    return (list)


print(simple_multiplier(n))