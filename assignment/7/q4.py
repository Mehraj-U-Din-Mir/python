"""Write a program which takes user’s age and display the category of person. Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen."""
# choice =input("""1=Age below 10 years- Kid, 
#                  2=Age below 20 - Teen, 
#                  3=Age below 40 - young,
#                  4=Age below 60 -Experienced,
#                  5=Age above or equal 60 - Senior Citizen""")
age=int(input("Enter the age of a person"))
# if age<10:
#     print("kId")
# elif(age>10 and age<20):
#     print("Teen")
# elif(age>20 and age<40):
#     print("young")
# elif(age>40 and age<60):
#     print("Exerienced")
# else:
#     print("Senior citizen")
match age:
    case age if age<10:
        print("Kid")
    case age if age>10 and age<20:
        if age> 10 and age<20:
            print("Teen")
    case  age  if age>20 and age<40:
       print("young")
        
    case age if age>40 and age<60:
         print("Experiemced")
       
    case age  if age>=60:
        if age>=60:
            print("Senior Citizen")
    case _:
        print("NOTA")
