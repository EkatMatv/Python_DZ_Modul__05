#Написать игру «Пятнашки».
import random

board = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 0]]

empty_row, empty_col = 3, 3

for _ in range(100):
    possible_moves = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row = empty_row + dx
        new_col = empty_col + dy
        if 0 <= new_row < 4 and 0 <= new_col < 4:
            possible_moves.append((new_row, new_col))

    new_row, new_col = random.choice(possible_moves)
    board[empty_row][empty_col], board[new_row][new_col] = board[new_row][new_col], 0

    empty_row, empty_col = new_row, new_col

while True:
    # Вывод доски
    print("\nТекущее состояние:")
    for row in board:
        print(" ".join(f"{num:2}" if num != 0 else "  " for num in row))

    if board == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]:
        print("\nПоздравляем! Вы собрали головоломку!")
        break

    empty_found = False
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                empty_row, empty_col = i, j
                empty_found = True
                break
        if empty_found:
            break

    try:
        num = int(input("\nВведите число для перемещения (1-15): "))
        if num < 1 or num > 15:
            print("Число должно быть от 1 до 15!")
            continue

        num_found = False
        for i in range(4):
            for j in range(4):
                if board[i][j] == num:
                    num_row, num_col = i, j
                    num_found = True
                    break
            if num_found:
                break

        if (abs(num_row - empty_row) + abs(num_col - empty_col)) == 1:
            # Выполняем перемещение
            board[empty_row][empty_col], board[num_row][num_col] = num, 0
        else:
            print("Это число нельзя переместить!")

    except ValueError:
        print("Ошибка! Вводите только числа от 1 до 15")
    except:
        print("Произошла ошибка!")