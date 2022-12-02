'''
Напишите программу, которая реализует функциональность считывая с клавиатуры стоимости товара. При этом стоит учесть,
что пользователь может ввести не цифры, а смесь цифр и букв или отрицательное число. При необходимости создайте
пользовательное исключение и обработайте его (например, для отрицательных чисел).
'''
class NegativeValueEror(Exception):
   def __init__(self, number):
       super().__init__()
       self.number = number
   def __str__(self):
        return "Input positive number"

while True:
    try:
       number = float(input("Enter cost of product: "))
       if number < 0:
            raise NegativeValueEror(number)
       break
    except ValueError as err:
        print("Try again")
    except NegativeValueEror as err:
        print(err)
print(number)
'''
Модифицируйте класс Группа (задание прошлой лекции) так, чтобы при попытке добавления в группу более 10-ти студентов,
было возбужденно пользовательское исключение. Таким образом нужно создать еще и пользовательское исключение для этой
ситуации. И обработать его.
'''
class Human:
    def __init__(self, name, surname, gender, age):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age

    def __str__(self):
        return "Name : {}, surname : {}, gender : {}, age = {}".format(self.name, self.surname, self.gender, self.age)
class Student(Human):
    def __init__(self, name, surname, gender, age, character, several_rating):
        super().__init__(name, surname, gender, age)
        self.character = character
        self.several_rating = several_rating

    def __str__(self):
        return super().__str__() + ", character : {}, several_rating = {}".format(self.character, self.several_rating)

class TooMuch(Exception):
    def __init__(self, list):
        super().__init__()
        self.list = list
    def __str__(self):
        return "Your group is too big."

class Group:
    def __init__(self, year, course, university):
        self.year = year
        self.course = course
        self.university = university
        self.list = []

    def plus_s(self, student):
        self.list.append(student)

    def cross_s(self, student):
        self.list.remove(student)

    def searching(self, surname):
        flag = 0
        for element in self.list:
            if element.surname == surname:
                print(element)
                flag = 1
        if flag == 0:
            print("This student not in this group.")

    def l_list(self):
        return len(self.list)

    def __str__(self):
        n_list = []
        nr_list = ""
        for element in self.list:
            n_list = str(element)
            nr_list += n_list + '\n'
        return nr_list

one_human = Student("Alexei", "Arcanist", "M", 18, "tolerant", 4.2)
two_human = Student("Olga", "Sebrenkova", "W", 18, "bad", 4.2)
three_human = Student("Vlodimir", "Penkov", "M", "19", "good", 3.7)

ITIP = Group(21, 2, "KHNURE")

ITIP.plus_s(one_human)
ITIP.plus_s(three_human)
ITIP.plus_s(two_human)

for i in range(1, 10):
    try:
        ITIP.plus_s(two_human)
        if ITIP.l_list() >= 10:
            raise TooMuch(list)
    except TooMuch as err:
        print("Your group is too big.")
        ITIP.cross_s(two_human)

print(ITIP)