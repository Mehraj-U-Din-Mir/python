# Write a python script to check whether a given year is a leap year or not.
from calendar import isleap
print("Enter the Year")
year=int(input())
if(year %4==0):
    if(year %100==0):
        if(year %400==0):
            print("%d is leap year"%(year))
        else:
            print("%d is common year"%(year))
    else:
        print("%d is leap year"%(year))
else:
    print("%d is not common yaer"%(year))

if((year % 4==0 and year %100==0) or (year%400==0)):
    print("Leap")
print(f'{year} is leap') if isleap(year) else print(f'{year} is common yaer')