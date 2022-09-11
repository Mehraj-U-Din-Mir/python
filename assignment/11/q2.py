# Write a python script to calculate sum of squares of first N natural numbers
num= int(input("Enter the number till you want to calculate Sum of Squares   "))
if num<0:
    print("Enter a valid positive number")
elif num==0:
    print(" You have entered a neutral number")
else:
    sum=0
    while(num>0):
        sum=sum+num**2
        num=num-1
    print(sum)