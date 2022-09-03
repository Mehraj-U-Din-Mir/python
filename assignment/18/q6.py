"""Write a python program to create a dictionary that contains three dictionaries.
(nested)"""
dir={
    'dir1':{
        102:"java",
        103:"python",
        104:"julia"
    },
    'dir2':{
        105:"r_prog",
        106:"c++"
    },
    'dir3':{
        107:"c_prog",
        108:"Spring"
    },
    1:{
        'name':"mehraj",
        'roll':12
    }
}

#print(dir)
for k in dir:
    print(k,dir[k])

# we need to go for dir 1 then what we have to follow
# access the paticulat dictionay form the given nested dictionary
for ke in dir["dir1"]:
    print(ke,dir["dir1"][ke])

# access the paticulat elemet of sub_dictionary  form the given nested dictionary

print(dir["dir2"][105])