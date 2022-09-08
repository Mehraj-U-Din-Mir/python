# Write a python script to print first N odd natural numbers in reverse order
n= int(input("Enter the number"))
for i in range(n,0,-1):
        print(i*2-1, end=' ')
