# Write a python script to count digits in a given number
num= int(input("Enter the number to find number of digits"))
count=0
i=0
while (num!=0):
    num=int(num/10)
    count+=1
print(count)
# n = int(input("Enter a number : "))
# count = 0
# while(n != 0):
#     n = int(n/10)
#     count = count + 1
# print("Number of digits :",count)