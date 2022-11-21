'''
Создайте класс, описывающий человека (создайте метод, выводящий информацию о человеке).
'''
class Human:
    def __init__(self, name, surname, gender, age):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age

    def __str__(self):
        return "Name : {}, surname : {}, gender : {}, age = {}".format(self.name, self.surname, self.gender, self.age)
'''
На его основе создайте класс Студент (переопределите метод вывода информации)
'''
class Student(Human):
    def __init__(self, name, surname, gender, age, character, several_rating):
        super().__init__(name, surname, gender, age)
        self.character = character
        self.several_rating = several_rating

    def __str__(self):
        return super().__str__() + ", character : {}, several_rating = {}".format(self.character, self.several_rating)
'''
Создайте класс Группа, который содержит список из обьектов класса Студент. Реализуйте методы добавления, удаления
студента и метод поиска студента по фамилии. Определите для Группы метод __str__() для возвращения списка студентов
в виде строки.
'''
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

ITIP.cross_s(one_human)

ITIP.searching("Penkov")
print()
print(ITIP)