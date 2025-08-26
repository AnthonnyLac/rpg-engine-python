from src.domain.models.ability import Ability
from src.domain.models.atributes.attribute import Attribute
from src.domain.models.charactersClass.character_class import CharacterClass


class Warrior(CharacterClass):
    def __init__(self):
        abilities = [
            Ability("Second Wind", 0, "Regain health during combat."),
            Ability("Battle Focus", 0, "Gain a temporary combat bonus.")
        ]
        super().__init__("Warrior", ["Swordsmanship", "Shield Defense"], abilities, 20)

    def attribute_bonus(self):
        return Attribute(strength=2, constitution=2)