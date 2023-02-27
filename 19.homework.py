'''
Создайте декоратор, который будет подсчитывать, сколько раз была
вызвана декорируемая функция.
'''
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.num_calls += 1
        return func(*args, **kwargs)
    wrapper.num_calls = 0
    return wrapper

@count_calls
def my_func():
    print("Who are you ???")

my_func()
my_func()
my_func()

print(my_func.num_calls)
'''
Создайте декоратор, который зарегистрирует декорируемую функцию в списке
функций, для обработки последовательности.
'''
registered = []

def register(func):
    registered.append(func)
    return func

@register
def my_func():
    print("first")

@register
def my_second_func():
    print("second")

print(registered)
'''
Предположим, в классе определен метод __str__, который возвращает 
строку на основании класса. Создайте такой декоратор для этого метода,
чтобы полученная строка созранялась в текстовый файл, имя которого
совпадает с именем класса, метод которого вы декорировали.
'''
def save_to_file(func):
    def wrapper(self):
        filename = f"{type(self).__name__}.txt"
        with open(filename, "w") as file:
            string = func(self)
            file.write(string)
        return string
    return wrapper

class Text():

    def __init__(self, first, second):
        self.first = first
        self.second = second

    @save_to_file
    def __str__(self):
        return f"First = {self.first}, second = {self.second}."

t = Text(2, 4)
print(t)
'''
Создайте декоратор с параметрами для проведения хронометрада работы
той или иной функции. Параметрами должны выступать то, сколько раз нужно
запустить декорируемую функцию и в какой файл сохранить результаты
хронометража. Цель - провести хронометраж декорируемой функции.
'''
import time

def chronometer(num_runs, output_file):
    def decorator(func):
        def wrapper(*args, **kwargs):
            avg_time = 0
            with open(output_file, "w") as file:
                for i in range(num_runs):
                    start_time = time.monotonic()
                    result = func(*args, **kwargs)
                    end_time = time.monotonic()
                    run_time = end_time - start_time
                    avg_time += run_time
                    file.write(f"Run {i + 1}: {run_time:.6f}-second\n")
                avg_time /= num_runs
                file.write(f"Average time for {num_runs} runs: {avg_time:.6f} second\n")
                return result
        return wrapper
    return decorator

@chronometer(num_runs=10, output_file="results.txt")
def my_function():
    return "Hellow ???"

my_function()