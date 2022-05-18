#	Задать список из n чисел последовательности (1+〖1/n)〗^n
# и вывести на экран их сумму
from msilib import sequence
import os
os.system('cls')
n = int(input('Введите число: '))

list = [round((1+1/i)**i, 5)for i in range(1, n+1)]
res = sum(list)
print(f'Последовательность: {list}')
print(f'сумма чисел последовательности: {round(sum(list),5)}')
