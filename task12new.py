# 12.	Для натурального n создать словарь индекс-значение,
# состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}


from random import randint
n = randint(5, 15)
print(n)
list = [{x: (3*x)+1} for x in range(1, n+1)]
print(list)
