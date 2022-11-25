# 1. Вычислить число c заданной точностью d

# n = float(input('Введите первое число: '))
# d = float(input('Введите Второе число: '))
# if d == 1:
#     print(int(n))
# else:
#     d = str(d)
#     d = d.split('.')
#     d = len(d[1])
#     print(round(n, d))


# 2. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

# n = int(input('Введите число: '))
# lst = []
# for i in range(2, n // 2 + 1):
#     if n % i == 0:
#         for j in range(2, i // 2 + 1):
#             if i % j == 0:
#                 break
#         else:
#             lst.append(i)
# print(lst)

# 3. Задайте последовательность чисел. Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.

# lst1 = [3,12,4,5,6,4,5,6,34,5,56]
# lst2 = []
# for i in lst1:
#     if lst1.count(i) == 1:
#         lst2.append(i)
# print(lst2)


# # 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# # (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
# from random import randint
# import random
#
# k = int(input('Введите натуральную степень k: '))
# while k <= 0:
#     k = int(input('Введены не корректные данные! Введите натуральную степень k: '))
#
# result = [0 for i in range(k)]
# koef = random.sample(range(0, 101), k + 1)
# print(f'Рандомные коэффициенты: {koef}')
# for i in range(len(result)):
#     result[i] = f'{koef[i]}x^{k}'
#     k -= 1
# result.append(str(koef[-1]))
# print(f'До обработки: {result}')
# for elem in result:
#     if elem == 0:
#         result.remove(elem)
#     try:
#         ind_x = elem.find('x')
#         d = int(elem[:ind_x])
#     except AttributeError:
#         continue
#     if d == 0 or elem == '0':
#         result.remove(elem)
#     if '^1' in elem:
#         result.remove(elem)
#         result.insert(-1, elem[:elem.find('^1')])
# print(f'После обработки: {result}')
# polynom = ''
# for i in range(len(result) - 1):
#     polynom += f'{result[i]} + '
# polynom += f'{result[-1]} = 0'
# print(polynom)
#
# with open('text.txt', 'w') as f:
#     f.write(polynom)



## с семинара

# import random
# some_dict = {0: '⁰', 1: '¹', 2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹'}
# k = int(input('Введите натуральную степень k: '))
# coef = [random.randint(0, 100) for _ in range(k + 1)]
# print(coef)
# with open('coef.txt', 'w', encoding='utf-8') as m:
#     for i in range(len(coef)):
#         if k - i != 1 and k - i != 0:
#             m.write(f'{coef[i]}x{some_dict[k - i]} + ')
#         elif k - i == 1:
#             m.write(f'{coef[i]}x + ')
#         elif k - i == 0:
#             m.write(f'{coef[i]} = 0')
