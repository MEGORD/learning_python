'''
Используя словарь, напишите программу, которая выведет на экран
название дня недели по его номеру.
'''
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saterday", "Sunday"]
dict = {}
i = 0

for days in week:
    dict[i + 1] = week[i]
    i += 1
i = int(input("Enter number of a day: "))

print(dict[i])
'''
Представьте описание кота (домашнее животное) на основе словаря.
'''
name = "Busia"
dict_c = dict()
dict_c[name] = dict()

dict_c[name]["age"] = 5
dict_c[name]["сolor"] = "white"
dict_c[name]["sex"] = "female"
dict_c[name]["eye"] = "red"
dict_c[name]["character"] = "bad"

print(name, "=>", dict_c[name])
'''
Напишите программу которая считает строку текста с клавиатуры
и выведет на экран статистику, сколько раз какая буква встречается.
'''
line = "Hellow world"
dict = {}
line = line.replace(' ', '')
line = line.lower()

for letter in line:
    number = dict.get(letter)
    if number is None:
        dict[letter] = 1
    else:
        dict[letter] = number + 1

print(dict)