# def goodday(name, ending):
#     print("Good Day, " + name)
#     print(ending)
#     return "ok"

# a = goodday("Harry","Thank You")
# print(a)

#default arguments

def goodday(name, ending="Thank you"):   #ending is by default is thank you
    # print("Good Day, " + name)
    print(f"Good Day, {name}")
    print(ending) 

a = goodday("Harry","Thanks")#Good Day, Harry  Thanks

b = goodday("Harry")       #Good Day, Harry      Thank you

print("Rohan")

