# 2.	Найти максимальное из пяти чисел
import os
os.system('cls')
# a=int(input('введите первое число: '))
# b=int(input('введите второе число: '))
# c=int(input('введите третье число: '))
# d=int(input('введите четвертое число: '))
# g=int(input('введите пятое число: '))
# if a>b and a>c and a>d and a>g:
#     print(f'наибольшее число a= {a}')
# elif b>a and b>c and b>d and b>g:
#     print(f'наибольшее число b= {b}')
# elif c>a and c>b and c>d and c>g:
#     print(f'наибольшее число c= {c}')
# elif d>a and d>b and d>c and d>g:
#     print(f'наибольшее число d= {d}')
# elif g>a and g>b and g>c and g>d:
#     print(f'наибольшее число g= {g}')

# massive=[12, 34, 56, 3, 68]
# print(massive)
# print('наибольшее число: ', max(massive))#ПЕРВОЕ РЕШЕНИЕ
# max=massive[0]
# for i in massive:
#     if i>max:
#         max=i
# print('наибольшее число: ', max)#ВТОРОЕ РЕШЕНИЕ
# from random import randint

# N = 5  # Количество цифр для сравнения

# nums = [randint(1, 20) for i in range(N)]

# print(nums)

# myMax = nums[0]
# myMin = nums[0]

# for i in range(N):
#     if nums[i] > myMax:
#         myMax = nums[i]
#     if nums[i] < myMin:
#         myMin = nums[i]

# print('Max:', myMax, 'Min:', myMin)#ТРЕТЬЕ РЕШЕНИЕ
a, b, c, d, e = 3, 5, 24, 15, 8
max=a
if max<b:
    max=b
if max<c:
    max=c
if max<d:
    max=d
if max<e:
    max=e
print(max)#ЧЕТВЕРТОЕ РЕШЕНИЕ

