
from src.domain.models.ability import Ability
from src.domain.models.atributes.attribute import Attribute
from src.domain.models.races.race import Race

class Elf(Race):
    def __init__(self):
        abilities = [
            Ability("Keen Senses", 0, "Advantage on perception checks"),
            Ability("Magic Resistance", 0, "Advantage on saving throws against magic")
        ]
        super().__init__("Elf", 9, True, "Neutral", abilities)

    def attribute_bonus(self):
        return Attribute(dexterity=2, intelligence=1)