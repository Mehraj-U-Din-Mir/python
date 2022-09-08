#Write a python script to print MySirG N times on the screen 
from numpy import ediff1d


name=int(input("Enter how many times  "))
i=1
while(i<=name):
    print(i, "MySirG")
    i=i+1
else:
    print(f" {name} times loop has been exexcited")