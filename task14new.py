# 14.	Подсчитать сумму цифр в вещественном числе
# import random
# random.uniform
# n=round(random.uniform(0,5), 5)
# print(n)
# def sum_digit(n):
#      return sum(map(int, list(str(n).replace('.',''))))

# print(sum_digit(n))

from posixpath import split
import random
random.uniform
n = round(random.uniform(0, 5), 5)
print(n)
data=list(map(int, list(str(n). replace('.',''))))
print(data)
res=sum(data)
print(res)