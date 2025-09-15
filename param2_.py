'''
Ask 2 numbers from user. 
Calculate total of 2 numbers.
Print the sum is odd or even 
'''

# def addition():
#     num1= int(input("Enter num1: "))
#     num2= int (input("Enter num2: "))
#     sum=num1+num2
#     return sum

def addition(n1,n2):
    sum= n1+n2
    return sum

def check(num):
    if num %2 ==0:
        print("Even")
    else:
        print("Odd")


num1= int(input("Enter num1: "))
num2= int (input("Enter num2: "))
s=addition(num1,num2)
check(s)
