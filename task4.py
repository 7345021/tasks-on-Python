#4.	Показать первую цифру дробной части числа
import os
os.system('cls')
# number=float(input('Введите число: '))
# number1=str(float(number))
# #print(number1)
# number2=number1.split('.')
# print(number2)
# number3=number2[1]
# #print(number3)
# number_fin=number3[0]
# print(number_fin)
n=float(input('Введите  вещественное число: '))
#b=int((n*10)%10)
print(f'первая цифра дробной части: {int(n*10)%10}')