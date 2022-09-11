# Write a python script to calculate sum of first N odd natural numbers
num= int(input("Enter the number till you want to sum up odd numbers  "))
if num<0:
    print("Enter a valid positive number")
elif num==0:
    print(" You have entered a neutral number")
else:
   sum=0
   for i in range(1,num*2):
       if i%2!=0:
           sum=sum+i
   print(f' the Sum of first {num} odd numbers is ={sum}')