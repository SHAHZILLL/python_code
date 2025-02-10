# from typing import List, Union, Tuple 

# n : int = 5

# name: str = "Harry"


# def  sum(a: int, b: int) -> int:
#     return a+b

# c : int = 6
# d: str = "SHAHZIL"
# e: int = int(input("Enter any number"))


# def add(a: int, b: int) -> int:
#     return a + b

# result: int = add(6,9)
# print(result)
# print(type(e))
# print(e)


# from typing import List, Dict, Tuple, Set

# my_list: List[int] = [1, 2, 3]  # List of integers
# my_dict: Dict[str, int] = {"a": 1, "b": 2}  # Dictionary with string keys and integer values
# my_tuple: Tuple[int, str, float] = (1, "Hello", 3.14)  # Tuple with specific types
# my_set: Set[str] = {"apple", "banana"}  # Set of strings


# my_dict = {"a": 1, "b": 2, "c": 3,"c": 3}
# print(my_dict)  # Output: {"a": 1, "b": 2, "c": 3}

# my_list.insert(-len(my_list),9)
# my_list.append(9)
# my_list.remove(1)
# print(my_list)
# 


# user_info = {
#     "name": "Shahzil",
#     "age": 25,
#     "city": "Karachi"
# }

# Access values by keys
# print("Name:", user_info["name"])
# print("Age:", user_info["age"])
# print("City:", user_info["city"])

# Update the dictionary
# user_info["age"] = 26
# user_info["country"] = [3,4,6,77,1]

# print(user_info)


# Dictionary with tuple keys
# locations = {
#     (10.5, 20.3): "Point A",
#     (15.2, 25.8): "Point B",
#     "Point B" : (15.7, 25.8)
# }

# print(locations["Point B"])  # Output: Point A

def get_user_info():
    return ("Shahzil", 25, "Karachi",33,55)

name, age, city, *data  = get_user_info()
print(f"Name: {name}, Age: {age}, City: {city}")
print(data)
