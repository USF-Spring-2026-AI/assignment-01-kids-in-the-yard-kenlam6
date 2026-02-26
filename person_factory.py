import random
from person import Person


class PersonFactory:
    # store all the people
    def create_id(self, row: dict):
        return Person(
            gender=row['gender'],
            name=row['name'],
            decade=row['decade'],
            last=None
        )

    def __init__(self):
        self.name_data = []

    def create_root(self):
        # list to hold 2 people
        couple = []
        # Create Desmond
        desmond = Person(
            name="Desmond",
            gender="male",
            decade="1950s",
            last="Jones"
        )
        couple.append(desmond)
        # Create Molly
        molly = Person(
            name="Molly",
            gender="female",
            decade="1950s",
            last="Smith"
        )
        # she marries Desmond, she takes his last
        molly.set_last("Jones")
        couple.append(molly)
        return couple

    def last_name_prob(self):
        last_names_dict = {}
        for _, row in self.last_names.iterrows():
            last_names_dict[row['Rank']] = {
                'LastName': row['LastName'],
                'Decade': row['Decade']
            }
        # Get the first row as a list of floats
        float_values = self.prob.iloc[0].tolist()

        # Create probability dictionary with rank as key
        # Since rank 1 corresponds to index 0, rank 2 to index 1, etc.
        probab_dict = {rank+1: float_values[rank]
                       for rank in range(len(float_values))}

        combined_dict = {}
        for rank in last_names_dict:
            if rank in probab_dict:
                combined_dict[rank] = {
                    'LastName': last_names_dict[rank]['LastName'],
                    'Decade': last_names_dict[rank]['Decade'],
                    'Probability': probab_dict[rank]
                }
        return combined_dict

    def select_name_by_probability(self, combined_dict):
        # Get all names and their probabilities
        names = []
        probabilities = []

        for rank in sorted(combined_dict.keys()):
            names.append(combined_dict[rank]['LastName'])
            probabilities.append(combined_dict[rank]['Probability'])

        # Select one name based on probabilities
        selected_name = random.choices(names, weights=probabilities, k=1)[0]
        return selected_name
