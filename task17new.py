# 17.	Задать список из N элементов, заполненных числами из [-N, N].
#  Найти произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке
# одно число

from functools import reduce
import os
os.system('cls')
N = int(input("Введите размер списка: "))
num_list = list(range(-N, N+1))  # задаем список из N элементов, заполняем его
print(num_list)
with open('17_task_file_new.txt', 'w') as data:  # Заполняем текстовый файл
    data.write('0\n')
    data.write('3\n')
    data.write('4\n')
    data.write('8\n')


def get_data_from_file(path):
    data = open(path, 'r')
    dlist = [int(line.strip()) for line in data]
    data.close()
    return dlist


path = '17_task_file_new.txt'
datalist = get_data_from_file(path)
print(datalist)
list = [num_list[i] for i in datalist]
print(list)
result = reduce((lambda x, y: x * y), list)
print(result)



