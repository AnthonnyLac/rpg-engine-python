from src.domain.models.ability import Ability
from src.domain.models.atributes.attribute import Attribute
from src.domain.models.races.race import Race

class Dwarf(Race):
    def __init__(self):
        abilities = [
            Ability("Darkvision", 0, "See in the dark"),
            Ability("Stonecunning", 0, "Expert at detecting stonework")
        ]
        super().__init__("Dwarf", 6, True, "Lawful Good", abilities)

    def attribute_bonus(self):
        return Attribute(constitution=2, wisdom=1)
