#Write a python script to check whether a given number is a three digit number or not.
print("Enter any digit number")
num=int(input())
print("%d is three digit number"%(num)) if (num<=999 and num>=100) else print("%d is other then three digit"%(num))
