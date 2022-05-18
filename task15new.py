# 15.Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
#[ 1, 2, 6, 24 ]
from math import factorial


n = int(input('Введите число: '))
list = [(0+factorial(1+i)) for i in range(n)]
print(list)
