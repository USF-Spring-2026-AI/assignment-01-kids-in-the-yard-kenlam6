class Person:

    def __init__(self, name, gender, decade, last):
        self._name = name
        self._gender = gender
        self._decade = decade
        # self._last = last

    # Accessor (getter) methods

    def get_name(self):
        return self._name

    def get_last(self):
        return self._last

    def get_gender(self):
        return self._gender

    def get_decade(self):
        return self._decade

    def get_full(self):
        return f"{self._name} {self._last}"

    # Mutator (setter) methods

    def set_last(self, last):
        self._last = last
