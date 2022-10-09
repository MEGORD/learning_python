'''
Напитшите программу которая посчитает сколько
букв "b" в введенной строке текста.
'''
text = input("Enter text :", )
flag = 0

for words in text:
    if words == "b":
        flag += 1
print("Count of a b:", flag)
'''
Считайте строку, которая будет представлять имя
человека, введенное с клавиатуры. Проверьте эту строку
на валидность.
'''
text = input("Enter a name: ", )

if text == text.title():
    print(text)
else:
    print("You entered the wrong person's name.")
'''
Напишите программу, которая вычислить сумму всех кодов символов строки.
'''
text = input("Enter text :", )
temp = 0

for number in text:
    temp += ord(number)
print(temp)
'''
Выведите на экран 10 строк со значениями числа Pi.
В первой строке должно быть 2 знака полсле запятой,
во второй 3 и так далее.
'''
import math
for n in range(1, 10):
    print("Pi = {number:.{num}f}".format(num = n + 1, number = math.pi))
'''
Вводится строка из слов, разделенных пробелами.
Найти самое длинное слово и вывести его на экран.
'''
text = input("Enter text :", )
text_part = text.split(" ")
text_get = ""

for num in text_part:
    if len(text_get) < len(num):
        text_get = num
print(text_get)