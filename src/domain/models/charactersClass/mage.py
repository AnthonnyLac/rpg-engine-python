
from src.domain.models.ability import Ability
from src.domain.models.atributes.attribute import Attribute
from src.domain.models.charactersClass.character_class import CharacterClass

class Mage(CharacterClass):
    def __init__(self):
        abilities = [
            Ability("Fireball", 5, "Deals fire damage in an area."),
            Ability("Teleport", 0, "Instantly moves to a nearby location.")
        ]
        super().__init__("Mage", ["Spellcasting", "Arcane Knowledge"], abilities, 10)

    def attribute_bonus(self):
        return Attribute(intelligence=3, wisdom=1)