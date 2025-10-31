"""
programming_language.py
Estimate: 30 minutes
Actual:   50 minutes
"""


class ProgrammingLanguage:
    """Store information about a programming language."""
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a readable string describing the language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
