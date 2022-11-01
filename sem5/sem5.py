#Вытягивает и заполняется пробел в числе

# n = 8
# with open('text.txt', 'r', encoding='utf-8') as k:
#     some_list = list(map(int, k.read().split()))
#     for i in range(n - 1):
#         if some_list[i] != some_list[i + 1] - 1:
#             print(some_list[i + 1] - 1)

# 3 задача Удаляет текст и записывает в новый

# text = input()
# text = text.split()
# new_text = list(filter(lambda x: 'abc' not in x, text))
# print(new_text)


#2 В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число.


int_list = [0, 1, 2, 3, 4, 5, 8, 9, 11]
int_list.sort()
idx = 0
new_list = []
while idx < len(int_list):
    some_list = [int_list[idx]]
    new_idx = idx
    while new_idx + 1 != len(int_list) and int_list[new_idx] == int_list[new_idx + 1] - 1:
        some_list.append(int_list[new_idx + 1])
        new_idx += 1
    new_list.append(some_list)
    idx += len(some_list)
print(new_list)
a = []
for i in new_list:
    if len(i) != 1:
        a.append(f'{i[0]}-{i[-1]}')
    else:
        a.append(f'{i[0]}')
print(*a, sep=',')
