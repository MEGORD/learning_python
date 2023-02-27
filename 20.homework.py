'''
Создайте декоратор, который зарегистрирует декорируемый класс в
списке классов.
'''
REGISTRED = []

def register(cls):
    REGISTRED.append(cls)

@register
class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y

print(REGISTRED)
'''
Создайте декоратор класса с параметром. Параметром должна біть
строка, которая должна дописываться (слева) к результату работы метода
__str__.
'''
def adder(cls):
    def wrapper(self):
        string = "I'm on the left - " + self
        return string
    return wrapper

@adder
class Massage:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

test = Massage("I'm on right")

print(test)
'''
Для класса Box напишите статический метод, который будет подсчитывать суммарный обьем
двух ящиков, которые будут его параметрами.
'''
import random

class Box:
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height

    def volume(self):
        return self.width * self.length * self.length

    @staticmethod
    def double_volume():
        Box1 = Box(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
        Box2 = Box(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
        print(f"Volume of this boxes = {Box1.volume() + Box2.volume()}.")

Box.double_volume()