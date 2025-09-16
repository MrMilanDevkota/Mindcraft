# understanding the basic concept of class in python
# class is a blueprint of an object
# creating a class
class Person:
    name="Milan"
    age=23
    country="Nepal"

# creating an object of the class
p1= Person()
print(p1.name)
print(p1.age)
print(p1.country)

# creating another object of the class
p2= Person()
print(p2.name)
print(p2.age)
print(p2.country)

# modifying the object properties
p1.name="Swastika"
p1.age=22
p1.country="India"
print(p1.name)
print(p1.age)
print(p1.country)

print(p2.name)  
print(p2.age)
print(p2.country)

