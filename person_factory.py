import csv
from person import Person


class PersonFactory:
    # store all the people
    def create_id(self, row: dict):
        return Person(
            gender=row['gender'],
            name=row['name'],
            decade=row['decade']
        )

    def read_name(self, filepath="first_names.csv"):
        nation = []
        with open(filepath, 'r') as f:
            # Create a CSV reader that treats the first row as column headers
            # DictReader creates dictionaries where keys are column names
            reader = csv.DictReader(f)
            for row in reader:
                person = self.create_id(row)

                nation.append(person)
        return nation
