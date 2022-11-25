# Проверка на квадратность task 1
#print('Введите Первое число: ')
#a = int(input())
#print('Введите Второе число: ')
#b = int(input())
#if a == b * b:
#    print('Да')
#elif b == a * a:
#    print('Да')
#else:
#    print('Нет')

# Task 2 поиск максимума

# number = int(input())
# maxx = number
# for _ in range(4):
#     number = int(input())
#     if number > maxx:
#         maxx = number
# print(maxx)
#
# some_list = []
# for _ in range(5):
#     number = int(input())
#     some_list.append(number)
# maxx = some_list[0]
# for element in some_list:
#     if element > maxx:
#         maxx = element
# print(maxx)

# print(max(map(int, input().split())))

# task 3 от -N до N

#number = int(input('Введите число'))
#for i in range(-number, number+1):
#    print(i)


# task 4 перевел в строку или - Списки list

#some_list = [] 
#number = int(input('Введите число'))
#print()
#for i in range(-number, number+1):
#    some_list.append(i)
#print(some_list)

# task 5 дробные 

# Математическое решение таск 5

# n = float(input())
# if n % 1 == 0:
#     print('no')
# else:
#     print((int(n * 10) % 10))

# не математическое решение 

# n = input()
# if '.' in n:
#     index_t = n.find('.')
#     print(n[index_t + 1])
# else:
#     print('нет')


# task 6 Число на вход кратно ли 5 , 10 или 15 но не 30


n = int(input(' Введите число: '))
if (n % 5 == 0 and n % 10 == 0 or n % 15 == 0) and n % 30 != 0:
    print('да')
else:
    print('нет')
