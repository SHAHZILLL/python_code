class Employee: 
    language = "Python" # This is a class attribute
    payment = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The payment is {self.payment}")

    @staticmethod
    def greet():
        print("Good morning")


harry = Employee()
# harry.language = "JavaScript" # This is an instance attribute
harry.greet()
harry.getInfo() 
# Employee.getInfo(harry)
 