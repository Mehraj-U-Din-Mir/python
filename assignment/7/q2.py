"""Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division"""
def Calculator():
    a,b=int(input("Enter first numbers  ")), int(input("Enter 2nd numbers  "))
    print("Which operation you want to perform")
    choice=input("\na or A=  addtion \ns or S = Subtraction  \nm or M = Multiplication  \nd or D = Division")
    match choice:
        case 'a' | 'A':
            print(f'sum of {a},{b} = { a+b}')
        case 's'| 'S':
           print(f'sum of {a},{b} is { a-b}')
        case 'm'|'M':
            print(f'sum of {a},{b} is { a*b}')
        case 'd'|'D':
            print(f'sum of {a},{b} is { a/b}')
        case _:
            print(" this in not in above operator cataagory")
Calculator()
while True:
    print("hyy do you want more y/n")
    res=input()
    if res=='y':
        Calculator()
    else:
        print("We end our Menu here")
    
