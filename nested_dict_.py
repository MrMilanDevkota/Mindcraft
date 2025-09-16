# dictionary nesting:
# we will be doing dictionary inside dictionary
myfamily={
    "siblings":3,
    "child1":{
        "name":"milan",
        "year":2000
    },
    "child2":{
        "name":"swastika",
        "year":2001
    },
    "child3":{
        "name":"dikshya",
        "year":2003
    }   
}
print(myfamily)
print(myfamily["child3"])

# changing the value of nested dictionary
myfamily["child1"]["name"]="Munal"
print(myfamily["child1"])

# adding new item to nested dictionary
myfamily["child3"]["age"]=21
print(myfamily["child3"])

# deleting an item from nested dictionary
myfamily["child2"].pop("year")
print(myfamily["child2"])


