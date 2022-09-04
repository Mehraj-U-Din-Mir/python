"""Write a python program to create a function to check whether a number falls in a
given range."""

from tabnanny import check


def chk_range(n):
    if n in range(10,100):
        print("number ", n, "is in range")
    else:
        print("number " ,n," is not in range")
chk_range(45)
chk_range(500)