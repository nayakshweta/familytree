from family_tree import FamilyTree
import re

def main():

    input = raw_input("Welcome to familytree. Please enter input in the format Name<space>Gender of the person whose familytree you are creating.\n")
    input_list = input.split(' ')
    root_person_name = input_list[0]
    root_person_gender = input_list[1]

    familytree = FamilyTree(root_person_name, root_person_gender)

    print "Welcome to", root_person_name,"'s familytree."
    print "Find or Update relationships.\n"

    while True:
        command = raw_input("Input:")

        pattern_existing_relation = "Person=(?P<name>[a-zA-Z]+) Relation=(?P<relation>[a-zA-Z]+)"
        pattern_new_relation = "(?P<relation1>[a-zA-Z]+)=(?P<name1>[a-zA-Z]+) (?P<relation2>[a-zA-Z]+)=(?P<name2>[a-zA-Z]+)"

        if command.startswith('Person'):
            entry = re.match(pattern_existing_relation, command)
            person_name = entry.group('name')
            relation = entry.group('relation')

            if relation == 'Sons':
                family = familytree.find_family_with_parent_name(person_name)
                sons_list = family.get_sons(person_name)
                print "Sons=" + ','.join(sons_list)
            
            elif relation == 'Daughters':
                family = familytree.find_family_with_parent_name(person_name)
                daughters_list = family.get_daughters(person_name)
                print "Daughters=" + ','.join(daughters_list)
            
            elif relation == 'Wife':
                wife = familytree.get_spouse(person_name)
                print "Wife=", wife

            elif relation == 'Husband':
                husband = familytree.get_spouse(person_name)
                print "Husband=", husband
            
            elif relation == 'Mother':
                family = familytree.find_family_with_child_name(person_name)
                mother = family.wife
                print "Mother=", mother

            elif relation == 'Father':
                family = familytree.find_family_with_child_name(person_name)
                father = family.husband
                print "Father=", father

            elif relation == 'Brothers':
                family = familytree.find_family_with_child_name(person_name)
                brothers_list = family.get_brothers(person_name)
                print "Brothers=", ','.join(brothers_list)

            elif relation == 'Sisters':
                family = familytree.find_family_with_child_name(person_name)
                sisters_list = family.get_sisters(person_name)
                print "Sisters=", ','.join(sisters_list)
            
            elif relation == 'Cousins':
                cousins_list = familytree.get_cousins(person_name)
                print "Cousins=", ','.join(cousins_list)

            elif relation == 'Grandmothers':
                grandmothers_list = familytree.get_grandmothers(person_name)
                print "Grandmothers=", ','.join(grandmothers_list)
            
            elif relation == 'Grandfathers':
                grandfathers_list = familytree.get_grandfathers(person_name)
                print "Grandfathers=", ','.join(grandfathers_list)
            
            elif relation == 'Grandsons':
                grandsons_list = familytree.get_grandsons(person_name)
                print "Grandsons=", ','.join(grandsons_list)
            
            elif relation == 'Granddaughters':
                granddaughters_list = familytree.get_granddaughters(person_name)
                print "Granddaughters=", ','.join(granddaughters_list)
            
            elif relation == 'Aunts':
                aunts_list = familytree.get_aunts(person_name)
                print "Aunts=", ','.join(aunts_list)

            elif relation == 'Uncles':
                uncles_list = familytree.get_uncles(person_name)
                print "Uncles=", ','.join(uncles_list)

        elif re.match(pattern_new_relation, command):
            entry = re.match(pattern_new_relation, command)
            relation1 = entry.group('relation1')
            name1 = entry.group('name1')
            relation2 = entry.group('relation2')
            name2 = entry.group('name2')

            if relation2 == 'Wife':
                familytree.add_wife(name1, name2)
                print "\nWelcome to the family,", name2

            elif relation2 == 'Husband':
                familytree.add_husband(name1, name2)
                print "\nWelcome to the family,", name2

            elif relation2 == 'Son':
                family = familytree.find_family_with_parent_name(name1)
                family.add_son(name2)
                print "\nWelcome to the family,", name2
            
            elif relation2 == 'Daughter':
                family = familytree.find_family_with_parent_name(name1)
                family.add_daughter(name2)
                print "\nWelcome to the family,", name2

        else:
            print "Unknown command, please try again."

if __name__ == "__main__":
    main()