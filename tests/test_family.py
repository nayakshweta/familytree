from unittest import TestCase
from person import Person
from family import Family

class TestFamily(TestCase):

    def test_family_init(self):
        husband = Person('Evan', 'Male')
        wife = Person('Diana', 'Female')
        family = Family(husband, wife)
        
        assert family.husband.name == 'Evan'
        assert family.husband.gender == 'Male'
        assert family.wife.name == 'Diana'
        assert family.wife.gender == 'Female'
        assert family.children == []
    
    def test_add_daughter(self):
        husband = Person('Evan', 'Male')
        wife = Person('Diana', 'Female')
        family = Family(husband, wife)
        daughter_name = 'Nisha'
        family.add_daughter(daughter_name)

        assert family.children[0].name == 'Nisha'
        assert family.children[0].gender == 'Female'
    
    def test_add_son(self):
        husband = Person('Evan', 'Male')
        wife = Person('Diana', 'Female')
        family = Family(husband, wife)
        son_name = 'Alex'
        family.add_son(son_name)

        assert family.children[0].name == 'Alex'
        assert family.children[0].gender == 'Male'
