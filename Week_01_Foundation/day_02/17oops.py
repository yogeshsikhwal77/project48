class employee:
    language = "Py"   #class attribute
    salary = 10000000

yogesh = employee()
yogesh.name = "Yogesh"  #instance attribute
print(yogesh.name,yogesh.language,yogesh.salary)

mohan=employee()
mohan.name = "mohan tonny gone"
print(mohan.name,mohan.salary,mohan.language)
# Here name is instance attribute and salary and language are class attributes as they directly belong to the class