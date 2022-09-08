# Write a python script to print first N odd natural numbers
num=int(input("Enter the number of times  "))
i=1
while i<=num:
    if(i%2!=0):
        print(i,end=' ')
    i=i+1