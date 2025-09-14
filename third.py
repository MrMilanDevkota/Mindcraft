# # if-else statement
# num = 25
# if num >= 1000:
#     print(" protest successful")
# else:
#     print("protest failed") 

num = int(input("Enter a number: "))
if num % 2 == 0 and num%5 ==0:
    print("The number is divisible by 2 and 5")
elif num % 2 == 0:
    print("The number is divisible by 2")
elif num % 5 == 0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 2 and 5")
 #not equal to !=