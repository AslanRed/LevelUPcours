import math
import matplotlib.pyplot as plt
# Найти дальность , время полета пули, максимальная высота

class CalcShot():
    def __init__(self, start_speed, shot_angle, bul_size, bul_mass, cr):
        self.speed = start_speed
        self.angle = math.radians(shot_angle)
        self.b_size = bul_size
        self.bl_mass = bul_mass
        self.cr = cr
        self.rho  = 1.225
        self.Sm = math.pi * (self.b_size ** 2)/4
        self.kr = cr * self.Sm * self.rho / (2 * self.bl_mass)

    def shoot(self):
        x, y = 0, 0 
        val_x, val_y = [x], [y]
        val_speed = [self.speed]
        dt = 0.01
        g = 9.8
        time = 0
        val_time = [time]
        while 1:
            x = x + (self.speed * math.cos(self.angle)) * dt
            val_x.append(x)
            y = y + (self.speed * math.sin(self.angle)) * dt
            val_y.append(y)
            new_angle = self.angle - dt * g * math.cos(self.angle)/ self.speed
            time = time + dt
            self.speed = self.speed - dt * (self.kr * (self.speed ** 2) + g * math.sin(self.angle))
            val_speed.append(self.speed)
            val_time.append(time)
            if y <= 0:
                print(f'Time in air {time}')
                print(f'Max height {val_y}')
                print(f'Max distance {round(max(val_x))}')
                print(f'Max speed {round(max(val_speed))}')
                break
        plt.plot(val_x, val_y, linewidth = 2.0)
        plt.grid()
        plt.show()
        plt.plot(val_time, val_speed, linewidth = 2.0)
        plt.grid()
        plt.show()

calc = CalcShot(210, 180, 4.5, 0.0005, 0.023)
calc.shoot()