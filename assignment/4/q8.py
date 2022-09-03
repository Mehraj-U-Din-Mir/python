# Write a python script to calculate simple interest
# A=	final amount
# P	=	initial principal balance
# r	=	annual interest rate
# t	=	time (in years)
p=float(input("Enter the Initial Amount"))
r=float(input("Enter  anual interest rate"))
t=int(input("Enter the time "))
Simple_interest=(p*r*t)/100
total=p+Simple_interest
print("Simple INterest = ",Simple_interest)
print("The Total amount need to pay = ", total)