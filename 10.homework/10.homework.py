'''
№1
Напишите программу, которая запишет в фойл список целых чисел.
'''
import random

list = []
for number in range(10):
    list.append(random.randint(1, 100))
my_file = open("first.txt", "w")
for number in list:
    my_file.write(str(number))
    my_file.write(" ")
my_file.close()
'''
№2
Напишите программу, которая вычитает текст из текстового файла
и выведет на экран, сколько раз в тексте встречается буква "A".
'''
def calculate (file_adress, symbol):
    count = 0
    my_file = open(file_adress, "r")
    for text in my_file:
        for letter in text:
            letter = letter.upper()
            if letter == symbol:
                count += 1
    my_file.close()
    return count

result = calculate("second.txt", "A")

print(result)
'''
№3
Создайте консольный "текствовый редактор" с возсожностью
сохранения набранного текста в файл. (Не переусердствуйте. Имеется
ввиду, что вы сначала должны считать несколько строк с клавиатуры,
а потом сохранить считанный текст в файл).
'''
def editor (file_adress, text):
    my_file = open(file_adress, "w")
    for letter in text:
        if letter == " ":
            my_file.write(" ")
        else:
            my_file.write(letter)
    my_file.close()

text = input("Enter your text: ", )
editor("third.txt", text)
'''
№4
Напишите програму, которая найдет самое длинное слово в текстовом файле.
'''
def converter (file_adress):
    list = []
    my_file = open(file_adress, "r")
    text = my_file.read()
    list = text.split()
    my_file.close()
    return list

print(max(converter("fourth.txt"), key = len))
