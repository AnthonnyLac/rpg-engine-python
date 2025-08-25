from src.domain.models.ability import Ability
from src.domain.models.attribute import Attribute

class Race:
    def __init__(self, name, movement, infravision, alignment, abilities):
        self.name = name
        self.movement = movement
        self.infravision = infravision
        self.alignment = alignment
        self.abilities = abilities

    def attribute_bonus(self):
        return Attribute()  # padrão: sem bônus

    def __repr__(self):
        abilities_str = ", ".join(str(ability) for ability in self.abilities)
        return f"{self.name} (Movement: {self.movement}, Infravision: {self.infravision}, Alignment: {self.alignment}, Abilities: {abilities_str})"


class Elf(Race):
    def __init__(self):
        abilities = [
            Ability("Keen Senses", 0, "Advantage on perception checks"),
            Ability("Magic Resistance", 0, "Advantage on saving throws against magic")
        ]
        super().__init__("Elf", 9, True, "Chaotic Good", abilities)

    def attribute_bonus(self):
        return Attribute(dexterity=2, intelligence=1)


class Dwarf(Race):
    def __init__(self):
        abilities = [
            Ability("Darkvision", 0, "See in the dark"),
            Ability("Stonecunning", 0, "Expert at detecting stonework")
        ]
        super().__init__("Dwarf", 6, True, "Lawful Good", abilities)

    def attribute_bonus(self):
        return Attribute(constitution=2, wisdom=1)


class Human(Race):
    def __init__(self):
        abilities = [
            Ability("Versatile", 0, "Can adapt to various tasks"),
            Ability("Adaptable", 0, "Bonus to any attribute")
        ]
        super().__init__("Human", 9, False, "Neutral", abilities)

    def attribute_bonus(self):
        return Attribute(strength=1, dexterity=1, constitution=1, intelligence=1, wisdom=1, charisma=1)
