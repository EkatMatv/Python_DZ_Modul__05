'''Написать игру «Быки и коровы». Программа «загадывает» четырёхзначное число и
играющий должен угадать его. После ввода пользователем числа программа
сообщает, сколько цифр числа угадано (быки) и сколько
цифр угадано и стоит на нужном месте (коровы). После
отгадывания числа на экран необходимо вывести количество сделанных пользователем
попыток. В программе необходимо использовать рекурсию.'''

import random

def secret_number():
    digits = random.randint(1000, 9999)
    return digits
def count_bulls_cows(number1, number2):
    cows = 0
    bulls = 0
    secret = str(number1)
    user = str(number2)
    for i in range(len(secret)):
            if secret[i] in user:
                cows +=1
            if secret[i] == user[i]:
                bulls +=1
    return cows, bulls
def game_bulls_cows(secret, attempts=1):
    user_num = input(f'Попытка №{attempts}. Введите 4-значное число: ')
    cows, bulls = count_bulls_cows(secret, user_num)
    print(f"Результат: {bulls} бык(ов), {cows} корова(ы)")
    if bulls == 4:
        print(f"\nВы угадали число {secret} за {attempts} попыток!")
        return
    return game_bulls_cows(secret, attempts + 1)

secret_num = secret_number()
game_bulls_cows(secret_num)
