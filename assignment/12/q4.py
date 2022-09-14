""" Write a python script to print all Prime numbers between two given numbers (both
values inclusive)"""
begning_num=int(input("Enter the number to which you wish to start from"))
last_num=int(input("Enter the number to which you wish to end for"))
for i in range(begning_num,last_num+1):
    k=0
    for j in range( 2,i//2+1):
        if i%j==0:
            k=k+1
    if(k<=0):
        print(i, end=' ')
