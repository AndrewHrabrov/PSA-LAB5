import random

class Dice:
    def __init__(self, count = 6, num = 1, *, seed=None):
        self.bones = (count, num)
    def throw(self):
        result = []
        for _ in range(self.bones[1]):
            result.append(random.randrange(1, self.bones[0]+1))
        return result

for i in range(1, 1000):
    dice = Dice(count=6, num=2)
    print(dice.throw())