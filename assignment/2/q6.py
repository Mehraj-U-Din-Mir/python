"""Write a python script to print all the keywords"""

import keyword
print(" list of keywords are given below", sep='\n')
print(keyword.kwlist)
print("the total keywords are", len(keyword.kwlist))