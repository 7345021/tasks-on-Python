#	Задать список из n чисел последовательности (1+〖1/n)〗^n
# и вывести на экран их сумму
from msilib import sequence
import os
os.system('cls')
n = int(input('Введите число: '))

def get_seq(n):
    return [round((1+1/i)**i, 5)for i in range(1, n+1)]
num = get_seq(n)
print(f'Последовательность чисел: {num}')
print(f'Сумма чисел последовательности: {round(sum(num),5)}')
