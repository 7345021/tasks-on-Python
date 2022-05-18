# 11. 11.	Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

n = int(input('Введите число: '))


def f(x):
    return(-3)**x


list = [f(i) for i in range(n)]
print(list)
