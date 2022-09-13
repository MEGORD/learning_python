'''
С помощью одного цикла нарисовать фигуру максимальная высота которой
вводится с клавиатуры.
*
**
***
**
*
'''
n = int(input("Enter the height of your figure: "))
i = 1
f = False

while n > 0:
    if i == n or f == True:
        print(i * "*")
        i -= 1
        f = True
        if i == 0:
            break
        continue
    print(i * "*")
    i += 1
'''
С помощью циклов вывести на экран все простые числа от 1 до 100.
'''
i = 2

while i <= 100:
    if i == 2 or i == 3 or i == 5 or i == 7:
        print(i)
    elif i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
        print(i)
    i += 1
'''
Вывести на экран "песочные часы", максимальная ширина который считывается с клавиатуры
нечетным числом.
'''
s = int(input("Enter odd size of clock: "))
i = 0
flag = True
f = 1
control = 1
while i <= s:
    if not flag:
        j -= 1
        f = f + control * 2
        print(" " * (j - 2), "*" * int(f))
        i += 1
        if i == s + 1:
            break
    else:
        f = s - i * 2
        print(" " * i, "*" * f)
        i += 1
        if i == s // 2 + 1:
            flag = False
            i += 1
            j = i