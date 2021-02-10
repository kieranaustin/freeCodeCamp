import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k,v in kwargs.items():
            self.contents += ([k] * int(v))

    def draw(self, num_balls_drawn):
        if num_balls_drawn > len(self.contents):
            return self.contents
        else:
            drawn = []
            for i in range(num_balls_drawn):
                pos = random.randrange(len(self.contents))
                drawn += [self.contents.pop(pos)]
            return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hits = 0
    for i in range(num_experiments):
        hatCopy = copy.deepcopy(hat)
        drawn = hatCopy.draw(num_balls_drawn)
        hitList = []
        for k,v in expected_balls.items():
            if drawn.count(str(k))>=int(v):
                hitList.append(True)
            else:
                hitList.append(False)
        if all(hitList):
            hits += 1

    return hits/num_experiments
