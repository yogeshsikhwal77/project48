# class method,k property setter
class employee:
    a=1

    @classmethod
    def show(cls):
        print(f"the class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e= employee()
e.a = 45

e.name = "yogesh sikhwal"
print(e.fname)
print(e.lname)

e.show()
