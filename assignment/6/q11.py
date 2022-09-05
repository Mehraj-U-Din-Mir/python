"""Write a python script to take the month value in numeric format and display the
number of days in it."""
print("Enter the month")
month=int(input())
if(month in (4,6,9,11)):
    print("%d month has 30 days"%(month))
elif(month in (1,3,5,7,8,10,12)):
    print("%d month has 31 days"%(month))
else:
     print("%d month has 29 or 28 days"%(month))