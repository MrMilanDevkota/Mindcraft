# concept of dicttionary 
# dictionary doesnot allow duplicate items 


brandbuilder={
    "key":"value",
    "nabina":"faciliator",
    "milan":"tutor",
    "swastika":"student",
    "dikshya": "student"
}

car={
    "color":"red",
    "company":"honda",
    "model":2019
}

print(type(car))
print(len(car))
print(car)

print(car.get("model"))

print(brandbuilder.get("swastika"))
print(car["company"])
print(brandbuilder["nabina"])

print(car.keys()) # to print the keys 
print(brandbuilder.keys())

print(brandbuilder.values()) # to print the values 

print(car.items())

car.update({'price':200000, 'location':'Pokhara'})
print(car)

car["model"]=  2020  # individual values lai change garauna ko lagi 
print(car)

brain={}  # empty dictionary

brain.update({"milan":"bro"})
print(brain)

# to delete an item
car.pop("location")
print(car)

# to delete entire dictionary
brain.clear()
print(brain)

# to delete last item
car.popitem()
print(car)