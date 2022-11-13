'''
Напишите функцию, которая вернет сумму всех нечетных элементов списка.
'''
import random
def summ_odd (list):
    summ = 0
    for element in list:
        if not element % 2 == 0:
            summ += element
    return summ

list = []
for element in range(10):
    list.append(random.randint(1, 100))
print(list)
print(summ_odd(list))
'''
Напишите функцию, которая будет рисовать на экране треугольник заданной высоты.
Символ, которым рисуется треугольник, так же должен быть параметром этой функции.
'''
def triangle (height, symbol = '#'):
     i = 1
     while i <= height:
         print(i * symbol)
         i += 1
height = int(input("Enter the height of your triangle: "))
triangle(height, "@")
'''
Напишите программу, которая попросит ввести пользователя его имя и возраст.
После проверки возраста на корректность (что-бы не был меньше 0 или больше 500)
выведите имя человека и его возрастную градацию:
0 - 10 - детский возраст (childhood)
10 - 25 - юный возраст (youth)
25 - 44 - молодой возраст (youthfulness)
44 - 60 - средний возраст (average age)
60 - 75 - пожилой возраст (elderly)
75 - 90 - старческий возраст (old age)
 > 90 - долгожитель (long-liver)
'''
age_list = [10, 25, 44, 60, 75, 90, 500]
age = {
    10:"childhood",
    25:"youth",
    44:"youthfulness",
    60:"average_age",
    75:"elderly",
    90:"old_age",
    500:"long-liver"
}

your_name = input("Enter your name: ", )
your_age = int(input("Enter your age: ", ))
while True:
    if 0 > your_age or your_age > 500:
        your_age = int(input("Enter your age again : ", ))
    else:
        break
index = 0
for number in age_list:
    if number >= your_age:
        break
    else:
        index += 1

print("Your name -", your_name)
print("Your age -", age[age_list[index]])