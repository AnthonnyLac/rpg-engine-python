from src.domain.models.atributes.attribute import Attribute

class Race:
    def __init__(self, name, movement, infravision, alignment, abilities):
        self.name = name
        self.movement = movement
        self.infravision = infravision
        self.alignment = alignment
        self.abilities = abilities

    def attribute_bonus(self):
        return Attribute()  # padrão: sem bônus

    def __repr__(self):
        abilities_str = ", ".join(str(ability) for ability in self.abilities)
        return f"{self.name} (Movement: {self.movement}, Infravision: {self.infravision}, Alignment: {self.alignment}, Abilities: {abilities_str})"





