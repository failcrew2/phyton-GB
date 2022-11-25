    # 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
    # В качестве символа-разделителя используйте пробел.

# a, b, c = map(int, input().spilit())
# d = b**2 - 4 * a * c
# if d < o:
#     print('Решения нет')
# elif d == 0:
#     print(-b / 2*a)
# else:
#     print (-b + d ** 0.5) / 2 * a
#     print (-b - d ** 0.5) / 2 * a

        # 2. Найдите корни квадратного уравнения Ax² 
        # + Bx + C = 0 двумя способами:
        from sympy import *
a, b = map(int, input().split())
for i in range(min(a, b), a*b+1, min(a,b)):
    if i % a == 0 and i % b ==0:
        print(i)
        break
