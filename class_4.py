class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def printfunc(self):
        print("Hello my name is ", self.name)
        print(f"My age is {self.age}")

p1=Person("Milan", 22)

p1.printfunc()

p2=Person("Dikshya", 18)
p2.printfunc()

p3=Person('Swastika', 22)
p3.printfunc()

p3.name='dikshya1'
p3.printfunc()

del p3.name
del p3

p3.printfunc()