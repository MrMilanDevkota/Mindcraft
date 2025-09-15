# understanding __init__ method in python class
class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

# creating an object of the class
p1 = Person("Milan", 23, "Nepal")
print(p1.name)



class Dog:

    def __init__ (self, name, age, country):
        self.name=name
        self.age= age
        self.country=country

d1=Dog("Tyson",5,"Nepal")
print(d1.name)

d1.name="Kale"
print(d1.name)
    
class Cat:
    def __init__ (self, name, breed , color):
        self.name=name
        self.breed=breed
        self.color=color

c1=Cat("biralo","local","red")
print(c1.color)

print(c1)