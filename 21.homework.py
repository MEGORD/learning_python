'''
Создайте дескриптор, который будет делать поля класса управляемые
им доступными только для чтения.
'''
class ReadDescriptor:
    def __init__(self, initial_value=None):
        self.value = initial_value

    def __get__(self, instance, owner):
        print("Hellow")
        return self.value

    def __set__(self, instance, value):
        print("Hellow")
        raise AttributeError("Can't modify read-only attribute")

class Reading:
    read_attr = ReadDescriptor("initial value")


object = Reading()

var = object.read_attr
object.read_attr = 'Something'
'''
Реализуйте функционал, который будет запрещать установку полей класса любыми значениями,
кроме целых чисел. Т.е., если тому или иному полю попытаться присвоить, например, строку, то должно
быть возбужденно исключение.
'''
class IntegerDescriptor:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("must be an integer")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)

class Value:
    integer_attr = IntegerDescriptor()

smt = Value()

smt.integer_attr = 124312
print(smt.integer_attr)
'''
Реализуйте свойство класса, которое обладает следующим функционалом: при установки значения
этого свойства в файл с заранее определенным названием должно сохранятся время (когда устанавливали
значение свойства) и установленное значение.
'''
import datetime

class Property:
    def __init__(self, value=None, filename='test.txt'):
        self._value = value
        self._filename = filename

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        self._value = value
        with open(self._filename, 'a') as f:
            f.write(f'{datetime.datetime.now()}: {value}\n')

class Something:
    prop = Property()

object = Something()
object.prop = 42
object.prop = 24

