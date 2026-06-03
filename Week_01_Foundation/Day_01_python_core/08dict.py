d={} # empty dictorineries
marks = {
    "harry": 100,
    "gonju": 10,
    "rohan": 1,
    0: "harry"
}

print(marks["harry"]) #100
print(marks.items())   #dict_items([('harry', 100), ('gonju', 10), ('rohan', 1), (0, 'harry')])
print(marks.keys())    #dict_keys(['harry', 'gonju', 'rohan',0])
print(marks.values())   #dict_values([100, 10, 1, 'harry'])
marks.update({"harry":99,"Monika":100})
print(marks) #{'harry': 99, 'gonju': 10, 'rohan': 1, 0: 'harry', 'Monika': 100}

print(marks.get("Harry2")) #None
print(marks["Harry2"]) #error given