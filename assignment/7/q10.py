"""Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday"""
print("""a. Yellow - Monday
         b. Blue - Tuesday
         c. Orange - Wednesday
         d. White - Thursday
         e. Black - Friday
         f. Red - Saturday
         g. All other colours - Sunday""")

color=input("Enter the color   ").lower()
match color:
    case color if  color=='i like yellow color' or color =="yellow":
        print("monday")
    case color if  color=='i like blue color' or color =="blue":
        print("Tuesday")
    case color if  color=='i like orange color' or color =="orange":
        print("Wednesday") 
    case color if  color=='i like ohite color' or color =="white":
        print("Thursday")  
    case color if  color=='i like black color' or color =="black":
        print("Friday")
    case color if  color=='i like red color' or color =="red":
        print("Saturday")
    case _:
        print("sunday")