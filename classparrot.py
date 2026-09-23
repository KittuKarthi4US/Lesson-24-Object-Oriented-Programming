class Parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
Blu = Parrot('Blu', 17)
Woo = Parrot('Woo', 11)

print('Blu is a {}'.format(Blu.species))
print('Woo is also a {}'.format(Woo.species))

print('{} is {}-yrs old'.format(Blu.name, Blu.age))
print('{} is {}-yrs old'.format(Woo.name, Woo.age))