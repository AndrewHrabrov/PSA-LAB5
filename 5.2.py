import random

class Dice:
    def __init__(self, count = 6, num = 1, *, seed=None):
        random.seed(seed)
        self.state = random.getstate()
        self.bones = (count, num)
    def throw(self):
        random.setstate(self.state)
        results = []
        for _ in range(self.bones[1]):
            results.append(random.randrange(1, self.bones[0]+1))
        self.state = random.getstate()
        return results

dice = Dice(count=6, num=2, seed=100000)
for i in range(1, 10):
    print(dice.throw())