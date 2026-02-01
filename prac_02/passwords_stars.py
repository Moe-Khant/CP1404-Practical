password = input("Enter password: ")
MINIMUM_LENGTH = 10

while len(password) < MINIMUM_LENGTH:
    print("Password does not meet the requirement.")
    password = input("Enter password: ")

print("*" * len(password))