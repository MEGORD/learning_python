'''
Реализуйте генераторную функцию, которая будет возвращать по одному
члену геометрической прогрессии с указанным множителем.
Генератор должен остановить свою работу или по достижения указанной границы, или при
передаче каманды на завершение.
'''
def g_progression(start, stop, step):
    while start <= stop:
        if start >= 500:
            return
        yield start
        start *= step
    return

for i in g_progression(5, 1000, 2):
    print(i)
'''
Реализуйте свой аналог генераторной функции range().
Да, вы теперь знаете, что это - генератор.
'''
def my_range(start, stop, step):
    while start <= stop:
        yield start
        start += step
    return

for i in my_range(1, 10, 2):
    print(i)
'''
Напишите функцию-генератор, которая будет возвращать простые числа.
Верхняя граница этого диапазона должна быть задана параметром этой функции.
'''
def prime_nunbers(border):
    start = 0
    while start < border:
        start += 1
        if start == 2 or start == 3 or start == 5 or start == 7:
            yield start
        elif start % 2 == 0 or start % 3 == 0 or start % 5 == 0 or start % 7 == 0 or start == 1:
            continue
        else:
            yield start
    return

for i in prime_nunbers(100):
    print(i)
'''
Напишите выражение-генератор для заполнения списка.
Список должен быть заполнен кубами чисел от 2 и до указанной вами величины.
'''
n = (input("Your nunber: "))
o_list = [i**2 for i in range(2, int(n)) if i**2 <= int(n)]

print(o_list)