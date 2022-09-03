"""Write a python program to get the key of lowest value from the dictionary.
sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
}"""

sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
}
print("print the minimun value present in dictionary")
num=min(sample_dict,key=sample_dict.get)
print(num)

print("***print the minimun key present in dictionary***")
print(min(sample_dict))