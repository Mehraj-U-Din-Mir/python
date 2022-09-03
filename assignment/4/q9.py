# Write a python script to calculate the volume of a cuboid.
from cmath import sqrt
import math
from os import sep
l=float(input("ENter the length of cuboid "))
b=float(input("Enter the breadth of cuboid "))
h=float(input("Enter the height of cubid "))

vol_cuboid=l*b*h
print("the volume of cuboid = ", vol_cuboid,"units^3",sep=' ')