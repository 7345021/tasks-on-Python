# 14.	Подсчитать сумму цифр в вещественном числе
import random
random.uniform
n=round(random.uniform(0,5), 5)
print(n)
def sum_digit(n):
     return sum(map(int, list(str(n).replace('.',''))))

print(sum_digit(n))
