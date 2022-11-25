        # 14 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
        # Пример:
        # - 6782 -> 23
        # - 0,56 -> 11

# number = input(' Введите ваше число: ')
# checksumm = 0
# for symbol in number:
#     if symbol != '.' and symbol != '-':
#         checksumm += int(symbol)
# print(checksumm)

        # 15 Напишите программу которая принимает на вход число N 
        # и выдает набор произведений чисел от 1 до N

n = int(input('Введите ваше число: '))
some_list = [1]
fact = 1
for i in range(2, n + 1):
    fact *= i
    some_list.append(fact)
print(some_list)


        #16 Задайте список и n чисел и выведите на экран 
        # их сумму

# n = int(input('Введите ваше число: '))
# checksumm = 0 
# for i in range(1, n + 1):
#     checksumm += (1 + 1 / i) ** i
# print(checksumm)


        # 17 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся 
        # в файле file.txt в одной строке одно число.
#
# from random import *
# n = int(input('Введите ваше число: '))
# some_list = []
# for _ in range(n):
#     some_list.append(randint(-n, n))
# print(some_list)
# with open('file.txt', 'w', ='utf-8') as f:
#     for _ in range (randint(1, n)):
#         f.write(str(randint(0, n-1)) + '\n')
# fact = 1
# with open('file.txt', 'w', encodint='utf-8') as f:
#     f = f.read().splitlines()
#     for number in f:
#         fact *= some_list[int(number)]
# print(fact)


