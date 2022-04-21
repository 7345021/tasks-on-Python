#18.Реализовать алгоритм перемешивания списка. 
from random import randint, shuffle
original_list = [randint(-5, 5) for i in range(8)]
print(f'Первоначальный список: {original_list}')#создали оригинальный список

shuffle(original_list)#функция перемешивания
print(f'Перемешанный список:  {original_list}')#распечатали перемешанный список

