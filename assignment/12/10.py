"""Write a python script to calculate HCF of two numbers"""
first=int(input("Enter your first number  "))
second=int(input("Enter your second number  "))
if first> second:
    first,second=second,first
for i in range(1,first+1):
    for j in range(1,second+1):
        if first %i==0 and second%i==0:
            hcf=i
print(f' hcf of {first} and {second} is {hcf}')