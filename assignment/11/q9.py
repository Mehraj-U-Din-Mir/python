""" Write a python script to print binary equivalent of a given decimal number. (do not
use bin() method)"""
# num= int(input("Enter the number to find bnary of entered number"))

n = int(input('Enter a number, to get binary equivalent: '))
for i in range(n-1, -1,-1):
    k=n>>i
    if k & i:
        print ('1', end=' ')
    else:
        print('0', end=' ')
        i-=1
# bits = int(input('How many bits you need to represent a binary number: ')) - 1

# #using bitwise operators
# while bits != -1:
#     binary = num >> bits
#     if binary & 1: print('1', end = '')
#     else: print('0', end='')
#     bits -= 1


# #using arithmetic operators
# print()
# while num: print(num % 2, end = ''); num //= 2