# class Employee:
#     company = "ITC"
#     def show(self):
#         print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


# class Programmer(Employee):
#     company = "ITC Infotech"
#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")


# a = Employee()
# b = Programmer()

# print(a.company, b.company)


# class Parent:
#     # Parent class
#     name = "shahzil"
#     a = [1,2,34,56,7,78]
#     def greet(self):
#         print("Hello from the Parent class!")


# class Child(Parent):
#     # Child class inherits from Parent
#     pass


# # Example Usage
# child = Child()
# child.greet()  # Output: Hello from the Parent 
# child.a.append(99)  # Output: Hello from the Parent class!
# print(child.a)  # Output: Hello from the Parent class!


# class Parent:
#     def greet(self):
#         print("Hello from the Parent class!")

# class Child(Parent):
#     def greet(self):
#         super().greet()  # Call the parent class method
#         print("Hello from the Child class!")

# # Example Usage
# child = Child()
# child.greet()
# # Output:
# # Hello from the Parent class!
# # Hello from the Child class!


class User:
    def __init__(self, name):
        self.name = name

    def login(self):
        print(f"{self.name} logged in.")

class Admin(User):
    def manage_users(self):
        print(f"{self.name} is managing users.")

class Guest(User):
    def browse(self):
        print(f"{self.name} is browsing as a guest.")

# Example Usage
admin = Admin("Shahzil")
admin.login()         # Output: Shahzil logged in.
admin.manage_users()  # Output: Shahzil is managing users.

guest = Guest("Ali")
guest.login()         # Output: Ali logged in.
guest.browse()        # Output: Ali is browsing as a guest.
