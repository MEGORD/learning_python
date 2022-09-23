'''
1. Написать программу, которая считает 4 числа
с клавиатуры и выведет на экран самое большое
из них.
'''
first = int(input('Enter first: '))
second = int(input('Enter second: '))
third = int(input('Enter third: '))
fourth = int(input('Enter fourth: '))

if first >= second >= third >= fourth:
    print('Max =', first)
elif second >= first >= third >= fourth:
    print('Max =', second)
elif third >= first >= second >= fourth:
    print('Max =', third)
else:
    print('Max =', fourth)
'''
2. Есть девятиэтажный дом, в котором 4 подьезда.
Номер подьезда начинается с единицы. На одном этаже
4 квартиры. Напишите программу которая, получит
номер квартиры с клавиатуры, и выведет на экран,
на каком этаже, какого подьезда расположена эта квартира.
Если такой квартиры нет в этом доме, то нужно сообщить
об этом пользователю.
'''
n_flat = int(input('Enter number of a your flat: '))

if n_flat > 9 * 4 * 4 or n_flat <= 0:
    print('This apartment does not exist.')
else:
    if n_flat % 36 == 0:
        print('Number of entrance =', int(n_flat / 36))
    else:
        print('Number of entrance =', int((n_flat / 36) + 1))
    if n_flat % 36 % 4 == 0:
        print('Number of floor = ', int((n_flat - 1) % 36 / 4 + 1))
    else:
        print('Number of floor = ', int(n_flat % 36 / 4 + 1))
'''
3. Определить количество дней в году, который вводит пользователь.
В високосном году - 366 дней, тогда как в обычном их 365.
Високосный год определяется по следующему правилу:
Год високосный, если он делится на четыре без остатка, но если
он делится на 100 без остатка, это не високосный год. Однако,
если он делится без остатка на 400, это високосный год.
'''
c_year = int(input('Enter count of a year: '))

if c_year % 400 == 0:
    print('366')
elif c_year % 100 == 0:
    print('365')
elif c_year % 4 == 0:
    print('366')
else:
    print('365')
'''
4. Треугольник существует только тогда,
когда сумма любых двух его сторон больше третьей.
Дано: a, b, c - стороны предполагаемого треугольника.
Напишите программу, которая укажет, существует ли такой
треугольник или нет.
'''
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

if a + b > c and a + c > b and b + c > a:
    print('Trinangle is a real')
else:
    print('Trinangle isnt a real')
