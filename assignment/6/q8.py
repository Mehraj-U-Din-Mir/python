"""Write a python script to check whether a given quadratic equation has two real &
 distinct roots, real & equal roots or imaginary roots"""
from math import sqrt

import cmath
print("Enter a,b,c")
a,b,c=int(input()),int(input()),int(input())
discrm=b**2 -4*a*c
if discrm>0:
    print(f'Roots are{(-b +sqrt(discrm))/(2*a)} and {(-b -sqrt(discrm))/(2*a)} real and distinct')
elif discrm==0:
    print(f'Roots are {-b/ (2 * a)} real and equal.')
else:
    print(f'Roots are {(-b +cmath. sqrt(discrm)) / (2 * a)} and {(-b -cmath.sqrt(discrm)) / (2 * a)} complex.')
# from math import sqrt
# import cmath
# print("Enter a, b, and c values of quadratic equation.")
# a, b, c = int(input()), int(input()), int(input())
# discriminant = b ** 2 - 4 * a * c
# if discriminant > 0:
#     print(f'Roots are {(-b + sqrt(discriminant)) / (2 * a)} and {(-b - sqrt(discriminant)) / (2 * a)} real and distinct.')
# elif discriminant == 0:
#     print(f'Roots are {-b/ (2 * a)} real and equal.')
# else:
#     print(f'Roots are {(-b + cmath.sqrt(discriminant)) / (2 * a)} and {(-b -cmath. sqrt(discriminant)) / (2 * a)} complex.')