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
n=int(input(" Enter the number of elements you want to enter"))
d1={}
for e in range(n):
    key=int(input(" ENtre the keys"))
    data=input("ENter the values")
    d1[key]=data
    print(d1)