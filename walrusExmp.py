# The walrus operator (:=) is a new feature introduced in Python 3.8. It allows you to assign a value to a variable as part of an expression. This operator is also called the assignment expression operator.

# Why is it called a "Walrus"?
# It looks like the eyes and tusks of a walrus: := 🦭

# What Does the Walrus Operator Do?
# It helps to:

# Assign a value to a variable.
# Use the value of the variable in the same expression.
# This can make your code more concise and avoid repetitive calculations.

# Syntax
# variable := expression


# Examples of Walrus Operator
# 1. Simplifying Loops
# Without the walrus operator:


# NORMAL CODE WITHOUT WALRUS OPERATOR
# data = input("Enter something: ")
# while data != "quit":
#     print(f"You entered: {data}")
#     data = input("Enter something: ")

# # With the walrus operator:
# while (data := input("Enter something: ")) != "quit":
#     print(f"You entered: {data}")

# NORMAL CODE WITHOUT WALRUS OPERATOR
# my_list = [1, 2, 2, 3, 4]
# value = len(my_list)
# if value > 5:
#     print(f"The list is too long ({value} elements).")
# else :
#     print('error')

# With the walrus operator:
# if (value := len(my_list)) > 5:
#     print(f"The list is too long ({value} elements).")
# else:
#     print('not too long')


# Why is it better?

# It avoids repeating input() in the loop.
# The code is cleaner and more concise.


# num : int = 6
# number = 7


# class Employee:
#     company = "TechCorp"  # Class attribute

#     def __init__(self, name, age):
#         self.name = name  # Instance attribute
#         self.age = age    # Instance attribute

#     @classmethod
#     def company_info(cls):
#         print(f"Company Name: {cls.company}")
        
# # Calling class method directly from the class
# Employee.company_info()  # Output: Company Name: TechCorp

# # Creating an instance and calling the class method from the instance
# employee = Employee("John", 30)
# employee.company_info()  # Output: Company Name: TechCorp


# class Dog:
#     def __init__(self, name, breed):
#         self.nameee = name  # Instance attribute
#         self.breed = breed  # Instance attribute

#     def bark(self):
#         print(f"{self.nameee} is barking! {self.breed}")

# dog = Dog("Buddy", "Labrador")
# dog.bark()  # Output: Buddy is barking!


class Car:
    total_cars = 0  # Class attribute

    def __init__(self, model):
        self.model = model
        Car.total_cars += 1

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars

car1 = Car("Toyota","2002")
# car2 = Car("Honda")
print(Car.get_total_cars())  # Output: 2  
