#3.	Вывести на экран числа от -N до N
import os
os.system('cls')
num=abs(int(input('Введите число: ')))
for i in range(-1*num, num+1):
    print(i, end=' ')