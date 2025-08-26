import random

class Utils:

    @staticmethod
    def roll_3d6():
        return sum(random.randint(1, 6) for _ in range(3))

    @staticmethod
    def roll_4d6_drop_lowest():
        rolls = [random.randint(1, 6) for _ in range(4)]
        rolls.remove(min(rolls))
        return sum(rolls)