# 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

# num = int(input(' Введите число: '))
# def checkNumber(num):
#     if 6 <= num <=7:
#         print(' yes ')
#     elif 0 < num < 6:
#         print(' no ')
#     else:
#         print('в неделе 7 дней :)')
# checkNumber(num)


# 2 Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# def inputNums(x):
#     xyz = ["X", "Y", "Z"]
#     a = []
#     for i in range(x):
#         a.append(input(f"Введите значение {xyz[i]}: "))
#     return a


# def checkPredicate(x):
#     left = not (x[0] or x[1] or x[2])
#     right = not x[0] and not x[1] and not x[2]
#     result = left == right
#     return result


# statement = inputNums(3)

# if checkPredicate(statement) == True:
#     print(f"Утверждение истинно")
# else:
#     print(f"Утверждение ложно")


# 3 Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится). 
# Пример: - x=34; y=-30 -> 4 - x=2; y=4-> 1 - x=-34; y=-30 -> 3 


# def inputCordination(x):
#     a = [0] * x
#     for i in range(x):
#         is_OK = False
#         while not is_OK:
#             try:
#                 number = float(input(f"Введите {i+1} координату: "))
#                 a[i] = number
#                 is_OK = True
#                 if a[i] == 0:
#                     is_OK = False
#                     print("Координата не должно быть равна 0 ")
#             except ValueError:
#                 print("Вводить надо числа!")
#     return a


# def checkCordioantion(xy):
#     text = 4
#     if xy[0] > 0 and xy[1] > 0:
#         text = 1
#     elif xy[0] < 0 and xy[1] > 0:
#         text = 2
#     elif xy[0] < 0 and xy[1] < 0:
#         text = 3
#     print(f"Точка находится в {text} четверти плоскости")


# koordinate = inputCordination(2)
# checkCordioantion(koordinate)



# 4 Напишите программу, которая принимает на вход координаты двух точек 
#и находит расстояние между ними в 2D пространстве.


# def inputNumbers(x):
#     xy = ["X", "Y"]
#     a = []
#     for i in range(x):
#         is_OK = False
#         while not is_OK:
#             try:
#                 number = int(input(f"Введите координату по {xy[i]}: "))
#                 a.append(number)
#                 is_OK = True
#             except ValueError:
#                 print("Ты ошибся. Вводить надо целые числа!")
#     return a


# def calculateLengthSegment(a, b):
#     lengthSegment = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
#     return lengthSegment


# print("Введите координаты точки А")
# pointA = inputNumbers(2)
# print("Введите координаты точки В")
# pointB = inputNumbers(2)

# print(f"Длина отрезка: {format(calculateLengthSegment(pointA, pointB), '.2f')}")



print("Введите координаты точки:")
x = float(input("x = "))
y = float(input("y = "))
if x > 0 and y > 0:
    print('Точка находится в 1 четверти')
elif x < 0 and y > 0:
    print('Точка находится в 2 четверти')
elif x < 0 and y < 0:
    print('Точка находится в 3 четверти')
elif x > 0 and y < 0:
    print('Точка находится в 4 четверти')