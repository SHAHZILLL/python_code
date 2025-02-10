# def main():
#     try:
#         a = int(input("Hey, Enter a number: "))
#         print(a)
#         return

        
#     except Exception as e:
#         print(e) 
#         return

#     print("Hey I am inside of finally")

#     # finally:


# main()

# try:
#     result = int(input('Entter number: '))
# except Exception as e:
#    print(f"An error occurred: {e}")
# else:
#     print(f"Result is {result * 5}")
# finally:
#     print(f"always run") 

# try:
#     file = open("example.txt", "r")
#     data = file.read()
# except FileNotFoundError:
#     print("File not found!")
# finally:
#     print("Closing the file...")
#     # file.close()c
    

# def divide(a, b):
#     if b == 0:
#         raise ZeroDivisionError("Division by zero is not allowed!")
#     return a / b

# try:
#     a = int(input('enter a number: '))
#     b = int(input('enter a number: '))
#     print(divide(a, b))
# except ZeroDivisionError as e:
#     print(e)


# def process_file(filename):
#     try:
#         with open(filename, "r") as file:
#             data = file.read()
#     except FileNotFoundError:
#         print("File not found!")
#     except PermissionError:
#         print("Permission denied!")
#     else:
#         print(f"File content: {data}")
#     finally:
#         print("Finished processing the file.")

# process_file("example.txt")


