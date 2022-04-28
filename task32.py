# 32.Задайте последовательность чисел. Напишите программу,
#  которая выведет список неповторяющихся элементов исходной
#  последовательности.

from random import randint



data = []
for i in range(10):
    data.append(int(randint(1, 10)))
print(data)

f=[]
for k in data:
    b=0
    for h in data:
        if k==h:
            b+=1
    if b==1: # элемент в списке единичен(уникален)
        f.append(k)
print(f)
#ВТОРОЙ СПОСОБ

s=[]
for j in data:
    if data.count(j)==1:
        s.append(j)
print(s)
