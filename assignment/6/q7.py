#Write a python script to check whether a given number is positive, negative or zero.
print("Enter the number for testing of +ve , -ve, 0")
num=int(input())
#print(" %d is positive"%(num)) if(num>0) else print("%d is negative "%(num))
if num>0:
    print("%d is positive "%(num))
elif num<0:
    print("%d is negative "%(num))
else:
    print("%d is zero"%(num)," As zero ins neutral")