from person import Person
from family import Family

class FamilyTree:

    def __init__(self, name, gender):
        self.root_person = Person(name, gender)
        self.list_of_families = []

    def find_person(self, name):
        if self.root_person.name == name:
            person = self.root_person
        else:
            for family in self.list_of_families:
                if (family.husband.name == self.root_person.name) and (family.husband.name == name):
                    person = family.husband
                elif (family.wife.name == self.root_person.name) and (family.wife.name == name):
                    person = family.wife
                else:
                    for child in family.children:
                        if child.name == name:
                            person = child
        return person


    def add_wife(self, person_name, wife_name):
        person = self.find_person(person_name)
        wife = Person(wife_name, 'Female')
        family = Family(person, wife)
        self.list_of_families.append(family)

    def add_husband(self, person_name, husband_name):
        person = self.find_person(person_name)
        husband = Person(husband_name, 'Male')
        family = Family(husband, person)
        self.list_of_families.append(family)


    def find_family_with_child_name(self, name):
        for family in self.list_of_families:
            for child in family.children:
                if child.name == name:
                    return family
