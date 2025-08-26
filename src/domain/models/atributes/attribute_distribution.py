
from src.domain.models.atributes.attribute import Attribute


class AttributeDistribution:
    @staticmethod
    def classic_distribution():
        return Attribute(10, 10, 10, 10, 10, 10)

    @staticmethod
    def heroic_distribution():
        return Attribute(16, 12, 12, 8, 8, 8)

    @staticmethod
    def adventurer_distribution(strong_attribute):
        points = {
            'strength': 10,
            'dexterity': 10,
            'constitution': 10,
            'intelligence': 10,
            'wisdom': 10,
            'charisma': 10
        }
        points[strong_attribute] = 16
        return Attribute(**points)
