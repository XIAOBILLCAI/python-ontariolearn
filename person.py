"""
Person.
"""

class Person:
    """Represents people!"""
    def __init__(self, first_name, last_name, height):
        self.first_name = first_name
        self.last_name = last_name
        self.height = height

    def get_full_name(self):
        """Return first and last name."""
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.get_full_name()

    def __repr__(self):
        return 'Person(first_name={}, last_name={}, height={})'.format(
            repr(self.first_name),
            repr(self.last_name),
            repr(self.height)
        )
        
