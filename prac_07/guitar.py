CURRENT_YEAR = 2025


class Guitar:
    """Store info about a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Set name, year, and cost of the guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Show guitar info as a string."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the guitar """
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 years or older"""
        return self.get_age() >= 50
    def __lt__(self, other):
        """Allow sorting guitars by year."""
        return self.year < other.year

