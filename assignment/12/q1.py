"""Write a python script to reverse a number"""
# num=int(input("Enter the number"))
# rev=str(num)
# rev_num=int(rev[ : : -1])
# print(f' the Reverse of number {num} is ={rev_num}')
# print(type(rev_num))
num = int(input("Enter any number to which you wish to find the reverse"))
rev=0
while(num!=0):
    rem=num%10
    rev=(rev*10)+rem
    num=int(num/10) # or go ;for  floor diveision that is num//10
print(rev)