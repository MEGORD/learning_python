'''
Создайте класс "Прямоугольник", у которого присутствуют два поля
(ширина и высота). Реализуйте метод сравнения прямоугольников по площади.
Также реализуйте методы сложения прямоугольников (площадь суммарного
прямоугольника должна быть равна сумме площадей прямоугольников, которые вы складываете).
Реализуйте методы умножения прямоугольника на число n (это должно увеличить
площадь базового прямоугольника в n раз).
'''
import math

class Rectangle:
    def __init__(self, w ,h):
        self.weight = w
        self.heigh = h

    def get_square(self):
        square = self.weight * self.heigh
        return square

    def compare_s(self):
        return  rec1.get_square() > rec2.get_square()

    def multiplication_s(self, r1, n):
        n_square = r1.get_square() * n
        return n_square

    def __add__(self, other):
        side = math.sqrt(self.weight * self.heigh + other.weight * other.heigh)
        n_rectangle = Rectangle(side, side)
        return n_rectangle

    def __str__(self):
        return "Rectangle : heigh = {}, weigh = {} .".format(self.heigh, self.weight)

rec1 = Rectangle(1, 3)
rec2 = Rectangle(3, 4)

rec3 = rec1 + rec2

print(rec3.compare_s())
'''
Создайте класс "Правильная дробь" и реализуйте методы сравнения, сложения
вычитания и произведения для экземпляров этого класса.
'''
class P_fraction:
    def __init__(self, nomerator, denomerator):
        P_fraction.cheker(self, nomerator, denomerator)
        self.nomerator = nomerator
        self.denomerator = denomerator

    def cheker(self, nomerator, denomerator):
        if nomerator > denomerator:
            raise Exception("Error: {} < {}".format(nomerator, denomerator))

    def __add__(self, other):
        sum_n = self.nomerator + other.nomerator
        sum_d = self.denomerator + other.denomerator
        return str(sum_n) + "/" + str(sum_d)

    def __sub__(self, other):
        sub_n = self.nomerator - other.nomerator
        sub_d = self.denomerator - other.denomerator
        return str(sub_n) + "/" + str(-sub_d)

    def __mul__(self, other):
        mul_n = self.nomerator * other.nomerator
        mul_d = self.denomerator * other.denomerator
        return str(mul_n) + "/" + str(mul_d)

    def __eq__(self, other):
        n1 = self.nomerator / self.denomerator
        n2 = other.nomerator / other.denomerator
        equals = n1 == n2
        return equals

    def __str__(self):
        return str(self.nomerator) + "/" + str(self.denomerator)

num1 = P_fraction(1, 2)
num2 = P_fraction(2, 4)

num3 = num1 == num2
print(num3)