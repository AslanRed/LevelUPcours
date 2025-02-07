# Управление кафе

# 1 создать класс Drink  с атрибутами  name и  volume, с методом  display info
class Drink():

    def __init__(self,name, volume):
        self.name = name
        self.volume = volume
    
    def display_info(self):
        return print(f'Это {self.name}, остаток - {self.volume}')
    
vine = Drink('vine', 700)
vine.display_info()

# 2 Создать 2 подкласса - холодные и горячие напитки
class HotDrink(Drink):
     
    def __init__(self, name, volume, temperature = 75):
        super().__init__(name, volume)
        self.temperature = temperature

    def display_info(self):
        return print(f'Это {self.name}, остаток - {self.volume}, temp - {self.temperature}')

tea = HotDrink('tea', 200, 90)
tea.display_info()

class ColdDrink(Drink):
     
    def __init__(self, name, volume, ice_cubes = 3):
        super().__init__(name, volume)
        self.ice_cubes = ice_cubes

    def display_info(self):
        return print(f'Это {self.name}, остаток - {self.volume}, temp - {self.ice_cubes}')
    
juice = ColdDrink('juice', 500, 4)
juice.display_info()

