"""Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary part"""
from operator import imatmul


print("Enter real and  imaginery part of complex cumber")
comp=complex(float(input()),float(input()))
if(comp.real>comp.imag):
    print("real is big")
else:
    print("imaginery is big")

