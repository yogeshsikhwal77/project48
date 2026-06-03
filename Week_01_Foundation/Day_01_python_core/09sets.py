e = set() # Dont use s = {} as it will create an empty dictionary
s = {1, 5, 32, 54,5, 5, 5,"Yogesh"} 
print(s) #{32, 1, 'Yogesh', 5, 54}
print(s,type(s)) #{32, 1, 'Yogesh', 5, 54} <class 'set'>

s.add(566)
print(s,type(s)) #{32, 1, 'Yogesh', 5, 54, 566} <class 'set'>

s.remove(1)
print(s)  #{32, 5, 54, 'Yogesh', 566}

#Union and intersection of sets
s1 = {1, 45, 6, 78}  
s2 = {7, 8, 1, 78}

print(s1.union(s2))      #{1, 6, 7, 8, 45, 78}
print(s1.intersection(s2)) #{1,78}