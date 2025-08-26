from src.domain.models.atributes.attribute_distribution import AttributeDistribution
from src.domain.models.charactersClass.mage import  Mage
from src.domain.models.charactersClass.warrior import Warrior
from src.domain.models.charactersClass.rogue import Rogue

class Character:
    def __init__(self, name, race, char_class, attribute_distribution="classic", attributes_values=None):
        self.name = name
        self.race = race
        self.char_class = char_class
        
        # Atributos base
        if attribute_distribution == "classic":
            base_attributes = AttributeDistribution.classic_distribution(attributes_values)
        elif attribute_distribution == "heroic":
            base_attributes = AttributeDistribution.heroic_distribution(attributes_values)
        elif attribute_distribution == "adventurer":
            base_attributes = AttributeDistribution.adventurer_distribution(attributes_values)
        else:
            raise ValueError("Invalid attribute distribution")


        # Atributos finais = base + raça + classe
        #comentado somatoria de atributos
        self.attributes = base_attributes #+ self.race.attribute_bonus() + self.char_class.attribute_bonus()

    def sheet(self):
            return (
                f"=== {self.name} ===\n"
                f"Race: {self.race.name} | Class: {self.char_class.name}\n"
                f"Alignment: {self.race.alignment}\n"
                f"Attributes: {self.attributes}\n"
                f"HP: {self.char_class.base_health}\n"
                f"Abilities: {[a.name for a in self.char_class.abilities + self.race.abilities]}"
            )
            
    def to_dict(self):
        return {
            "name": self.name,
            "race": {
                "name": self.race.name,
                "alignment": self.race.alignment,
                "abilities": [a.name for a in self.race.abilities]
            },
            "class": {
                "name": self.char_class.name,
                "base_health": self.char_class.base_health,
                "abilities": [a.name for a in self.char_class.abilities]
            },
            "attributes": {
                "strength": self.attributes.strength,
                "dexterity": self.attributes.dexterity,
                "constitution": self.attributes.constitution,
                "intelligence": self.attributes.intelligence,
                "wisdom": self.attributes.wisdom,
                "charisma": self.attributes.charisma
            }
        }



    def __repr__(self):
        return self.sheet()