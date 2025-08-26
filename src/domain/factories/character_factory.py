from src.domain.models.races.dwarf import Dwarf
from src.domain.models.races.elf import Elf
from src.domain.models.races.human import Human
from src.domain.models.charactersClass.mage import  Mage
from src.domain.models.charactersClass.warrior import Warrior
from src.domain.models.charactersClass.rogue import Rogue
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
