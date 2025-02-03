# 1 создать класс animal  с атрибутами -  name, speciec
# 2 Создать подкласс Mammal: warm_blood = True; display_info и Bird; can_fly = True; display_info 
# 3. Создать класс Zoo: animals = []; add_animal, show_all_animals

class Animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species


class Mammal(Animal):
    def __init__(self, name, species, warm_blood = True):
         super().__init__(name, species,)
         self.warm_blood = warm_blood

    def display_info(self):
        print(f'{self.name} - {self.species}: warm blood = {self.warm_blood}')


class Bird(Animal):
    def __init__(self, name, species, can_fly = True):
         super().__init__(name, species)
         self.can_fly = can_fly

    def display_info(self):
        print(f'{self.name} - {self.species}: can fly = {self.can_fly}')


class Zoo():
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def show_all_animals(self):
        for animal in self.animals:
            animal.display_info()

zoo = Zoo()
lion = Mammal('lion', 'carnivore')
chimp = Mammal('chimp', 'omnivore')
elephant = Mammal('elephant', 'herbivore')
bear = Mammal('bear', 'omnivore')
eagle = Bird('eagle', 'carnivore')
falcon = Bird('falcon', 'carnivore')
ostrich = Bird('ostrich', 'omnivore', can_fly = False)
zoo.add_animal(lion)
zoo.add_animal(chimp)
zoo.add_animal(elephant)
zoo.add_animal(bear)
zoo.add_animal(eagle)
zoo.add_animal(falcon)
zoo.add_animal(ostrich)
zoo.show_all_animals()