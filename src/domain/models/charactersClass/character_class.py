from src.domain.models.atributes.attribute import Attribute
from abc import ABC, abstractmethod


class CharacterClass(ABC):
    def __init__(self, name, skills, abilities, base_health):
        self.name = name
        self.skills = skills
        self.abilities = abilities
        self.base_health = base_health

    @abstractmethod
    def attribute_bonus(self) -> Attribute:
        pass

    def __repr__(self):
        abilities_str = ", ".join(str(ability) for ability in self.abilities)
        return f"{self.name} (HP: {self.base_health}, Skills: {self.skills}, Abilities: {abilities_str})"







