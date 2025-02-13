import math
# Найти дальность , время полета пули(2*V*sin(angle)/g), максимальная высота(h = (V**2*sin **2 (agle))/ 2g g=(9.81))

class CalcShot():
    def __init__(self, start_speed, shot_angle):
        self.start_speed = start_speed
        self.shot_angle = math.radians(shot_angle)
    
    def find_max_hight(self):
        max_hight = ((self.start_speed ** 2) * ( math.sin(self.shot_angle) ** 2))/ (2 * 9.81)
        return print(f'max hight {max_hight}')
    
    def find_max_time(self):
        max_time = ((self.start_speed * 2) * ( math.sin(self.shot_angle)))/ 9.81
        return print (f'max time in the air is {max_time}')
    
    def find_max_distance(self):
        max_distance = ((self.start_speed ** 2) * (math.sin(2*self.shot_angle)))/ 9.81
        return print (f'max distance {max_distance}')
