MINIMUM_LENGTH = 6


def main():
    password = get_password()
    print_stars(password)


def get_password():
    password = input("Password: ")

    while len(password) < MINIMUM_LENGTH:
        print("Password too short! Must be at least", MINIMUM_LENGTH, "characters.")
        password = input("Password: ")
    return password


def print_stars(password):
    print("*" * len(password))


main()
