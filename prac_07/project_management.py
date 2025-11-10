from project import Project
from datetime import datetime
import csv

DEFAULT_FILE = "projects.txt"


def load_projects(filename=DEFAULT_FILE):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file, delimiter="\t")
            next(reader)
            for row in reader:
                if len(row) < 5:
                    continue
                name, date_str, priority, cost, completion = row
                start_date = datetime.strptime(date_str, "%d/%m/%Y").date()
                project = Project(name, start_date, int(priority), float(cost), int(completion))
                projects.append(project)
    except FileNotFoundError:
        print(f"{filename} not found. Starting with empty project list.")
    return projects


def save_projects(projects, filename=DEFAULT_FILE):
    """Save list of Project objects to a file."""
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file, delimiter="\t")
        writer.writerow(["Name", "Start Date", "Priority", "Cost", "Completion"])
        for project in projects:
            writer.writerow([
                project.name,
                project.start_date.strftime("%d/%m/%Y"),
                project.priority,
                project.cost,
                project.completion
            ])


def display_projects(projects):
    """Display incomplete and completed projects, sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_completed()])
    completed = sorted([p for p in projects if p.is_completed()])

    print("\nIncomplete projects:")
    for project in incomplete:
        print(f"  {project}")

    print("\nCompleted projects:")
    for project in completed:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Display projects starting after a given date."""
    date_input = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.strptime(date_input, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format")
        return
    filtered = [p for p in projects if p.start_date > filter_date]

    def get_start_date(project):
        return project.start_date

    filtered.sort(key=get_start_date)
    for project in filtered:
        print(project)


def add_new_project(projects):
    """Prompt user to add a new project and append to projects list."""
    print("Let's add a new project")
    name = input("Name: ").strip()
    date_str = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.strptime(date_str, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost, completion))


def update_project(projects):
    """Update completion or priority of a chosen project."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
    except (ValueError, IndexError):
        print("Invalid selection")
        return
    print(project)
    completion_input = input("New Percentage: ")
    priority_input = input("New Priority: ")
    completion = int(completion_input) if completion_input else None
    priority = int(priority_input) if priority_input else None
    project.update(completion, priority)


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILE)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILE}")

    menu = ("- (L)oad projects  \n"
            "- (S)ave projects  \n"
            "- (D)isplay projects  \n"
            "- (F)ilter projects by date\n"
            "- (A)dd new project  \n"
            "- (U)pdate project\n"
            "- (Q)uit")

    while True:
        print(menu)
        choice = input(">>> ").lower()
        if choice == "l":
            filename = input("Filename to load projects from: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "s":
            filename = input("Filename to save projects to: ")
            save_projects(projects, filename)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        elif choice == "q":
            save_choice = input(f"Would you like to save to {DEFAULT_FILE}? (y/n): ").lower()
            if save_choice == "y":
                save_projects(projects, DEFAULT_FILE)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
