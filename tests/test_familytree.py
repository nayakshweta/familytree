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
