# 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# count = int(input('Введите количество элементов: '))
# some_list = []
# sum = 0
# for _ in range(count):
#     number = int(input())
#     some_list.append(number)
# for idx in range(1, count, 2):
#     sum += some_list[idx]
# print(sum)


# 2.  Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


# count = int(input('Введите количество элементов: '))
# some_list = []
# for _ in range(count):
#     number = int(input())
#     some_list.append(number)
# new_list = []
# for id in range((count -1)// 2 + 1):
#     num1 = some_list[id]
#     num2 = some_list[count - id - 1]
#     new_list.append(num1 * num2)
# print(new_list)

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.

# count = int(input('Введите количество элементов: '))
# some_list = []
# for _ in range(count):
#     number = float(input())
#     some_list.append(number)
# minn = 1
# maxx = 0
# for el in some_list:
#     if '.' in str(el):
#         dr = str(el).split('.')[1]
#         if float('0.' + dr) > maxx:
#             maxx = float('0.' + dr)
#         elif float('0.' + dr) < minn:
#             minn = float('0.' + dr)
# print(maxx - minn)

# 4. Напишите программу, которая будет
# преобразовывать десятичное число в двоичное.

# a = int(input('Введите число для перевода в двочное: '))
# print(bin(a)[2:])

# 5. Числа фибоначчи

a = int(input('Введите число: '))
some_list = [0] * (a * 2 + 1)
some_list[a + 1] = 1
for idx in range(a + 2, a * 2 + 1):
    some_list[idx] = some_list[idx - 1] + some_list[idx - 2]
for idx in range(a, -1, -1):
    some_list[idx] = some_list[idx +2] - some_list[idx + 1]
print(some_list)