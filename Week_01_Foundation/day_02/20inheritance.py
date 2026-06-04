class employee:
    company = "best"
    def show(self):
        print(f"The name of employee is {self.name} and salary is {self.salary}")

# class programmer:
#     company = "Best pvt"
#     def show(self):
#          print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#          print(f"The name is {self.name} and he is good with {self.language} language")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")
     
# class programmer(employee):
#     company = "Best pvt"
#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")

# multiple inheritance 
class programmer(employee,Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")


a = employee()
b= programmer()
b.name = "yogesh"
b.salary = 12

b.show()
b.printLanguages()
b.showLanguage()



