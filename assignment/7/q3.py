"""Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit."""
 
choice=input("\ni=isosoless traingle \n2=right angled traingle \n3=equiletral traingle \n4 exit")
match choice:
    case '1':
        side_one,side_two,side_three=int(input(" enter side one  ")), int(input("Enter 2nd side  ")),int(input("Enter third side"))
        if side_one==side_two or side_two==side_three or side_three==side_one :
            print(f" traingle having side one {side_one}, side two {side_two},side three {side_three} is an isolless triangle")
        else:
            print(" not an isosless triangle may be what you are finding is in 2nd case")
    case '2':
        base,hyp,alt=int(input(" enter side one  ")), int(input("Enter 2nd side  ")),int(input("Enter third side"))
        if hyp **2==base**2 +alt**2:
            print( print(f" traingle having side one {base}, side two {hyp},side three {alt} is an right angled triangele traingle triangle"))
        else:
            print("not a right angled triangle go for 1 or 3 case")
    case '3':
        side_one,side_two,side_three=int(input(" enter side one  ")), int(input("Enter 2nd side  ")),int(input("Enter third side"))
        if side_one==side_two==side_three:
            print(f" traingle having side one {side_one}, side two {side_two},side three {side_three} is an equiletral traingle triangle")
        else:
            print(" not an equiletral triangle May be your anser in in 1 or 2")
    case '4':
        print("Exit")
    case _:
        print("This case is not present ")