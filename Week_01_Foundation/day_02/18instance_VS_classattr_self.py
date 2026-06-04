class employee:
    language = "js"
    salary = "1200000"

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

mohit = employee()
mohit.language = "c"  #intence attribute
print(mohit.language,mohit.salary)

mohit.greet()
mohit.getInfo()  #employee.getinfo(mohit)