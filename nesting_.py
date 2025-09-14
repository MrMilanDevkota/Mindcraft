# nesting
age= int(input("enter your age: "))
if age>=18:
    if age<60:
        print("you can drive")
    else:
        print("you are too old to drive")
else:
    print("you are not eligible to drive")
    