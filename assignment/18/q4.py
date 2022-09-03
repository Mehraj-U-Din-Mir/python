"""Write a python program to change the value of a specific item by referring to its key
name."""
dir={
    102:"hello",
    104:"pyhton",
    106:" hello java"
}
for num in dir:
    print(num, dir[num])
# dir[104]="Artificial Intelligence"
# print ("the updated dict is = ",dir)
    # now we will change tha value of spacific item by its key

dir[104]="java"
print("THe updated directory is =" )
for  n in dir:
    print(n,dir[n])