# Write a python script to print first N even natural numbers in reverse order
num=int(input("Enter the number"))
i=1
while(num>i):
        print(num*2-2,end=' ')
        num=num-1