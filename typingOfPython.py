# # list: A list is an ordered collection of elements. Each element is accessed using its index (a number).
# my_list = [10, 20, 30, 40]
# print(my_list[1])  # Output: 20

# # list: You access elements by their position (index).
# my_list = ["a", "b", "c"]
# print(my_list[0])  # Output: "a"

# my_list = [1, 2, 3]
# print(my_list)  # Output: [1, 2, 3]

# my_list = [1, 2, 2, 3] #list: Allows duplicate values.

# # Example: Managing a Shopping Cart
# # In an online store, we might use a list to store the items a user has added to their shopping cart.

# # List representing the shopping cart
# shopping_cart = ["apple", "banana", "orange"]

# # Add an item to the cart
# shopping_cart.append("grape")
# print("Updated Cart:", shopping_cart)

# # Remove an item from the cart
# shopping_cart.remove("banana")
# print("Cart after removing banana:", shopping_cart)

# # Check if an item is in the cart
# if "apple" in shopping_cart:
#     print("Apple is in the cart!")

# # Loop through the items in the cart
# print("Items in your cart:")
# for item in shopping_cart:
#     print("- " + item)

# # Access the second item in the cart
# second_item = shopping_cart[1]
# print("The second item in your cart is:", second_item)


# # list:
# # Useful for storing ordered data.
# # Suitable for sequential tasks like iterating over elements.
# # Example: A list of items in a shopping cart

# # dict:
# # Useful for representing relationships or mappings.
# # Example: A dictionary for storing user information (name: Shahzil, age: 25).

# # list:
# # Searching for an element takes O(n) (linear search).
# # dict:
# # Searching for a key takes O(1) (hash table lookup).

# # Summary Table
# # Feature	  List	   Dictionary
# # Structure   Ordered  collection	    Unordered key-value pairs
# # Access	  By index (e.g., list[0])	By key (e.g., dict["key"])
# # Duplicates  Allows   duplicates	    Keys must be unique
# # Performance Slower   search (O(n))	Faster search (O(1))


# # dict: A dictionary is an unordered collection of key-value pairs. Each value is accessed using its key (not an index).
# my_dict = {"name": "Shahzil", "age": 25}
# print(my_dict["name"])  # Output: Shahzil

# # dict: You access elements by their keys (not position).
# my_dict = {"a": 1, "b": 2, "c": 3}
# print(my_dict["a"])  # Output: 1

# my_dict = {"a": 1, "b": 2, "c": 3}
# print(my_dict)  # Output: {"a": 1, "b": 2, "c": 3}

# # dict: Keys must be unique, but values can be duplicated.
# my_dict = {"a": 1, "b": 2, "c": 1}  # Key "a" and "c" have the same value

'''
   not right code
'''
# n = int(input("enter num: "))
# for i in range(n):
#     print(1 + i)
'''
   this right code
'''
# for i in range(1, n + 1):
#     print(i, end="")

n = int(input("num: "))
arr = map(int, input("44").split())
print(n)
print(arr)