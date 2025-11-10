"""
project.py , project_management.py
Estimate: 120 minutes
Actual:   180 minutes
"""


class Project:
    """Represents a project with a name, start date, priority, cost, and completion."""

    def __init__(self, name, start_date, priority, cost, completion):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        """Return human-readable string for display."""
        date_str = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {date_str}, priority {self.priority}, "
                f"estimate: ${self.cost:,.2f}, completion: {self.completion}%")

    def is_completed(self):
        """Return True if the project is 100% complete."""
        return self.completion >= 100

    def update(self, completion=None, priority=None):
        """Update completion and/or priority."""
        if completion is not None:
            self.completion = completion
        if priority is not None:
            self.priority = priority

    def __lt__(self, other):
        """Less than operator based on priority."""
        return self.priority < other.priority
