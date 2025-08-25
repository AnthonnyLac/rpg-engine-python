from src.domain.models.race import Elf, Dwarf, Human
from src.domain.models.character_class import Warrior, Mage, Rogue
from src.domain.models.character import Character

class CharacterFactory:
    @staticmethod
    def create(name, race_type, class_type, distribution="classic", strong_attribute=None):
        races = {"elf": Elf, "dwarf": Dwarf, "human": Human}
        classes = {"warrior": Warrior, "mage": Mage, "rogue": Rogue}

        if race_type.lower() not in races:
            raise ValueError(f"Invalid race: {race_type}")
        if class_type.lower() not in classes:
            raise ValueError(f"Invalid class: {class_type}")

        race = races[race_type.lower()]()
        char_class = classes[class_type.lower()]()

        return Character(name, race, class_type, distribution, strong_attribute)
