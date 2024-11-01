import random

class Dice:
    def __init__(self, count = 6, num = 1, seed=None):
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

dice = Dice(6, 2)
results = []
for _ in range(1, 100001):
    results.append(sum(dice.throw()))
for i in range(2, 13):
    print(f'{i} выпало {results.count(i)} раз')