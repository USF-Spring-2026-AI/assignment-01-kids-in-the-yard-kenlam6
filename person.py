class Person:

    def __init__(self, name, gender, decade):
        self._name = name
        self._gender = gender
        self._decade = decade

    # Accessor (getter) methods

    def get_name(self):
        return self._name

    def get_gender(self):
        return self._gender

    def get_decade(self):
        return self._decade
    # Mutator (setter) methods
