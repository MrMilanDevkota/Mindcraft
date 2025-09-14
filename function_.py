# functions 
'''
user defined function ; built in function 
print , len , range , type .....-> built in function 

'''
def average(a,b,c):
    avg= (a+b+c)/3
    return avg

print(average(5,6,7))



def nprtoicr(a):
    iccr= a * 1.6
    print("The nepalese currency ",a,"is equals to", iccr)
    return 

nprtoicr(10)

def icrtonpr(a):
    npr= a/1.6
    print("The indian currency",a, "is equals to", npr)
    return 

icrtonpr(16)