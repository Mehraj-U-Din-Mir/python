# Write a python script to calculate sum of first N even natural numbers
num= int(input("Enter the number till you want to sum of """"Even""" "numbers numbers  "))
sum=0
for i in range(2, num*2+2,2):
    sum=sum+i
print(f"Sum of even numbers upto {num}  is : {sum}")