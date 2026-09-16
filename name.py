class Family_name:
    def __init__(self, family_name, main_building="", root=""):
        self.family_name = family_name
        self.main_building = main_building
        self.root = root
    
class Full_name(Family_name):
    def __init__(self, family_name, last_name, main_building, root):
        super().__init__(family_name, main_building, root)
        self.last_name = last_name
    
    def name_print(self):
        print(self.family_name + self.last_name)
        
test = Full_name("홍", "길동", "", "")
print(test.family_name)
print(test.main_building)
print(test.root)
test.name_print()