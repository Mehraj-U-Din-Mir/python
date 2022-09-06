# Write a python script to display the number of days in a given month number.
month=int(input("Enter the month number"))
# match month:
#     case 1 |3 | 5  | 7 | 8 | 10 | 12  :
#         print("there are 31 days")
#     case 2:
#         print("There can b 29 or 28 days")
#     case 4 | 6|9|11:
#         print("there are 30 days in month")
#     case _:
#         print("Enter a valid month")
match month:
    case month if month in (1,3,5,7,8,10,12):
        print(f' MOnth {month} has  31 days')
    case month if month in(4,6,9,11):
        print(f' MOnth {month} has  30 days')
    case month  if month==2:
        print(f' MOnth {month} has  28 or 39 days days')
