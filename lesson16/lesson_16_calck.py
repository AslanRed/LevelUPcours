# D = (V**2*sin(2*agle))/ g g=(9.81)
# началюная скорость, угол стрельбы.
#библиотека math, угол в радианах
# Найти дальность , время полета пули(2*V*sin(angle)/g), максимальная высота(h = (V**2*sin **2 (agle))/ 2g g=(9.81))
import calc_class

if __name__ == '__main__':

    calc_for_shooting = calc_class.CalcShot(100, 180)
    calc_for_shooting.find_max_distance()
    calc_for_shooting.find_max_time()
    calc_for_shooting.find_max_hight()