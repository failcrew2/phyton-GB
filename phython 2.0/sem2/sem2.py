# 3 задача вхождения в строку

some_str_1 = input()
some_str_2 = input()
len_str_2 = len(some_str_2)
i = 0
count = 0
while i < len(some_str_1):
    if some_str_1[i:i + len_str_2] == some_str_2:
        count += 1
    i += 1
print(count)

# 1 задача

n = int(input())

count = 1

#5print (f'{n}')
for i in range(n - 1):
    print(f"{count}", end= ', ')
    count = count * (-3)
print(count)

# 2

