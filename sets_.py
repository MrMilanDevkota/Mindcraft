# sets

set1= {1,2,3,4,5}
print(type(set1))
print(len(set1))

set1.add(6)
print(set1)

set1.remove(3)
print(set1)

set1.discard(4)
print(set1)

set1.pop()
print(set1)

# set1.clear()
# print(set1)

set2={1,2,3,4,5,5,5,5}
print(set2)  # it will not print duplicate values

set3=set1.union(set2)
print(set3)

set4=set1.intersection(set2)
print(set4)

set5={3,1,2,0,7,5}
print(set5)   # it will print in sorted order
set5.update([8,9,10])
print(set5)