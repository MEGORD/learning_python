'''
Дополните класс Группа (задание Лекции 2) возможностью поддержки
итерационного протокола.
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

class Group:
    current_student = 0

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
        itr = iter(self.list)

        while True:
            try:
                student = next(itr)
                if surname == student.surname:
                    print(student)
                    flag = 1
                if flag == 0:
                    print("This student not in this group.")
                    print(student)
            except StopIteration:
                break

    def __iter__(self):
        return self

    def __next__(self):
        try:
            current = self.list[self.current_student]
            self.current_student += 1
        except IndexError:
            raise StopIteration
        return current

    def __str__(self):
        n_list = []
        nr_list = ""
        itr = iter(self.list)

        while True:
            try:
                element = next(itr)
                n_list = str(element)
                nr_list += n_list + '\n'
            except StopIteration:
                break
        return nr_list

one_human = Student("Alexei", "Arcanist", "M", 18, "tolerant", 4.2)
two_human = Student("Olga", "Sebrenkova", "W", 18, "bad", 4.2)
three_human = Student("Vlodimir", "Penkov", "M", "19", "good", 3.7)

ITIP = Group(21, 2, "KHNURE")

ITIP.plus_s(one_human)
ITIP.plus_s(three_human)
ITIP.plus_s(two_human)

ITIP.cross_s(one_human)

print(ITIP.__next__())
print(ITIP.__next__())
print(ITIP.__next__())
'''
Модифицируйте класс Заказ (задание Лекции 1) добавив реализацию протокола
последовательностей и итерационного протокола.
'''
class Order:
    goods = 0
    def __init__(self, name, surname, product):
        self.name = name
        self.surname = surname
        self.product = product

    def whole_price(self):
        full_price = 0
        for element in self.product.values():
            full_price += element
        return "Full price : {}".format(full_price)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            current = self.product[self.goods]
            self.goods += 1
        except IndexError:
            raise StopIteration
        return current

    def __len__(self):
        return len(self.product)

    def __getitem__(self, index):
        if isinstance(index, int):
            if index >= 0 and index < len(self.product.keys()):
                return self.product[index]
            else:
                raise IndexError()
        raise TypeError()

    def __str__(self):
        return "Buyer[ ID = {} {}],\nProduct = [{}]".format(self.name, self.surname, self.product)

Buyer_1 = Order("Adrian", "Dirty-raincloak", {"Milk":50, "Water":15})

print(Buyer_1)
print(Buyer_1.whole_price())
print(Buyer_1.product["Milk"])
print(len(Buyer_1.product))