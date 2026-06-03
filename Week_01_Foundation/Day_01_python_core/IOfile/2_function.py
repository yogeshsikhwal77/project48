f = open("file.txt")

# lines = f.readlines()
# print(lines,type(lines))  #['Yogesh is a good boy\n', 'I am a second line\n', 'This is amazing\n', 'Twinkle Twinkle little star'] <class 'list'>

# line1 = f.readline()
# print(line1,type(line1)) #Yogesh is a good boy  <class 'str'>

# line2 = f.readline()
# print(line2,type(line2)) #I am a second line  <class 'str'>

# line3 = f.readline()
# print(line3, type(line3)) #This is amazing  <class 'str'>

# line4 = f.readline()
# print(line4, type(line4)) #Twinkle Twinkle little star <class 'str'>

# line5 = f.readline()
# print(line5 =="")

line = f.readline()
while(line != ""):
   print(line)
   line =f.readline()

f.close()

