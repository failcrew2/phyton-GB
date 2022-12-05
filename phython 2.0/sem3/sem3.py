# # Поиск по множествам
#
# s = set()
# s.add('222')
# print(hash('222' in s))


# Пресворандом без import random

from time import time

# from time import time
#
# def randfromtime(max):
#     time1 = time()
#     time1 = (time1 - int(time1))
#     return int(time1 * max)
#
# print(randfromtime(1000))

# Задайте список. Напишите программу,
# которая определит, присутствует ли в
# заданном списке строк некое число.
# ['22', '33', '123', 'fwefe', 'ytyy', '55']

# our_list = ['22', '33', '123', 'fwefe', 'ytyy', '55']
# u = 55
# print(our_list)
#
# for i in range (len(our_list)):
#     if our_list[i].isdigit() and int(our_list[i]) == u:
#         print(f'В списке присудствует то что вы ищете \n На позиции {i} ' )


# 3. Напишите программу, которая определит позицию второго вхождения строки в
# списке либо сообщит, что её нет.
#
# *Пример:*
#
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1



our_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
u = 'qwe'
count = 0
print(our_list)

for i in range (len(our_list)):
    if our_list[i] == u:
        count += 1
        if count == 2:
            break
print(f'Второе вхождение строки в список на {i} позиции' )