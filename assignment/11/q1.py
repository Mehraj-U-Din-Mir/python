# Write a python script to calculate sum of first N natural numbers
num= int (input ("Enter the numer upto which you want to print the sum   "))
if num<0:
    print(" Enter a valid positive number")
elif num==0:
    print(" You have enter a neutral number")
else:
    sum=0
    while(num>0):
        sum=sum+num
        # sum= num*(num+1)/2
        num-=1
    print(sum)
