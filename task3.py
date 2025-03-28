'''Дана шахматная доска размером8×8 и шахматный конь.
Программа должна запросить у пользователя координаты
клетки поля и поставить туда коня. Задача программы
найти и вывести путь коня, при котором он обойдет все
клетки доски, становясь в каждую клетку только один
раз. (Так как процесс отыскания пути для разных начальных
клеток может затянуться, то рекомендуется сначала
опробовать задачу на поле размером 6×6). В программе
необходимо использовать рекурсию.'''


def is_valid_move(x, y, board_size=6):
    return 0 <= x < board_size and 0 <= y < board_size

def knight_tour(start_x, start_y, board_size=6):
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
             (-2, -1), (-1, -2), (1, -2), (2, -1)]

    board = [[-1 for _ in range(board_size)] for _ in range(board_size)]
    board[start_x][start_y] = 0  # Начальная позиция

    def solve(x, y, move_count):
        if move_count == board_size ** 2:
            return True

        for dx, dy in moves:
            next_x, next_y = x + dx, y + dy
            if is_valid_move(next_x, next_y) and board[next_x][next_y] == -1:
                board[next_x][next_y] = move_count
                if solve(next_x, next_y, move_count + 1):
                    return True
                # Откат (backtracking)
                board[next_x][next_y] = -1

        return False

    # Запуск решения
    if solve(start_x, start_y, 1):
        return board
    else:
        return None

def print_board(board):
    for row in board:
        print(" ".join(f"{num:2d}" for num in row))


def main():
    print("Шахматный конь - обход всех клеток доски")
    while True:
        try:
            x = int(input("Введите начальную строку (0-7): "))
            y = int(input("Введите начальный столбец (0-7): "))
            if not (0 <= x < 6 and 0 <= y < 6):
                print("Координаты должны быть от 0 до 7!")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите числа от 0 до 7!")

    print("\nИщем решение... Это может занять некоторое время...")
    solution = knight_tour(x, y)

    if solution:
        print("\nНайденный путь коня:")
        print_board(solution)
    else:
        print("Решение не найдено для данной начальной позиции.")

main()
