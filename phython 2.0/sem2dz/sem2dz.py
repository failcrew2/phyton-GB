# 1 Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр.
# Задача Номер два входит в код.
# На семинаре сказали что примите решение двух задач одним кодом.

n = int(input(' Введите числo: '))
sum = 0
# Начало решение второй
some_list = [1]
fact = 1

for i in range(2, n + 1):
    fact *= i
    some_list.append(fact)
    # Конец решения второй

# Начало решение первой
while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10

# Принты
print ('Сумма цифр: ' , sum)
print('Произведение: ', some_list)

# Столкнулся с проблемой, бесконечного цикла второй задачи p.s делаю в пайчарм.
# Принт второй задачи не выводит большие числа, если использовать пример 6782 с первой задачи ничего не происходит.
# Ошибкой не считается же?))))

# Задача 3
