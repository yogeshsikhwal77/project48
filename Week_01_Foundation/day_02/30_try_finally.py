def main():
    try:
        a= int(input("hey,enter a number: "))
        print(a)
        return
    
    except Exception as e:
        print(e)
        return
    
    finally:
        print("hey I am inside of finally") # if function return still finally code run 

main()