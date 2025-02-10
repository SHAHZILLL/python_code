class Employee: 
    language = "Py" # This is a class attribute
    payment = 1200000


harry = Employee()
harry.name = "Harry" # This is an instance attribute
print(harry.name, harry.language, harry.payment)

rohan = Employee()
rohan.name = "Rohan Roro Robinson"
print(rohan.name, rohan.payment, rohan.language)

# Here name is instance attribute and payment and language are class attributes as they directly belong to the class