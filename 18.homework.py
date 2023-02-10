'''
Реализуйте генераторную функцию, которая будет возвращать по одному
члену числовой последовательности, закон которой задается с помощью пользовательской функции.
Кроме этого параметром генераторной функции должны быть значение первого
члена прогрессии и количество выдаваемых
членов последовательности (n). Генератор должен остановить свобю работу
или по достижению n - го члена, или при передаче команды на завершение.
'''
def g_progression():
    start = 2
    list = []
    while start <= 100:
        list.append(start)
        start *= 2
    return list

def print_for_step(first_n, size_n):
    i = g_progression().index(first_n)
    while i < len(g_progression()):
        if i >= size_n:
            return
        yield first_n
        i += 1
        first_n = g_progression()[i]
    return

for i in print_for_step(2, 4):
    print(i)
'''
Используя функцию замыкания реализуйте такой прием программирования как Мемоизация.
Используйте полученный механизм для ускорения функции рекурсивного вычисления n - го
члена ряда Фибоначчи. Сравните скорость выполнения с просто рекурсивным подходом.
'''
import time

start_f = time.time()
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

print(f'Рекурсивный подход : Значение = {fib(30)}, время = {time.time() - start_f}.')

start_m = time.time()
_fib_cache = {1: 1, 2: 1}
def mem_fib(n):
    result = _fib_cache.get(n)
    if result is None:
        result = mem_fib(n-2) + mem_fib(n-1)
        _fib_cache[n] = result
    return result


print(f'Используя Мемоизацию : Значение = {mem_fib(150)} время = {time.time() - start_m}')
'''
Напишите функцию, которая применит к списку чисел произвольную пользовательскую фунцкию
и вернет суммы элементов полученного списка.
'''
def g_progression():
    start = 2
    list = []
    while start <= 100:
        list.append(start)
        start *= 2
    return list

def sum_of_progression():
    sum = 0
    for i in g_progression():
        sum += i
    return sum

print(sum_of_progression())