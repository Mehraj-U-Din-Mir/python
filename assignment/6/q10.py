"""10. Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same."""
print(" Enter three digits")
a,b,c=int(input()),int(input()),int(input())
if(a>=b and a>c):
    print("%d is greater"%(a))
elif(b>=a and b>=c):
     print("%d is greater"%(b))
else:
     print("%d is greater"%(c))