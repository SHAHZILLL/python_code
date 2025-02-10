class Employee: 
    language = "Python" # This is a class attribute
    payment = 1200000

    def __init__(self, name, payment, language): # dunder method which is automatically called
        self.name = name
        self.payment = payment
        self.language = language
        print("I am creating an object")
 
 
    def getInfo(self):
        print(f"The language is {self.language}. The payment is {self.payment}")

    @staticmethod
    def greet():
        print("Good morning")


harry = Employee("Harry", 1300000, "JavaScript") 
# harry.name = "Harry"
print(harry.name, harry.payment, harry.language)

rohan = Employee()