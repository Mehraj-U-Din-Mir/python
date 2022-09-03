# d1={
#     102:"mehraj",
#     103:"mohsin",
#     104:"faisal",
#     105:"ubaid" 
# }
# #print(d1)
#                                     ##accessing elements
# #print(d1[102])

#                                 ## Uing for loop
# # for k in d1:
# #     print(d1[k])   # it will gicve us only the value of dict elements

# # for k in d1:
# #     print(k,d1[k])

#                     # change the name of ubad to mohsin2
# # d1[105]='mohsin2'
# # for k in d1:
# #     print(d1[k])

#                                         #Delete a data of element
# # del d1[105]
# # print (d1)
#                             #add element to dictionary

# # d1[101]='faizan'
# # print(d1)
# # d1.pop(101)
# # print(d1)

#                         # some dictionary methods
#                         # items()
# # print(d1.items())
# # print(type(d1.items()))
# # for k in d1.items():
# #     print(k)
# #                         #unpack it form touple
# # print(" now time to unpack above given touples into the key pair value")
# # for k,v in d1.items():
# #     print(k,v)

# #                         #keys
# print(" Here we will get al the used keys  of dict")

# # print(d1.keys())
# # print(type (d1.keys()))
# # d1.clear()
# # # print(d1)

# # for v in d1.keys():
# #     print(d1[v])
#             # dict comprehention
# # d2={e:e**2 for e in range(1:7)}
# # print(d2)
# myDict = {x: x**2 for x in [1,2,3,4,5]}
# print (myDict)

                                            # take dict from user
# n=int(input(" Enter the number of elements you want to enter"))
# d1={}
# for e in range(n):
#     key=int(input(" ENtre the keys"))
#     data=input("ENter the values")
#     d1[key]=data
#     print(d1)
num=int(input("enter the number of elements "))
dir={}
for e in range(num):
    k=input("enter the key")
    v=input("Enter the value")
    dir[k]=v
for ke in dir:
    print (ke,dir[ke])
# # access the elements 
# # print(dir["dir1"][102])
# """******access the elements of Dir1******"""
# print("access the elements of Dir1")
# for  k in dir["dir1"]:
#     print(k,dir["dir1"][k])
# """*** ACcess the elements of dictionay 1***"""
# print("** ACcess the elements of dictionay 1***")
# for k1 in dir[1]:
#     print(k1,dir[1][k1])

# """ acces the keys of dir2"""
# print("acces the keys of dir2")
# for kdir2 in dir["dir2"]:
#     print(kdir2)
#     print(dir["dir2"][kdir2])

# """ how to add elements inside the nested dictionary"""
# print("add elements inside the nested dictionary")
# dir["dir4"]={}
# dir["dir4"]['name']="Mehraj"
# dir["dir4"]['roll']=12
# dir["dir4"]['age']=24
# # print(dir["dir4"])
# for kdir4 in dir["dir4"]:
#     print(kdir4,dir["dir4"][kdir4])

# """ how ton add dictionary to dir"""
# print("how ton add dictionary to dir")
# dir["dir5"]={1:"abc",2:"def",3:"ghi"}
# # print(dir["dir5"])
# for kdir5 in dir["dir5"]:
#     print (kdir5,dir["dir5"][kdir5])
# # practice

# print(" the accessed elemet =",dir["dir3"][107])

# """delete form dictionary"""
# # print(" delete the elemnet for the given dictionaey==")
# # del dir["dir5"][1]
# # print(dir["dir5"])
# # del dir["dir1"][104]
# # del dir["dir1"][103]
# # print(dir["dir1"])

# ''' delete dictionay'''
# print(" delete any dictionary")
# del dir["dir1"]
# print(dir)

# """ iterate full dictionary"""
# print("iterate full dictionary")
# # for k,v in dir.items():
# #     print(" id is",k)
# # for key in v:
# #     print(key + ':',v[key])

# """ apna tareeqa"""
# for keee ,val in  dir.items():
#     print("\n person id",keee)
# for key in val:
#     print(key + ':',val[key])