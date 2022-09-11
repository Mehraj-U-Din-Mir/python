# Write a python script to calculate sum of digits of a given number
num= int(input("Enter the number to find number of digits"))
sum=0
while (num>0):
    div=num%10
    sum=sum+div
    num=num//10
print(sum)