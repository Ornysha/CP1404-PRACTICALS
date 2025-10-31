"""
languages.py
Estimate: 30 minutes
Actual:   20 minutes
"""

from programming_language import ProgrammingLanguage


def main():
    """Create language objects and show dynamic ones."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    # List of all languages
    languages = [python, ruby, visual_basic]

    # Print names of dynamically typed languages
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
