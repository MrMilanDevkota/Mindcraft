def greet():
    # scoping 
    name= input("Enter your name: ")
    print(f"Your name is {name}")

name= 'xyz'
greet() # yeha name name ko variable vaye ni yo xyz sanga differ garcha
print(name)

