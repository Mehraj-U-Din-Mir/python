# Write a python program to create a function that finds a maximum of four numbers.
def max(a,b,c,d):
    if a>b and a>c and a>d:
        return a
    elif b>a and b>c and b>d:
        return b
    elif c>a and c>b and c>d:
        return c
    else:
        return d
print(max(7,9,56,234))