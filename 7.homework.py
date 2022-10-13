'''
Напишите программу, которая считывает две строки текста с клавиатуры
и выведет его на экран буквы, которые есть одновременно и в первой
и во второй строке.
'''
text_one = set(input("Enter your massage: ", ))
text_two = set(input("Enter your second massage: ", ))
print(text_one & text_two)
'''
Напишите программу, которая сгенерирует на экране два списка. Один с числами кратными
3, другой с числами кратными 5. С помощью множэств создайте список с числами, которые 
есть в обоих ножествах.
'''
import random

list_one = []
list_two = []

while len(list_one) <= 10:
    term = random.randint(1, 100)
    if term % 3 == 0:
        list_one.append(term)
while  len(list_two) <= 10:
    term = random.randint(1, 100)
    if term % 5 == 0:
        list_two.append(term)

print("First list:", list_one)
print("Second list:", list_two)
print(set(list_one) & set(list_two))