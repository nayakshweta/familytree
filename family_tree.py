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

    def find_family_with_parent_name(self, name):
        for family in self.list_of_families:
            if family.husband.name == name or family.wife.name == name:
                return family

    def get_spouse(self, name):
        for family in self.list_of_families:
            if family.husband.name == name:
                return family.wife.name
            elif family.wife.name == name:
                return family.husband.name


    def get_aunts(self, name):
        immediate_family = self.find_family_with_child_name(name)
        mothers_name = immediate_family.wife.name
        fathers_name = immediate_family.husband.name
        mothers_sisters = []
        mothers_sisters_in_law = []
        fathers_sisters = []
        fathers_sisters_in_law = []

        try:
            mothers_family = self.find_family_with_child_name(mothers_name)
            mothers_sisters = mothers_family.get_sisters(mothers_name)
            mothers_brothers = mothers_family.get_brothers(mothers_name)
            mothers_sisters_in_law = []
            for brother in mothers_brothers:
                mothers_sister_in_law = self.get_spouse(brother)
                if mothers_sister_in_law == None:
                    pass
                else:
                    mothers_sisters_in_law.append(mothers_sister_in_law)
        except:
            pass

        try:
            fathers_family = self.find_family_with_child_name(fathers_name)
            fathers_sisters = fathers_family.get_sisters(fathers_name)
            fathers_brothers = fathers_family.get_brothers(fathers_name)
            fathers_sisters_in_law = []
            for brother in fathers_brothers:
                fathers_sister_in_law = self.get_spouse(brother)
                if fathers_sister_in_law == None:
                    pass
                else:
                    fathers_sisters_in_law.append(fathers_sister_in_law)
        except:
            pass

        aunts_list = mothers_sisters + mothers_sisters_in_law + fathers_sisters + fathers_sisters_in_law
        return aunts_list


    def get_uncles(self, name):
        immediate_family = self.find_family_with_child_name(name)
        mothers_name = immediate_family.wife.name
        fathers_name = immediate_family.husband.name
        mothers_brothers = []
        mothers_brothers_in_law = []
        fathers_brothers = []
        fathers_brothers_in_law = []

        try:
            mothers_family = self.find_family_with_child_name(mothers_name)
            mothers_sisters = mothers_family.get_sisters(mothers_name)
            mothers_brothers = mothers_family.get_brothers(mothers_name)
            mothers_brothers_in_law = []
            for sister in mothers_sisters:
                mothers_brother_in_law = self.get_spouse(sister)
                if mothers_brother_in_law == None:
                    pass
                else:
                    mothers_brothers_in_law.append(mothers_brother_in_law)
        except:
            pass

        try:
            fathers_family = self.find_family_with_child_name(fathers_name)
            fathers_sisters = fathers_family.get_sisters(fathers_name)
            fathers_brothers = fathers_family.get_brothers(fathers_name)
            fathers_brothers_in_law = []
            for sister in fathers_sisters:
                fathers_brother_in_law = self.get_spouse(sister)
                if fathers_brother_in_law == None:
                    pass
                else:
                    fathers_brothers_in_law.append(fathers_brother_in_law)
        except:
            pass

        uncles_list = mothers_brothers + mothers_brothers_in_law + fathers_brothers + fathers_brothers_in_law
        return uncles_list


    def get_cousins(self, name):
        aunts_list = self.get_aunts(name)
        uncles_list = self.get_uncles(name)
        aunts_and_uncles_list = aunts_list + uncles_list
        cousins = []

        for auntoruncle in aunts_and_uncles_list:
            try:
                auntoruncle_family = self.find_family_with_parent_name(auntoruncle)
                for child in auntoruncle_family.children:
                    if child.name in cousins:
                        pass
                    else:
                        cousins.append(child.name)
            except:
                pass
        
        return cousins

    
    def get_grandfathers(self, name):
        immediate_family = self.find_family_with_child_name(name)
        mothers_name = immediate_family.wife.name
        fathers_name = immediate_family.husband.name
        grandfathers = []

        try:
            mothers_family = self.find_family_with_child_name(mothers_name)
            grandfather = mothers_family.husband.name
            grandfathers.append(grandfather)
        except:
            pass

        try:
            fathers_family = self.find_family_with_child_name(fathers_name)
            grandfather = fathers_family.husband.name
            grandfathers.append(grandfather)
        except:
            pass
        
        return grandfathers
    
    def get_grandmothers(self, name):
        immediate_family = self.find_family_with_child_name(name)
        mothers_name = immediate_family.wife.name
        fathers_name = immediate_family.husband.name
        grandmothers = []

        try:
            mothers_family = self.find_family_with_child_name(mothers_name)
            grandmother = mothers_family.wife.name
            grandmothers.append(grandmother)
        except:
            pass

        try:
            fathers_family = self.find_family_with_child_name(fathers_name)
            grandmother = fathers_family.wife.name
            grandmothers.append(grandmother)
        except:
            pass
        
        return grandmothers