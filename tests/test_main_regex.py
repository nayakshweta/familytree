from unittest import TestCase
import re

class TestMain(TestCase):

    def test_regex_pattern1(self):
        command = "Person=Evan Relation=Sons"
        pattern_existing_relation = "Person=(?P<name>[a-zA-Z]+) Relation=(?P<relation>[a-zA-Z]+)"
        
        entry = re.match(pattern_existing_relation, command)
        assert entry.group('name') == 'Evan'
        assert entry.group('relation') == 'Sons'

    def test_regex_pattern2(self):
        command = "Husband=Evan Wife=Diana"
        pattern_new_relation = "(?P<relation1>[a-zA-Z]+)=(?P<name1>[a-zA-Z]+) (?P<relation2>[a-zA-Z]+)=(?P<name2>[a-zA-Z]+)"

        entry = re.match(pattern_new_relation, command)
        assert entry.group('relation1') == 'Husband'
        assert entry.group('name1') == 'Evan'
        assert entry.group('relation2') == 'Wife'
        assert entry.group('name2') == 'Diana'