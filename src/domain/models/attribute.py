class Attribute:
    def __init__(self, strength=0, dexterity=0, constitution=0, intelligence=0, wisdom=0, charisma=0):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    def __add__(self, other):
        return Attribute(
            self.strength + other.strength,
            self.dexterity + other.dexterity,
            self.constitution + other.constitution,
            self.intelligence + other.intelligence,
            self.wisdom + other.wisdom,
            self.charisma + other.charisma
        )

    def __repr__(self):
        return (f"STR:{self.strength}, DEX:{self.dexterity}, CON:{self.constitution}, "
                f"INT:{self.intelligence}, WIS:{self.wisdom}, CHA:{self.charisma}")


class AttributeDistribution:
    @staticmethod
    def classic_distribution():
        return Attribute(10, 10, 10, 10, 10, 10)

    @staticmethod
    def heroic_distribution():
        return Attribute(16, 12, 12, 8, 8, 8)

    @staticmethod
    def adventurer_distribution(strong_attribute):
        points = {
            'strength': 10,
            'dexterity': 10,
            'constitution': 10,
            'intelligence': 10,
            'wisdom': 10,
            'charisma': 10
        }
        points[strong_attribute] = 16
        return Attribute(**points)
