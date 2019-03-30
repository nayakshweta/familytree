from person import Person

class Family:

    def __init__(self, husband_name, wife_name):
        self.husband = Person(husband_name, 'Male')
        self.wife = Person(wife_name, 'Female')
        self.children = []

    def add_daughter(self, daughter_name):
        pass
