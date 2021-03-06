# 33.Задана натуральная степень k. Сформировать случайным образом
#  список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# 1.	k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# ПЕРВЫЙ ВАРИАНТ!!!!
from dataclasses import replace
import itertools
from ntpath import join
from random import randint
import os
os.system("cls")

# pp = '2*х^2 + 5*х + 33 = 0'
# pol = ['2', '*x^', '2', ' + ', '5', '*x + ', '33', ' = 0']

# k = 3
# # генерируем список коэфициентов многочлена
# ratios = [str(randint(0, 100))for i in range(k)]
# print(ratios)
# indexes = [0, 4, 6, 2]


# def get_poly(pol, indexes, ratios, k):
#     ratios.append(str(k-1))
#     for indexes, replace in zip(indexes, ratios):
#         pol[indexes] = replace
#     return"".join(pol)


# pol_new = get_poly(pol, indexes, ratios, k)
# print(pol_new)


# with open('33_task_file.txt', 'w') as data:
#     data.write(pol_new)

#ВТОРОЙ ВАРИАНТ!!!

k = randint(2, 5)

def get_ratios(k):
    ratios = [randint(0, 10) for i in range (k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 10) 
    return ratios

def get_polynomial(k, ratios):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x',' x')


ratios = get_ratios(k)
polynom1 = get_polynomial(k, ratios)
print(polynom1)

with open('34_task_file.txt', 'w') as data:
    data.write(polynom1)


# Второй многочлен для следующей задачи:

k = randint(2, 5)

ratios = get_ratios(k) 
polynom2 = get_polynomial(k, ratios)
print(polynom2)

with open('34_task_file2.txt', 'w') as data:
    data.write(polynom2)


