'''Write a python script to print the octal equivalent of a given decimal number. (do not
use oct() method)'''
n= int(input("Enter the Decomal number"))
temp=n
oct=' '
while n:
    oct=oct+str(n%8)
    n=n//8
print(f' the octal of {temp} is ::{oct[: : -1]}')
