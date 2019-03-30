from unittest import TestCase
from person import Person
from family import Family

class TestFamily(TestCase):

    def test_family_init(self):
        husband_name = 'Evan'
        wife_name = 'Diana'
        family = Family(husband_name, wife_name)
        
        assert family.husband.name == 'Evan'
        assert family.husband.gender == 'Male'
        assert family.wife.name == 'Diana'
        assert family.wife.gender == 'Female'
        assert family.children == []