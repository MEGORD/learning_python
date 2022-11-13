'''
Напишите функцию, вернет максимальное число из списка чисел.
'''
import random

def max_number (numbers):
    flag = 0
    for number in numbers:
        if flag <= number:
            flag = number
    return flag

numbers = []
for number in range(10):
    numbers.append(random.randint(1, 100))
print(numbers)
print(max_number(numbers))
'''
Реализуйте функцию, параметрами которой являются - два числа
и строка. Возвращает она конкатенацию строки с суммой чисел.
'''
import random
def concatenation (text, number_1, number_2):
    number = number_1 + number_2
    text = text + str(number)
    return text

text = input("Enter your text: ", )
number_1 = random.randint(100, 200)
number_2 = random.randint(100, 200)
print(concatenation(text, number_1, number_2))
'''
Реализуйте функцию рисующую на экране прямоугольник из звездочек "*".
Ее параметрами будут целые числа, которые описывают длину и
ширину такого прямоугольника.
'''
def rectangle (height, widht):
    i = 1
    j = 1
    while i <= height:
        while j <= widht:
            if i == 1 or i == widht or j == 1 or j == height:
                print("*", end='')
                j += 1
                continue
            print(" ", end='')
            j += 1
        print()
        j = 1
        i += 1

h = int(input("Enter height of rectangle: "))
w = int(input("Enter weight of rectangle: "))

rectangle(h, w)
'''
Напишите функцию, котораяч реализует линейный поиск элемента в списке
целых чисел. Если такой элемент в спискуе есть, то верните его индекс,
если нет, то верните число "-1".
'''
import random
def search_index_element (list, element):
    indexes = []
    i = 0
    for number in list:
        if number == element:
            indexes.append(i)
        i += 1
    if indexes == []:
        return "-1"
    else:
        return indexes

numbers = []
for number in range(10):
    numbers.append(random.randint(1, 100))
print(numbers)
element = int(input("Enter number from 1 to 100: "))
print(search_index_element(numbers, element))
'''
Напишите функцию, которая верент количество слов в строке текста.
'''
def count_words (text):
    count = 1
    for letter in text:
        if letter == " ":
            count += 1
    if text == "":
        count = 0
    return count

text = input("Enter your text: ")
print(count_words(text))