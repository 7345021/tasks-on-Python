# 7.	Проверить истинность утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
import os
os.system('cls')
x = 0
y = 0
z = 0

left = not (x or y or  z)
right = not x and not y and not z 
statement = left == right
print(statement)
