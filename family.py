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
    
    def get_brothers(self, name):
        list_of_brothers = []
        for child in self.children:
            if child.name != name and child.gender == 'Male':
                list_of_brothers.append(child.name)
        return list_of_brothers

    def get_sisters(self, name):
        list_of_sisters = []
        for child in self.children:
            if child.name != name and child.gender == 'Female':
                list_of_sisters.append(child.name)
        return list_of_sisters
    
    def get_sons(self, parent_name):
        list_of_sons = []
        for child in self.children:
            if child.gender == 'Male':
                list_of_sons.append(child.name)
        return list_of_sons

    def get_daughters(self, parent_name):
        list_of_daughters = []
        for child in self.children:
            if child.gender == 'Female':
                list_of_daughters.append(child.name)
        return list_of_daughters

