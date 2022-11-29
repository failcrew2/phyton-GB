        # 1 Напишите программу, которая принимает на вход вещественное
        # число и показывает сумму его цифр.


# number = input(' Введите ваше число: ')
# checksumm = 0
# for symbol in number:
#     if symbol != '.' and symbol != '-':
#         checksumm += int(symbol)
# print(checksumm)

        # 2 Напишите программу которая принимает на вход число N
        # и выдает набор произведений чисел от 1 до N

# n = int(input('Введите ваше число: '))
# some_list = [1]
# fact = 1
# for i in range(2, n + 1):
#     fact *= i
#     some_list.append(fact)
# print(some_list)


        #3 Задайте список и n чисел и выведите на экран
        # их сумму

# n = int(input('Введите ваше число: '))
# checksumm = 0
# for i in range(1, n + 1):
#     checksumm += (1 + 1 / i) ** i
# print(checksumm)


        # 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся
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


        # 5 Реализуйте алгоритм перемешивания списка.
        # Из библиотеки random использовать можно только randint

# import random
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# random.shuffle(lst)
# print(lst)


# второй вариант)

import random
def mix_list(list_original):
    # Создаем копию, поскольку мы не должны изменять оригинал
    list = list_original[:]
    # Цикл от 0 до длины списка -1
    list_length = len(list)
    for i in range(list_length):
        # Получение случайного индекса
        index_aleatory = random.randint(0, list_length - 1)
        # Замена
        temp = list[i]
        list[i] = list[index_aleatory]
        list[index_aleatory] = temp
    # Возвращаем список
    return list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mixed_list = mix_list(list)
print("Исходный список: ")
print(list)
print("Перемешанный список: ")
print(mixed_list)
