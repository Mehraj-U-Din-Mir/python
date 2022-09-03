'''Write a python program to access the items of a dictionary by referring to its key
name.'''
dir={
    'name':"Mehraj",
    'age':24,
    'teacher':"MySirg",

};
print("acess directlly by using keys")
print(dir['name'])
print(dir['age'])
print(" using loop")
for k in dir:
    print(k)

# access the elements for Dict

# print(" *****The Element can be assessed as****")
# print(dir['teacher'])
num=str(input("ENtre the key so that we can show up data \n"))
if num in dir:
    print("the value is = ",dir[num])
else:
    print("data  is not present")
