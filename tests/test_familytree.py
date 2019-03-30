from unittest import TestCase
from person import Person
from family import Family
from family_tree import FamilyTree

class TestFamilyTree(TestCase):

    def test_initialize_familytree(self):
        name = 'Ben'
        gender = 'Male'
        familytree = FamilyTree(name, gender)

        assert familytree.root_person.name == 'Ben'
        assert familytree.root_person.gender == 'Male'

    def test_add_wife(self):
        person_name = 'Evan'
        gender = 'Male'
        familytree = FamilyTree(person_name, gender)
        wife_name = 'Diana'
        familytree.add_wife(person_name, wife_name)

        assert familytree.list_of_families[0].husband.name == 'Evan'
        assert familytree.list_of_families[0].wife.name == 'Diana'
        assert familytree.list_of_families[0].children == []
    
    def test_add_husband(self):
        person_name = 'Diana'
        gender = 'Female'
        familytree = FamilyTree(person_name, gender)
        husband_name = 'Evan'
        familytree.add_husband(person_name, husband_name)

        assert familytree.list_of_families[0].husband.name == 'Evan'
        assert familytree.list_of_families[0].wife.name == 'Diana'
        assert familytree.list_of_families[0].children == []
