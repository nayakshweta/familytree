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
    
    def test_get_brothers(self):
        husband = Person('Evan', 'Male')
        wife = Person('Diana', 'Female')
        family = Family(husband, wife)
        family.add_son('John')
        family.add_son('Alex')
        family.add_son('Joe')
        family.add_daughter('Nisha')
        list_of_brothers = family.get_brothers('Joe')
        
        assert 'Alex' in list_of_brothers
        assert 'John' in list_of_brothers
        assert 'Nisha' not in list_of_brothers
    
    def test_get_sisters(self):
        husband = Person('Evan', 'Male')
        wife = Person('Diana', 'Female')
        family = Family(husband, wife)
        family.add_son('John')
        family.add_son('Alex')
        family.add_son('Joe')
        family.add_daughter('Nisha')
        list_of_sisters = family.get_sisters('Joe')

        assert 'Nisha' in list_of_sisters
        assert 'Alex' not in list_of_sisters