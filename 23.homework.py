'''
Создайте ABC класс, с абстрактным методом проверки целого числа на простоту. Т.е., если
параметром этого метода является целое число и оно простое, то метод должен вернуть
True, а в противном случае False.
'''
import abc

class Checker(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def is_odd(self, n: int) -> bool:
        pass
'''
Создайте класс его наследующий.
'''
class MyChecker(Checker):
    def is_odd(self, n: int) -> bool:
        if n % 2 == 0:
            return False
        else:
            return True
'''
Создайте класс, который не наследует пользовательский ABC класс, но обладает нужным методом.
Зарегистрируйте его в качестве виртуального подкласса.
'''
class CustomChecker:
    def is_odd(self, n: int) -> bool:
        if n % 2 == 0:
            return False
        else:
            return True

Checker.register(CustomChecker)

my_checker = MyChecker()
print(my_checker.is_odd(3))

custom_checker = CustomChecker()
print(custom_checker.is_odd(8))
'''
Проверьте работоспособность проекта.
'''