"""Write a python program to check whether a given string is a multiword string or single
word string using match case statement"""
name=input("Enter te string   ")
match name:
    case name if ' ' not in name :
        print(f' String {name} contins singleword')
    case name if ' ' in name:
        print(f' String {name} contins multiword')
    case _:
        print("Please enter valid arguent")
