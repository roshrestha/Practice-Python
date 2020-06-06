class Player:
    
    teamName = 'Liverpool'
    teamMembers = []
    
    def __init__(self, name):
        self.name = name #creating instance variable
        self.formerTeams = []
        self.teamMembers.append(self.name)
        
    @classmethod
    def demo(cls):
        cls.teamName = 'Arsenal'
        return cls.teamName
    @classmethod
    def demo1(cls):
        return cls.teamMembers

print(Player.demo1())
    
    
    
    
print(Player.demo())

    
        
        
p1 = Player('Mark')
p2 = Player('Steve')
p1.formerTeams.append('Barcelona')
p2.formerTeams.append('Chelsea')
print('Name:', p1.name)
print('Team Name:', p1.teamName)
print('Former Team:', p1.formerTeams)
print('Team Members:', p1.teamMembers)
print('Name:', p2.name)
print('Team Name:', p2.teamName)
print('Former Team:', p2.formerTeams)
print('Team Members:', p2.teamMembers)

