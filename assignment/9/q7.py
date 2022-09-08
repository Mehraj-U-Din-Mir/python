# Write a python script to print first N even natural numbers in reverse order
num=int(input("Enter the number"))
i=1
while(num>i):
    if num%2==0:
        print(num,end=' ')
    num=num-1