# FIRST WAY OF DOING THIS

# class Programmer:
#     company = "Microsoft"
#     def __init__(self, name, salary, pin):
#         self.name = name
#         self.salary = salary
#         self.pin = pin


# p = Programmer("Harry", 1200000, 245001)
# print(p.name, p.salary, p.pin, p.company)
# r = Programmer("Rohan", 1200000, 245001)
# print(r.name, r.salary, r.pin, r.company)


# SECOND WAY OF DOING THIS
class Programmer:
    def __init__(self, name, age, programming_language, years_of_experience, team):
        """
        Initialize the attributes of the Programmer class.
        """
        self.name = name
        self.age = age
        self.programming_language = programming_language
        self.years_of_experience = years_of_experience
        self.team = team

    def display_info(self):
        """
        Display the information of the programmer.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Programming Language: {self.programming_language}")
        print(f"Years of Experience: {self.years_of_experience}")
        print(f"Team: {self.team}")
        print("--------------")

# Example Usage
programmers = [
    Programmer("Alice", 30, "Python", 8, "Azure AI"),
    Programmer("Bob", 28, "JavaScript", 6, "Teams"),
    Programmer("Charlie", 35, "C#", 10, "Windows Development"),
    Programmer("Charlie", 35, "C#", 10, "Windows Development"),
    Programmer("Charlie", 35, "C#", 10, "Windows Development")
]

for programmer in programmers:
    programmer.display_info()


