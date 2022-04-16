# 9.	Указав номер четверти прямоугольной
# системы координат, показать допустимые значения координат для точек этой четверти
import os
os.system('cls')

numquarte = int(input('введите номер четверти от 1 до 4: '))
if numquarte==1:
    print('первая четверть', '{x>0 and y>0}')
if numquarte==2:
    print('вторая четверть', '{x<0 and y>0}')
if numquarte==3:
    print('третья четверть', '{x<0 and y<0}')
if numquarte==4:
    print('четвертая четверть', '{x>0 and y<0}')
