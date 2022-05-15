#38.Напишите программу, удаляющую из текста все слова, 
# содержащие "абв".
# Пример:
# Входные данные:
#  'ываабв лповап абвцукв алоабвабв ываываыв'

# Входные данные: 
# 'лповап ываываыв'

import os
os.system("cls")
my_text = 'ываабв лповап абвцукв алоабвабв ываываыв прабв рпроо'
print(f'Исходный текст:  {my_text}')

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_some_words(my_text)
print(f'Новый текст: {my_text}')

