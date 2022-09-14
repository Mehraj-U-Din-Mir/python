# Write a python script to print all Prime numbers under 100\
n=100
for i in range(2,n+1):
    k=0
    for j in range(2,i//2+1):
        if(i%j==0):
            k=k+1
    if(k<=0):
        print(i,end=' ')