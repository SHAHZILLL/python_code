class Employee:
    def __inittt__(self):
        print("Constructor of Employeeeee")

    def __init__(self):
        print("Constructor of Employee")
    a = 1


class Programmer:
    def __init__(self):
        super().__init__()

        print("Constructor of Programmer")
    b = 2


class Manager(Programmer, Employee):  # Order of inheritance matters here
    def __init__(self):
        super().__init__()  # This will follow the MRO and call the Programmer's __init__
        super().__inittt__()
        print("Constructor of Manager")
    c = 3


# Create a Manager object
o = Manager()

# Accessing attributes
print(o.a)  # This will print '1' because 'a' is defined in Employee
