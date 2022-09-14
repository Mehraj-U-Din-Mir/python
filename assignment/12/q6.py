# Write a python script to print first N prime numbers

n=int(input("Enter the number up to which you want to find prime numbers"))

for i in range(2,n*2,1):
    k=0
    for j in range(2, i//2+1):
        if(i%j==0):
            k=k+1
    if(k<=0):
        print(i,end=' ')
        