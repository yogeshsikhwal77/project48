try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except ValueError as v:
    ValueError("gunda")
    print("hey")
    print(v)

except Exception as e:
    print(e)

print("thank you")