from person import Person

class Family:

    def __init__(self, husband, wife):
        self.husband = husband
        self.wife = wife
        self.children = []

    def add_daughter(self, daughter_name):
        daughter = Person(daughter_name, 'Female')
        self.children.append(daughter)
    
    def add_son(self, son_name):
        son = Person(son_name, 'Male')
        self.children.append(son)
