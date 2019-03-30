from unittest import TestCase
from person import Person

class TestPerson:

    def test_initialize_person(self):
        name = 'Evan'
        gender = 'Male'
        person = Person(name, gender)

        assert person.name == "Evan"
        assert person.gender == "Male"