"""Write a python program to check whether a given number is positive, negative or
zero using match case statement"""
num=int(input("Enter the number"))
match num:
    case num if num>0:
        print("positive")
    case num if num<0:
        print("negative")
    case num if num==0:
        print("Zero  and is neutral")