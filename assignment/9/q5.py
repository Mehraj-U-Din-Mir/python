# Write a python script to print first N odd natural numbers in reverse order
num=int(input("Enter the number of times  "))
i=1
while(num>=i):
    if(num%2!=0):
        print(num,end= ' ')
    num=num-1

