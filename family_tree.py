from person import Person
from family import Family

class FamilyTree:

    def __init__(self, name, gender):
        self.root_person = Person(name, gender)
        self.list_of_families = []

    def add_wife(self, person, wife_name):
        wife = Person(wife_name , 'Female')
        family = Family(person, wife)
        self.list_of_families.append(family)

    def add_husband(self, person, husband_name):
        husband = Person(husband_name, 'Male')
        family = Family(husband, person)
        self.list_of_families.append(family)
