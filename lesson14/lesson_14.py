#Написать класс трансформер который переводит римские числа в арабсие
class Transformer():
    def __init__(self, num):
         self.num  = num

    def transform_num(self):
        roman = {"I":1, "V": 5, "X":10, "L": 50,"C":100, "D": 500, "M":1000}
        result = 0
        for i in range(len(self.num) - 1):
            left = self.num[i]
            right = self.num[i + 1]
            if roman[left] >= roman[right]:
                result += roman[left] + roman[right]
            else:
                result += roman[right] - roman[left]
            return result

transform = Transformer('XMM')
print(transform.transform_num())