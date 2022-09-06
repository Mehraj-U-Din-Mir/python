"""Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement"""
str1,str2=input("Enter first string"),input("Enter the Second String")

match(str1,str2):
    case (str1,str2) if str1==str2:
          print(f"strings {str1} and {str2 } are identical")
        
    case (str1,str2) if str1>str2:
          print(f"strings {str2} comes before {str1 } ")
    case (str1,str2) if str1<str2:
          print(f"strings {str1} comes before {str2 } ")
# print('Enter your and friends first names respectively.')
# your_name, friends_name = input().lower().strip(), input().lower().strip()

# match (your_name, friends_name):
#     case (your_name, friends_name) if your_name == friends_name:
#         print(f'{your_name} and {friends_name} are identical.')
#     case (your_name, friends_name) if your_name > friends_name:
#         print(f'{friends_name} comes  before {your_name}.')
#     case (your_name, friends_name) if your_name < friends_name:
#         print(f'{your_name} comes before {friends_name}.')