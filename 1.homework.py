'''
number = int(input("Enter number: "))
print("Your number:", number)
print("First:", int(number/10000))
print("Second:", int(number/1000%10))
print("Third:", int(number/100)%10)
print("Fourth:", int(number/10%10))
print("Fifth:", int(number%10))
'''


import cmath
f_side = float(input("First side of trinagle: "))
s_side = float(input("Second side of trinagle: "))
t_side = float(input("Third side of trinagle: "))
p = f_side + s_side + t_side
print("Square of trinagle: ", cmath.sqrt(p*(p-f_side)*(p-s_side)*(p-t_side)))


'''
import cmath
r = float(input("Enter radius: "))
print("Lenght:", cmath.pi*r*2)
'''
