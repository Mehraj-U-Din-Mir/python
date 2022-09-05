# #Write a python script to print greater between two numbers. Print number only once even if the numbers are the same.
print("Enter two numbers")
num1, num2=int(input()), int(input())
print("%d is greater "%(num1)) if num1>=num2 else print("%d is greater"%(num2))

#or
print(f'the max in given numbers {num1} and {num2}, {max(num1,num2)} is greater')

#or
if(num1>num2):
    print(" %d is graeter "%(num1))
else:
    print("%d is greater"%(num2))