"""Write a python program to convert two lists into a dictionary in a way that item from
list1 is the key and item from list2 is the value."""
from multiprocessing.sharedctypes import Value


list1=[1,2,3]
list2=["java","python","C/C++"]

dic={}

for list_keys in list1:
    for list2_value in list2:
        dic[list_keys]=list2_value
        list2.remove(list2_value)
        break
    print("the resultant dictionary is =" +str(dic))