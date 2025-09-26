name = input("Enter name: ")
Menu = "(H)ello\n(G)oodbye\n(Q)uit"
print(Menu)
choice = input(">>> ").upper()
while choice != 'Q':
    if choice == 'H':
        print(f"Hello {name}")
    elif choice == 'G':
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(Menu)
    choice = input(">>> ").upper()
print("Finished.")
