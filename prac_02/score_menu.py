"""
CP1404/CP5632 - Practical
Score menu program
"""


def main():
    score = get_valid_score()
    display_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_score_status(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")
        display_menu()
        choice = input(">>> ").upper()

    print("Goodbye!")


def display_menu():
    print("(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit")


def get_valid_score():
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        score = float(input("Enter score (0-100): "))
    return score


def determine_score_status(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    print("*" * int(score))


main()
