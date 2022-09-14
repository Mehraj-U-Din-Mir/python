# """Write a python script to print first N n of a Fibonacci series"""
n=int(input("Enter the number up to which you want to print Fib Series   "))
base_num1=0
base_num2=1
if n==0:
    print(f'the series of {n} is {base_num1}')
elif n==1:
    print(f'the series of {n} is {base_num2}')
else:
    print(base_num1, base_num2, end = ' ')
    n -= 2
    while n:
        next_term = base_num2 + base_num1
        print(next_term, end = ' ')
        base_num1 = base_num2
        base_num2 = next_term
        n -= 1

         
# n = int(input('How many n of fibonacci series you want to print: '))
# base_num1 = 0
# base_num2 = 1
# if n < 0:
#     n *= -1
# if n == 0:
#     print('Ok, as wish.')
# elif n == 1:
#     print(base_num1, end = ' ')
# elif n == 2:
#     print(base_num1, base_num2, end = ' ')
# else:
#     print(base_num1, base_num2, end = ' ')
#     n -= 2
#     while n:
#         next_term = base_num2 + base_num1
#         print(next_term, end = ' ')
#         base_num1 = base_num2
#         base_num2 = next_term
#         n -= 1
