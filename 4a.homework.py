'''
"Перевернуть матрицу". Т.е. написать программу,
которая повернект базовую матрицу на 90, 180, 270
градусов по часовой стрелке.
'''
arr = list()

for row in range(4):
    temp = list()
    for col in range(1, 5):
        temp.append(col)
    arr.append(temp)
    print(temp)
print('------------------------------------------------------------')
for row in range(4):
    flag = row + 1
    for col in range(1, 5):
        arr[row] = [flag, flag, flag, flag]
    print(arr[row])
print('------------------------------------------------------------')
for row in range(4):
    for col in range(-4, 0):
        arr[col] = -col
    print(arr)
print('------------------------------------------------------------')
for row in range(4):
    flag = 4 - row
    for col in range(1, 5):
        arr[row] = [flag, flag, flag, flag]
    print(arr[row])
'''
Написать код для зеркального переворота списка.
'''
import random

arr = []

for i in range(5):
    arr.append(random.randint(1, 10))
print(arr)
arr.reverse()
print(arr)