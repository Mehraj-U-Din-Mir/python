# Write a python script to print first N even natural numbers
num=int(input("enter the number of times  "))
i=1
while(i<=num):
      i=i+1
      if(i%2!=0):
        continue
      print(i,end=' ')