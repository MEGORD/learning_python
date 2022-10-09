'''
Ввести с клавиатуры число (до миллиарда), которое обозначает
количество долларов и центов пользователя. Вывести это
количество прописью.
'''
# variable = int(input("Enter your number: ", ))
# numbers = ["", "million", "thousand", "units"]
# check = 1000000
# dict = {}
# i = 0
# while check >= 1:
#     i += 1
#     if variable // check == 0:
#         check = check / 1000
#         continue
#     dict[i] = variable // check % 1000
#     check = check / 1000
#     print(numbers[i], "=>", dict[i], "dollars")
'''
Напишите программу, которая переведет целое число
(от 1 до 100) в римские цифры.
'''
variable = int(input("Enter your number from 1 to 100: ", ))

dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}