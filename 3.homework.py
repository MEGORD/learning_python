'''
Выведите на экран все числа в диапазоне
от 1 до 100 кратные 7.
'''
i = 1

while i <= 100:
    if i % 7 == 0:
        print(i)
    i += 1
'''
Вычислить с помощью цикла факториал числа n
 введенного с клавиатуры (4 < n < 16).
'''
n = int(input('Enter n from 4 to 16: '))
i = 1
x = 1

while i <= n:
    x = i * x
    i += 1

print('Factorial', n, '=', x)
'''
Напечатайте таблицу умножения на 5.
'''
c = 5
i = 1

while i <= 9:
    print(i, "*", 5, "=", i * 5)
    i += 1
'''
Выведите на экран прямогульник из "*". Причем
высота и ширина прямоугольника вводятся с клавиатуры.
'''
h = int(input("Enter height of rectangle: "))
w = int(input("Enter weight of rectangle: "))
i = 1
j = 1

while i <= h:
    while j <= w:
        if i == 1 or i == w or j == 1 or j == h:
            print("*", end='')
            j += 1
            continue
        print(" ", end='')
        j += 1
    print()
    j = 1
    i += 1