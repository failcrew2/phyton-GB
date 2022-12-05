# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму
# элементов списка, стоящих на нечётной позиции.

some_lst = list(map(int, input('Введи числа: ').split()))
ne_chet = 0
counter = 0
for i in some_lst:

    if counter % 2 == 0:

        ne_chet += abs(i)

        counter += 1

print(f' Сумма нечетных чисел = {ne_chet}',{summ})



