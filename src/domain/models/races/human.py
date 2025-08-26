from src.domain.models.ability import Ability
from src.domain.models.atributes.attribute import Attribute
from src.domain.models.races.race import Race

class Human(Race):
    def __init__(self):
        abilities = [
            Ability("Versatile", 0, "Can adapt to various tasks"),
            Ability("Adaptable", 0, "Bonus to any attribute")
        ]
        super().__init__("Human", 9, False, "Neutral", abilities)

    def attribute_bonus(self):
        return Attribute(strength=1, dexterity=1, constitution=1, intelligence=1, wisdom=1, charisma=1)
