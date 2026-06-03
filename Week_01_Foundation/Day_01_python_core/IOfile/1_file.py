f = open("file.txt","r") #open file for reading
data = f.read()
print(data)
f.close()

st = "Hey Yogesh you are amazing"

f = open("myfile.txt","w") # file writing in myfile.txt
f.write(st)
f.close()
