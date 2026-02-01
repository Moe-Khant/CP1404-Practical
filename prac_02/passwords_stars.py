def main():
    password = get_password()
    minimum_length = 10

    while len(password) < minimum_length:
        print("Password does not meet the requirement.")
        password = get_password()

    print("*" * len(password))


def get_password() -> str:
    password = input("Enter password: ")
    return password


main()