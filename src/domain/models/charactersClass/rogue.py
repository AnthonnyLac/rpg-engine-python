from src.domain.models.ability import Ability
from src.domain.models.atributes.attribute import Attribute
from src.domain.models.charactersClass.character_class import CharacterClass

class Rogue(CharacterClass):
    def __init__(self):
        abilities = [
            Ability("Sneak Attack", 10, "Deals extra damage from stealth."),
            Ability("Evasion", 0, "Avoid damage from certain attacks.")
        ]
        super().__init__("Rogue", ["Stealth", "Lockpicking"], abilities, 15)

    def attribute_bonus(self):
        return Attribute(dexterity=3, charisma=1)