"""Write a python program to create a function to check whether a given number is even
or odd."""

def even_odd():
    num=int(input("Enter the number"))
    if(num%2==0):
        print("The Given number ",num," is even")
    else:
        print("The given number ",num," in not even")
even_odd()
#or
print(" ❤❤❤✔Using single line if else❤❤❤✔")
def E_O(n):
    print(" even" if n%2==0 else "odd")
E_O(9)