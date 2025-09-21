# # characters haru herney raicha 
# f = open("demofile.txt")
# print(f.readline())
# f.close()

# with open("demofile.txt") as f:
#   print(f.readline())
#   print(f.readline())

# with open("demofile.txt") as f:
#   for x in f:
#     print(x)

# with open("demofile.txt", "a+") as f:
#   f.write("Now the file has more content!")

#   f.seek(0)
#   print(f.readline())

with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read())