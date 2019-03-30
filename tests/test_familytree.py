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
        name = 'Evan'
        gender = 'Male'
        person = Person(name, gender)
        familytree = FamilyTree(name, gender)
        wife_name = 'Diana'
        familytree.add_wife(person, wife_name)

        assert familytree.list_of_families[0].husband.name == 'Evan'
        assert familytree.list_of_families[0].wife.name == 'Diana'
        assert familytree.list_of_families[0].children == []