'''Дан текстовый файл. Найти и заменить в нем задан-
ное слово. Что искать и на что заменять определяется
пользователем.'''

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
result = gcd(num1, num2)
print(f"НОД чисел {num1} и {num2} равен48 {result}")