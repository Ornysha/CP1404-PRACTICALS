
import csv
from guitar import Guitar

FILENAME = "guitars.csv"


def load_guitars(filename):
    """Load guitars from CSV file and return a list of Guitar objects."""
    guitars = []
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 3:
                    continue
                name, year, cost = row
                guitars.append(Guitar(name.strip(), int(year), float(cost)))
    except FileNotFoundError:
        print(f"{filename} not found. Starting with empty list.")
    return guitars


def save_guitars(filename, guitars):
    """Save list of Guitar objects back to CSV."""
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


def display_guitars(guitars):
    """Display all guitars."""
    for guitar in guitars:
        vintage = " (Vintage)" if guitar.is_vintage() else ""
        print(f"{guitar}{vintage}")


def add_new_guitar():
    """Ask user to input a new guitar and return a Guitar object."""
    name = input("Guitar Name: ").strip()
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    return Guitar(name, year, cost)


def main():
    guitars = load_guitars(FILENAME)

    print("All guitars loaded from file:")
    display_guitars(guitars)

    print("Sorted guitars (oldest to newest):")
    guitars.sort()
    display_guitars(guitars)

    while True:
        choice = input("Add a new guitar? (y/n): ").lower()
        if choice != "y":
            break
        new_guitar = add_new_guitar()
        guitars.append(new_guitar)

    print("All guitars after adding new ones:")
    display_guitars(guitars)

    save_guitars(FILENAME, guitars)
    print(f"All guitars saved to {FILENAME}.")


if __name__ == "__main__":
    main()
