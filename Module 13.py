# Задача 1. Сумма чисел 2
# def sum_number(user_number):
#     sum_number = 0
#     for number in range(1, user_number + 1):
#         sum_number += number
#     return sum_number
#
# user_number = int(input('Введите число: '))
#
# sum_user_number = sum_number(user_number)
# print('Сумма числа', user_number, 'равна:', sum_user_number)
# sum_user_sum = sum_number(sum_user_number)
# print('Сумма числа', sum_user_number, 'равна:', sum_user_sum)

# # Задача 2. «Назад в будущее»
#
# def gcd(a, b):
#     while a != 0 and b != 0:
#         if a > b:
#             a = a % b
#         else:
#             b = b % a
#     print('Наибольший общий делитель:', a + b)
#
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# gcd(a,b)

# # Задача 3. Приоритет задач
#
# def greatest_number(count_number):
#     max_number = int()
#     for number in range(1, count_number + 1):
#         user_number = int(input('Введите число: '))
#         if user_number > max_number:
#             max_number = user_number
#     return max_number
#
# count_number = int(input('Введите кол-во задач:'))
# greatest_number = greatest_number(count_number)
# print('Первая задача на обработку:', (greatest_number))


# # Задача 1. Возможности компьютера
#
# num = 1
# count = 0
#
# while num != 0:
#     num /= 2
#     count += 1
# print('Кол-во попыток:', count)

# # Задача 2. Тестирование
#
# x = 1
# user_num = float(input('Ввдеите число: '))
# count = 0
#
# while x <= 2:
#     x += user_num
#     count += 1
# print('Кол-во попыток:', count)

# # Задача 3. Урок информатики
#
# user_num = float(input('Ввдеите число больше 10: '))
# count = 0
#
# while user_num > 10:
#     user_num /= 10
#     count += 1
#
# print('Формат плавающей точки:', 'x =', user_num, '* 10 **', count)

# # Задача 1. Опять налоги
#
# def nalog (old_budget, new_tax):
#     while old_budget % 10 == 0:
#         old_budget /= 10
#         new_tax /= 10
#     if int(old_budget + new_tax) == int(old_budget):
#         print("Бюджет не изменился")
#     else:
#         print("Бюджет изменился")
#
# budget = float(input('Введите бюджет страны: '))
# new_tax = float(input('Новые поступления (налог): '))
#
# nalog(budget, new_tax)
#
# # Задача 2. Сравнение
#
# def eqv(first, second, third):
#     return abs((first + second) - third) <= 1e-15
#
# first_number = float(input('Введите число: '))
# second_number = float(input('Введите число: '))
# third_number = float(input('Введите число: '))
#
# print(eqv(first_number, second_number, third_number))




