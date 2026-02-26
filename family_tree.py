from person_factory import PersonFactory
from collections import defaultdict
# import random


class FamilyTree:
    def __init__(self):
        self.nation = []
        self.factory = PersonFactory()  # create new people

    def build_tree(self):
        root = self.factory.create_root()
        self.nation.extend(root)

        # Then read all the names from CSV
        csv_people = self.factory.read_name()
        self.nation.extend(csv_people)

    def print_total_people(self):
        print(f"Total number of people in the tree: {len(self.nation)}")

    def print_by_decade(self):
        # Create a dictionary to count people per decade
        decade_count = defaultdict(int)

        # Count each person by their decade
        for person in self.nation:
            decade = person.get_decade()
            decade_count[decade] += 1

        # Sort decades for organized display
        for decade in sorted(decade_count.keys()):
            count = decade_count[decade]
            print(f"{decade}: {count}")

    def print_duplicate_names(self):
        # Dictionary to store names and the people who have them
        name_dict = defaultdict(list)

        # Group all people by their name
        for person in self.nation:
            name_dict[person.get_name()].append(person)

        duplicates_found = False

        for name in sorted(name_dict.keys()):
            people = name_dict[name]
            if len(people) > 1:
                duplicates_found = True
                print(f"\n'{name}' appears {len(people)} times:")
                for i, person in enumerate(people, 1):
                    print(
                        f"  {i}. {person.get_gender()} - {person.get_decade()}"
                    )

        if not duplicates_found:
            print("\nNo duplicate names found!")

    def run(self):
        print("Reading data files...")
        self.build_tree()
        print("Generating family tree...")

        while True:
            print("Are you interested in:")
            print("(T)otal number of people in the tree")
            print("Total number of people in the tree by (D)ecade")
            print("(N)ames duplicated")
            print("(Q)uit")

            choice = input(">").upper().strip()

            if choice == 'T':
                self.print_total_people()
            elif choice == 'D':
                self.print_by_decade()
            elif choice == 'N':
                self.print_duplicate_names()
            elif choice == 'Q':
                print("Goodbye")
                break
            else:
                print("Please pick T, D, N, or Q.")


if __name__ == "__main__":
    tree = FamilyTree()
    tree.run()
