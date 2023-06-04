# # 4.5 Практическая работа
# Задача 1. Датчик погоды
# check_rain = int(input('На улице идёт дождь?\n'))
#
# if check_rain == 1:
#     print('Пошёл дождь. Возьмите зонтик!\n')
# elif check_rain == 0:
#     print('Дождя нет!')
# else:
#     print('Введено не верное значение. Повторите попытку!')

# Задача 2. Поступление
# check_name = input('Введите имя студента: ')
# check_points_rus = int(input('Введите количество баллов по русскому языку: '))
# check_points_math = int(input('Введите количество баллов по математике: '))
# check_points_inform = int(input('Введите количество баллов по информатике: '))
# received = bool
#
# if check_points_rus + check_points_math + check_points_inform >= 250:
#     print('Поздравляю, ты поступил на бюджет!')
#     received = True
# else:
#     print('К сожалению, ты не прошёл на бюджет.')
#     received = False

# # Задача 3. Следим за расписанием
# check_date = int(input('Введите сегодняшнее число: '))
#
# if check_date % 2 == 0:
#     print('Вася, пора работать. Сегодня четный день.')
# else:
#     print('Вася, сегодня отдыхай. День нечетный.')

# Задача 4. Калькулятор скидки
# price_first_product = int(input('Введите стоимость первого товара: '))
# price_second_product = int(input('Введите стоимость второго товара: '))
# price_third_product = int(input('Введите стоимость третьего товара: '))
# total_cost = price_first_product + price_second_product + price_third_product
#
# if total_cost > 10000:
#     total_cost = total_cost - ((total_cost * 10) / 100)
#     print('Итоговая сумма, вместе со скидкой, равна: ', total_cost)
# else:
#     print('Итоговая сумма покупки равна:', total_cost)

# Задача 5. Модуль числа
#
# value_x = int(input('Введите значение числа Х: '))
#
# if value_x < 0:
#     value_x = -value_x
#     print('Модуль числа X равен:', value_x)
# else:
#     print('Модуль числа X равен:', value_x)

# Задача 6. Игра в кубики
# number_guest = int(input('Введите число выпавшее у посетителя: '))
# number_owner = int(input('Введите число выпавшее у Владельца: '))
#
#
# if number_guest >= number_owner:
#     print('Игрок платит', '\nРазность равна: ', number_guest - number_owner)
# elif number_guest < number_owner:
#     print('Владелец платит', '\nСумма равна: ', number_guest + number_owner)
# print('Игра окончена')
#

# Задача 7. Хватит ли зарплаты
# quantity_hours = int(input('Введите количество рабочих чаcов: '))
# credit_balance = int(input('Введите остаток по кредиту: '))
# money_food = int(input('Введите количество необходимых денег на еду: '))
#
# salary = ((200 * quantity_hours) / 2**3) + quantity_hours
#
# if salary >= credit_balance + money_food:
#     print('Часов хватает. Можно отдохнуть.')
# else:
#     print('Часов не хватает. Придётся работать больше!')

# Задача 8. Максимальное число (по желанию)
# first_number = int(input('Введите первое число: '))
# second_number = int(input('Введите второе число: '))
# third_number = int(input('Введите третье число: '))
#
# if first_number > second_number and first_number > third_number:
#     print('Самым большим оказалось первое число: ', first_number)
# elif second_number > first_number and second_number > third_number:
#     print('Самым большим оказалось второе число: ', second_number)
# else:
#     print('Самым большим оказалось третье число: ', third_number)

# # Второй вариант решения
# first_number = int(input('Введите первое число: '))
# second_number = int(input('Введите второе число: '))
# third_number = int(input('Введите третье число: '))
# check_max = int()
#
# if first_number > second_number:
#     check_max = first_number
# else:
#     check_max = second_number
#
# if check_max < third_number:
#     check_max = third_number
# else:
#     check_max = check_max
#
# print('Наибольшим числом оказалось: ', check_max)