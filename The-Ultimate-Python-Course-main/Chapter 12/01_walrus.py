# # Using walrus operator 
# if (n := len([1, 2, 3, 4, 5])) > 3: 
#     print(f"List is too long ({n} elements, expected <= 3)") # Output: List is too long (5 elements, expected <= 3)

# foodList = list()
# while food := input("Enter food u like!: ") != "quit":
#     foodList.append(food)
#     print(foodList)
    
# print('foodList',foodList)


# foodList = list()
# while (food := input("Enter food u like!: ")) != "quit":  # Parentheses around the walrus expression
#     foodList.append(food)
#     print("You entered:", food)
#     print("Current foodList:", foodList)

# print("Final foodList:", foodList)


foodList = list()
while (food := input("Enter food you like (press Enter to stop): ")) != "":  # Stop if input is empty
    foodList.append(food)
    print("You entered:", food)
    print("Current foodList:", foodList)

print("Final foodList:", foodList)
