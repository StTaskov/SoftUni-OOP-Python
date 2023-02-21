class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):

        group_name = f"{self.name} {other.name}"
        all_peoples = self.people + other.people

        return Group(group_name, all_peoples)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join([repr(p) for p in self.people])}"

    def __getitem__(self, item):
        people_name = [repr(p) for p in self.people]

        return f"Person {item}: {people_name[item]}"
