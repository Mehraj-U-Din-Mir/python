# Write a python script to calculate factorial of a given number
num= int(input("Enter the number till you want to find the Factorial"))
fact=1
for i in range(num,0,-1):
    fact=fact*i
print (f' the factorial of {num} is  ::  {fact}')