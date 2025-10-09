"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subjects = load_subject_data(FILENAME)
    display_subject_details(subjects)


def load_subject_data(filename=FILENAME):
    subjects = []
    with open(filename) as in_file:
        for line in in_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            subjects.append(parts)
    return subjects


def display_subject_details(subjects):
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:3} students")


main()
