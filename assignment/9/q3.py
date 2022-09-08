# Write a python script to print first N natural numbers in reverse order
num= int(input("Enter the number of times"))
i=1
while(num>=i):
    print(num,end=',')
    num=num-1
