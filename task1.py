# 1.	По двум заданным числам проверить является
# ли одно квадратом второго.
import os
os.system('cls')

a = int(input('введите число a: '))
print(f'квадрат числа {a} равен {a**2}')
b=int(input('введите число b: '))
if b==a**2 or a==b**2:
    print('число b является квадратом числа a')
else:
    print('число b не является квадратом числа a')