# f = open("file.txt")

# # lines = f.readlines()
# # print(lines, type(lines))

# # line1 = f.readline()
# # print(line1, type(line1))

# # line2 = f.readline()
# # print(line2, type(line2))

# # line3 = f.readline()
# # print(line3, type(line3))

# # line4 = f.readline()
# # print(line4, type(line4))

# # line5 = f.readline()
# # print(line5 =="")
# line = f.readline()
# while(line != ""):
#     print(line)
#     line = f.readline()

# f.close()

def update_hi_score():
    try:
        # Read the current high score from the file
        with open("Hi-score.txt", "r") as file:
            hi_score = file.read()
        hi_score = int(hi_score) if hi_score.strip() else 0
    except FileNotFoundError:
        # If file doesn't exist, assume the high score is 0
        hi_score = 0

    # Get the current game score from the user
    try:
        current_score = int(input("Enter your score: "))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return

    print(f"Previous high score: {hi_score}")

    # Update the high score if the current score is greater
    if current_score > hi_score:
        print("Congratulations! You've set a new high score!")
        with open("Hi-score.txt", "w") as file:
            file.write(str(current_score))
    else:
        print("Try again to beat the high score!")

# Call the function
update_hi_score()
