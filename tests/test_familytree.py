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
        assert familytree.list_of_families == []

    def test_find_person(self):
        familytree = FamilyTree('Diana', 'Female')
        husband = Person('Evan', 'Male')
        family = Family(husband, familytree.root_person)
        familytree.list_of_families.append(family)
        familytree.list_of_families[0].add_daughter('Nisha')
        familytree.list_of_families[0].add_son('Joe')
        actual_person = familytree.find_person('Joe')

        assert actual_person.name == 'Joe'

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


    def test_family_with_child_name(self):
        person_name = 'Evan'
        gender = 'Male'
        familytree = FamilyTree(person_name, gender)
        familytree.add_wife('Evan', 'Diana')
        familytree.list_of_families[0].add_daughter('Nisha')
        familytree.add_husband('Nisha', 'Adam')
        familytree.list_of_families[0].add_son('Joe')
        familytree.add_wife('Joe', 'Niki')
        family = familytree.find_family_with_child_name('Joe')

        assert len(family.children) == 2

    def test_family_with_parent_name(self):
        person_name = 'Evan'
        gender = 'Male'
        familytree = FamilyTree(person_name, gender)
        familytree.add_wife('Evan', 'Diana')
        familytree.list_of_families[0].add_daughter('Nisha')
        familytree.add_husband('Nisha', 'Adam')
        familytree.list_of_families[0].add_son('Joe')
        familytree.add_wife('Joe', 'Niki')
        family = familytree.find_family_with_parent_name('Joe')

        assert family.children == []

    def test_get_spouse(self):
        familytree = FamilyTree('Evan', 'Male')
        familytree.add_wife('Evan', 'Diana')
        EvanDianasfamily = familytree.find_family_with_parent_name('Diana')
        EvanDianasfamily.add_daughter('Nisha')
        EvanDianasfamily.add_son('John')
        EvanDianasfamily.add_son('Joe')
        EvanDianasfamily.add_son('Alex')
        familytree.add_wife('Alex', 'Nancy')
        familytree.add_wife('Joe', 'Niki')
        familytree.add_husband('Nisha', 'Adam')
        AlexNancysfamily = familytree.find_family_with_parent_name('Alex')
        AlexNancysfamily.add_son('Jacob')
        AlexNancysfamily.add_son('Shaun')
        JoeNikisfamily = familytree.find_family_with_parent_name('Niki')
        JoeNikisfamily.add_son('Piers')
        JoeNikisfamily.add_daughter('Sally')
        actual_spouse = familytree.get_spouse('Joe')

        assert actual_spouse == 'Niki'

    def test_get_aunts(self):
        familytree = FamilyTree('Evan', 'Male')
        familytree.add_wife('Evan', 'Diana')
        EvanDianasfamily = familytree.find_family_with_parent_name('Diana')
        EvanDianasfamily.add_daughter('Nisha')
        EvanDianasfamily.add_son('John')
        EvanDianasfamily.add_son('Joe')
        EvanDianasfamily.add_son('Alex')
        familytree.add_wife('Alex', 'Nancy')
        familytree.add_wife('Joe', 'Niki')
        familytree.add_husband('Nisha', 'Adam')
        AlexNancysfamily = familytree.find_family_with_parent_name('Alex')
        AlexNancysfamily.add_son('Jacob')
        AlexNancysfamily.add_son('Shaun')
        JoeNikisfamily = familytree.find_family_with_parent_name('Niki')
        JoeNikisfamily.add_son('Piers')
        JoeNikisfamily.add_daughter('Sally')
        aunts_list = familytree.get_aunts('Shaun')

        assert len(aunts_list) == 2
    
    def test_get_uncles(self):
        familytree = FamilyTree('Evan', 'Male')
        familytree.add_wife('Evan', 'Diana')
        EvanDianasfamily = familytree.find_family_with_parent_name('Diana')
        EvanDianasfamily.add_daughter('Nisha')
        EvanDianasfamily.add_son('John')
        EvanDianasfamily.add_son('Joe')
        EvanDianasfamily.add_son('Alex')
        familytree.add_wife('Alex', 'Nancy')
        familytree.add_wife('Joe', 'Niki')
        familytree.add_husband('Nisha', 'Adam')
        AlexNancysfamily = familytree.find_family_with_parent_name('Alex')
        AlexNancysfamily.add_son('Jacob')
        AlexNancysfamily.add_son('Shaun')
        JoeNikisfamily = familytree.find_family_with_parent_name('Niki')
        JoeNikisfamily.add_son('Piers')
        JoeNikisfamily.add_daughter('Sally')
        uncles_list = familytree.get_uncles('Shaun')

        assert len(uncles_list) == 3