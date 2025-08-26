
from src.domain.models.atributes.attribute import Attribute


class AttributeDistribution:
    
    @staticmethod
    def from_list(values):
        """
        Recebe uma lista ou tupla com 6 valores e retorna um Attribute.
        Ordem esperada: STR, DEX, CON, INT, WIS, CHA
        """
        if len(values) != 6:
            raise ValueError("É necessário passar exatamente 6 valores para os atributos")
        
        return Attribute(**values)
    
    @staticmethod
    def classic_distribution(distribution):
        return AttributeDistribution.from_list(distribution)

    @staticmethod
    def heroic_distribution(distribution):
        return AttributeDistribution.from_list(distribution)

    @staticmethod
    def adventurer_distribution(distribution):
        return AttributeDistribution.from_list(distribution)
