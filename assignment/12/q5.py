# Write a python script to find next prime number of a given number


import math


num=int(input("Enter the number"))
temp=num
if num<2:
    print(f"next prime number of {num} is :{2} ")
if num % 2 == 0:
        num += 1
        for d in range(3, math.floor(math.sqrt(num)) + 1, 2): 
            if num % d == 0: 
                break
        else: 
            print(f'The next prime after {temp} is {num}')

if num>3:
    while True:
        num+=2
        for d in  range(3, math.floor(math.sqrt(num))+1,2):
            if num%d == 0:
             break
        else:
            print(f"Next prime number after {temp} is {num}")
            break


