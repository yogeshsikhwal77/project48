name = "yogesh"

nameshort = name[0:3] # start from index 0 all the way till 3 (excluding 3)
print(nameshort) 
c1 = name[3]
print(c1)
# in back we start from -1
print(name[-5: -1])
print(name[1:4])
print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])
print(name[1:5])

# skip value slicing
word = "amazing"
word[1:6:2] # "mzn" means skipping 2 btw 1 and 6