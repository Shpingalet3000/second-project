# # Задача 1. Язык математики
# a = 8
# b = 10
# c = 12
# d = 18
# res = ((-3 + a**2) * b - 2**3) / (c - 2 * d)
# print(res)
#
# # Задача 2. Финансовый отчёт
# firstQuarter = int(input('Введите сумму дохода за первый квартал: '))
# secondQuarter = int(input('Введите сумму дохода за второй квартал: '))
# thirdQuarter = int(input('Введите сумму дохода за третий квартал: '))
# fourthQuarter = int(input('Введите сумму дохода за четвертый квартал: '))
#
# sumFirstSecond = firstQuarter + secondQuarter
# sumThirdFourth = thirdQuarter + fourthQuarter
# divSum = sumFirstSecond / sumThirdFourth
#
# print('Динамика дохода: ', divSum)
#
# # Задача 3. Следующее и предыдущее числа
# number = int(input('Введите число: '))
# nextNumber = number + 1
# previousNumber = number - 1
#
# print('После числа ', number, 'идет число', nextNumber)
# print('До числа ', number, 'идет число', previousNumber)
#
# # Задача 4. Площадь треугольника
# lenghtA = int(input('Введите длину катета a: '))
# lenghtB = int(input('Введите длину катета b: '))\
#
# triangleArea = lenghtA * lenghtB / 2
#
# print('Площадь треугольника равна: ', triangleArea)
#
# # Задача 5. Часы
# minute = int(input('Введите количество минут: '))
#
# hours = minute // 60
# remainderMinute = minute % 60
#
# print('Кличество полных часов равно:', hours, '\nКоличество оставшихся минут равно:', remainderMinute)
#
# # Задача 6. Проверяем бухгалтера
# firstNum = int(input('Введите первое число: '))
# secondNum = int(input('Введите второе число: '))
#
# digitFirstNumber = firstNum % 100
# digitSecondNumber = secondNum % 100
#
# print('Сумма двух последний разрядов равна: ', digitFirstNumber + digitSecondNumber)
#
# # Задача 7. Режем число на части
# fourNumber = int(input('Введите четырехзначное число: '))
# firstDigit = fourNumber // 1000
# secondDigit = (fourNumber // 100) % 10
# thirdDigit = (fourNumber // 10) % 10
# fourthDigit = fourNumber % 10
#
# print('Последовательный вывод цифр числа:', firstDigit, secondDigit, thirdDigit, fourthDigit)
#
# # Задача 8. Поменять местами: не всё так просто! (необязательная, повышенной сложности)
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# print(a, b)
#
# a = a + b
# b = a - b
# a = a - b
#
# print(a, b)