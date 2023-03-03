'''
Реализуйте метакласс, который обладает следующим функционалом: при его использовании
в файл с заранее определенным названием нужно сохранить имя класса и список его полей.
'''
class ToStr:
    def __str__(self):
        filename = "test.txt"
        with open(filename, "w") as f:
            f.write(str(self.__class__.__name__)+"\n")
            for field_name in self.__dict__.keys():
                f.write(f"{field_name} = {str(self.__dict__[field_name])}")

class MetaStr(type):
    def __new__(type_class, class_name, super_classes, class_atr):
        super_classes = super_classes + (ToStr,)
        return type.__new__(type_class, class_name, super_classes, class_atr)

class Cat(metaclass=MetaStr):
    def __init__(self, name, age):
        self.name = name
        self.age = age

smt = Cat("Mr.Bigglesworth", 34)