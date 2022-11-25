# 41. Напишите программу вычисления арифметического выражения
# заданного строкой. Используйте операции
# +, -, /, *. Приоритет операций стандартный.
import inp as inp

inp = input(' Дай Газ ')
res = []
n = 0
for i in (len()):
            if inp[i] in ("+", "-", "*", "/"):
                res.append(int(inp[n:i]))
                res.append(inp[i])
                n = i + 1
            res.append(int(inp[i:]))
print(res)


# import re
#
# srt = str(input(''))
# str = str.split(' ')
# actions = {
#     "^": lambda x, y: str(float(x) ** float(y)),
#     "*": lambda x, y: str(float(x) * float(y)),
#     "/": lambda x, y: str(float(x) / float(y)),
#     "+": lambda x, y: str(float(x) + float(y)),
#     "-": lambda x, y: str(float(x) - float(y))
# }
# for i in range(len(str)):
#     if str[i] == '*':
#         mult = str[i - 1] * int(str[i + 1])
#     elif str[i] == '/':
#         delen = int(str[i-1]) / int(str[i + 1])
#     elif str[i] == '+':
#         result = int(str[0]) + int(str[2])
#     elif str[i] == '-':
#         result = int(str[0]) - int(str[2])
#
# print(result)

# def f(inp):
#     res = []
#     n = 0
#     for i in range(len(inp)):
#         if inp[i] in ("+", "-", "*", "/"):
#             res.append(int(inp[n:i]))
#             res.append(inp[i])
#             n = i + 1
#     res.append(int(inp[i:]))
#     return res