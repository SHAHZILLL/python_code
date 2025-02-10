class Employee: 
    language = "Python" # This is a class attribute
    payment = 1200000


harry = Employee()
harry.language = "JavaScript" # This is an instance attribute
print(harry.language, harry.payment)
 