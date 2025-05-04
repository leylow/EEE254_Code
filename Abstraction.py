"""Abstract Data Types (ADTs) help in managing complexity in programs by 
defining data structures by what they do rather than how they do it. 
In Python, classes are a way to implement ADTs. Key benefits of using ADTs include:

Encapsulation: Hide implementation details.

Reusability: Once defined, ADTs can be reused in different programs.

Modularity: Break a large problem into smaller, manageable units.

Maintainability: Easier to debug, test, and upgrade.

"""

import datetime

# Define an Abstract Data Type (ADT) called Person
class Person:
    def __init__(self, name):
        """
        Initialize the Person object with a name.
        Abstract idea: A 'Person' has a full name and possibly a birthday.
        """
        self._name = name  # Full name (e.g., "John Doe")

        try:
            # Attempt to extract the last name assuming there's a space in the name
            last_blank = name.rindex(' ')
            self._last_name = name[last_blank + 1:]
        except ValueError:
            # If there's no space, the entire name is used as the last name
            self._last_name = name
        
        self._birthday = None  # Birthday is initially unknown

    def get_name(self):
        """
        Public interface to get the person's full name.
        Abstracted: Users don't need to know how the name is stored internally.
        """
        return self._name

    def get_last_name(self):
        """
        Return the last name, used for sorting or display.
        Abstracted from the logic of how it's extracted.
        """
        return self._last_name

    def set_birthday(self, birthdate):
        """
        Sets the birthday for the person.
        Abstracts the use of datetime.date type.
        """
        self._birthday = birthdate

    def get_age(self):
        """
        Calculate age in days from birthday until today.
        Abstracts away date manipulation and error checking.
        """
        if self._birthday is None:
            raise ValueError("Birthday not set.")
        return (datetime.date.today() - self._birthday).days

    def __lt__(self, other):
        """
        Compare two Person objects for sorting.
        Uses abstraction by prioritizing last name, then full name.
        """
        if self._last_name == other._last_name:
            return self._name < other._name
        return self._last_name < other._last_name

    def __str__(self):
        """
        String representation of the person object.
        Abstracted display logic.
        """
        return self._name
