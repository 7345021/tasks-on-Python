#17.	Задать список из N элементов, заполненных числами из [-N, N].
#  Найти произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке 
# одно число
#from importlib.resources import path


N = int(input("Введите размер списка: "))
num_list = list(range(-N, N+1))#задаем список из N элементов, заполняем его
print(num_list)


# data = open('17_task_file.txt', 'a')#Первый способ
# data.write('0\n')
# data.write('1\n')
# data.write('3\n')
# data.write('5\n')
# data.write('8\n')
with open('17_task_file.txt', 'w') as data:#Второй способ
    data.write('0\n')
    data.write('3\n')
    data.write('5\n')
    data.write('8\n')
def get_data_from_file(path):
    data=open(path,'r')
    dlist = [int(line.strip()) for line in data]
    data.close()
    return dlist
def get_mult(nums, datalist):
    mult = 1
    for i in datalist:
        mult *= nums[i]
    return mult
path='17_task_file.txt'
datalist = get_data_from_file(path)
nums=num_list
print(datalist)
print(get_mult(nums,datalist))
