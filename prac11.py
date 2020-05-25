class Parrot:
    species = 'bird'
    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = Parrot('blu', 24)
woo = Parrot('woo', 15)
print(f'blu is a {blu.species}')
print(f'{woo.name} is a {woo.__class__.species} with an age of {woo.age}')