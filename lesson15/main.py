# Задача:
# Напишите класс Character обладающий 3 характеристиками: атака, здоровье, уклоенине
# FIGHTER = {"health": 5, "attack": 3, "dodge": 1}
# THIEF = {"health": 2, "attack": 3, "dodge": 4}
# MAGE = {"health": 1, "attack": 5, "dodge": 4}
# TYPES = {"fighter": FIGHTER, "thief": THIEF, "mage": MAGE}
# Класс имеет следующие методы:
# Распределение атрибутов как описано выше: character_1 = Character("fighter")
# Атака
# Получение урона в случае если увернуться не удалось.
# Уклонение: каждое очко уклонения умножается на 5. Результат уклонения зависит от рандомно генерируемого числа
# от 0 до 100. Если это число меньше или равно навыка уклонения, то герой уклоняется от атаки.
# Смерть: если здоровье меньше 1.
# Напишите функцию которая заставит сразиться разных героев друг с другом 100 раз. Выведите счет.
from random import randint

FIGHTER = {"health": 5, "attack": 3, "dodge": 1}
THIEF = {"health": 2, "attack": 3, "dodge": 4}
MAGE = {"health": 1, "attack": 5, "dodge": 4}
TYPES = {"fighter": FIGHTER, "thief": THIEF, "mage": MAGE}

class Character():

    def __init__(self, type):
        self.types = TYPES[type]
        self.name = type

    def asign_atributes(self):
        self.attack = self.types['attack']
        self.health = self.types['health']
        self.dodge = self.types['dodge']
    
    def attacking(self):
        do_damage = self.attack
        return do_damage
    
    def dodging(self):
        dodge_points = self.dodge * 5
        return dodge_points

    
    def get_damage(self, opponent_attack):
            self.health -= opponent_attack
            return self.health
    
    def dying(self):
        if self.health < 1:
            return True
        
fighter = Character('fighter')
fighter.asign_atributes()
mage = Character('mage')
mage.asign_atributes()
thief = Character('thief')
thief.asign_atributes()

if __name__ == '__main__':  
      
    def fighting(first, second):
        wins_f = 0
        wins_s = 0
        attack_f = first.attacking()
        attack_s = second.attacking()
        for fight in range(100):
            end_of_fight = False
            while end_of_fight == False:
                if first.dodging() < randint(0, 100):
                    first.get_damage(attack_s)
                    if first.dying():
                        wins_s += 1
                        end_of_fight = True
                        continue
                if second.dodging() < randint(0, 100):
                    second.get_damage(attack_f)
                    if second.dying():
                        wins_f += 1
                        end_of_fight = True
                        continue
        if wins_f > wins_s:
            print(f'{first.name} won by {wins_f - wins_s} points!')
        elif wins_s > wins_f:
            print(f'{second.name} won by {wins_s - wins_f} points!')
        else:
            print(f'It is  a draw: {wins_f, wins_s}')

    fighting(thief, fighter)