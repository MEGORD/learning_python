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