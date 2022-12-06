# items = list(map(int, input().split()))
#
# print(*items)
# # Печатай смотри что получается. Ввод ручной
#
#

# lst = []
#
# for x in range(-2, 7):
#     if x % 2 == 0:
#         lst.append(x * x)
#
# print(lst)
#
# lst1 = [x * x for x in range(-2, 7) if x % 2 == 0]
#
# print(lst1)


# Задача 1 Поиск потерянной цифры в файле text.txt

# with open('text.txt') as f:
#     for item in map(int, f.read().split( )):



# 2. Напишите программу, удаляющую из текста все слова, содержащие "абв

# txt = input()
# txt = txt.split()
# new_txt = list(filter(lambda x: 'абв' not in x, txt))
# print(new_txt)



# 3 . Дан список чисел. Создайте список, в который попадают числа, описываемые
#   возрастающую последовательность. Порядок элементов менять нельзя.
lst = [1,2,4,0,3,4,5,6]


lst1 = [3,12,4,5,6,4,5,6,34,5,56]
lst2 = []
for i in lst1:
    if lst1.count(i) == 1:
        lst2.append(i)
print(lst2)


