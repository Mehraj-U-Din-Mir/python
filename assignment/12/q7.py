"""Write a python script to check whether a given pair of numbers are co-Prime
numbers or not."""
num1=int(input("Enter the First number"))
num2=int(input("Enter the Sencond Number"))
hcf=0
for i in range(1,num1+1,1):
    for j in range(1,num2+1,1):
        if num1%i==0 and num2%i==0:
            hcf=i
        
if hcf==1:
    print(f"{num1} and {num2} are co-prime and there hcf = {hcf}")
else:
    print(f"{num1} and {num2} are not co-prime and there hcf = {hcf}")