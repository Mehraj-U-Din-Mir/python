#Write a python script which takes a three digit number from the user and displays only its middle digit.
num=int(input("Enter the three digit number"))
num1=num//10
num2=num1%10
print(num2)