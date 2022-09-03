"""Write a python program to merge two python dictionaries into one dictionary."""
dic1={
    1:"hello",
    2:"java"
}
dic2={
    3:"hello",
    4:"python"
}
# print(dic1 | dic2)

# or

print({**dic1,**dic2})

# or

dic3=dic1.copy()
dic3.update(dic2)
print (dic3)