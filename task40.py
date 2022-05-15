# 40. 40.*Создайте программу для игры в "Крестики-нолики".
# необязательно к выполнению (для тех, у кого есть большое желание)
from multiprocessing.sharedctypes import Value
import os
os.system("cls")

board = list(range(1, 10))  # номера клеток игрового поля,
# здесь хранятся все ходы игроков
wins_comb = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
             (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
# здесь хранятся выигрышные позиции


def take_board():  # Создаем игровое поле
    print('=============')
    for i in range(3):
        print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
    print('=============')


def take_input(player_symbol):  # функция принимает то, что вводит пользователь(Х или O)
    while True:
        value = input('Куда поставить: '+player_symbol+ '? ')
        if not(value in '123456789'):
            print('Ошибка ввода!!! Повторите!!!')
            continue
        value = int(value)  # преобразуем значение value к целочисленному типу.
        if str(board[value-1]) in 'XO':
            print('Эта клетка уже занята!!!')
            continue
        board[value-1] = player_symbol
        break


def check_win():  # функция проверки на выигрыш
    for i in wins_comb:
        if (board[i[0]-1]) == (board[i[1]-1]) == (board[i[2]-1]):
            return board[i[1]-1]
        else:
            return False


def main():
    counter = 0
    while True:
        take_board()
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        if counter > 3:
            winner = check_win()
            if winner:
                take_board()
                print(winner, 'Выиграл')
                break
        counter += 1
        if counter > 8:
            take_board()
            print('Ничья')
            break

main()
