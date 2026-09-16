class FirstName:
    def __init__(self, first_name):
        self.first_name = first_name

class MySecondName(FirstName):
    def __init__(self, second_name):
        super().__init__()
        self.second_name = second_name
        
    def __str__(self):
        return self.first_name + self.second_name
        
class MySisterName(FirstName):
    def __init__(self):
        super().__init__()
        self.second_name = "민지"
        
    def __str__(self):
        return self.first_name + self.second_name

first = FirstName("선")
me = MySecondName("종범")
sister = MySisterName()
print(me)
print(sister)

class Family_name:
    def __init__(self, name):
        self.name = name
    
class Last_name(Family_name):
    def __init__(self, name):
        self.name = name
        
a = Family_name("홍")
b = Last_name("길동")
full_name = a.name + b.name
print(full_name)