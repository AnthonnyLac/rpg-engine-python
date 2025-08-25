from src.domain.models.ability import Ability
from src.domain.models.attribute import Attribute

class CharacterClass:
    def __init__(self, name, skills, abilities, base_health):
        self.name = name
        self.skills = skills
        self.abilities = abilities
        self.base_health = base_health

    def attribute_bonus(self):
        return Attribute()  # padrão: sem bônus

    def __repr__(self):
        abilities_str = ", ".join(str(ability) for ability in self.abilities)
        return f"{self.name} (HP: {self.base_health}, Skills: {self.skills}, Abilities: {abilities_str})"


class Warrior(CharacterClass):
    def __init__(self):
        abilities = [
            Ability("Second Wind", 0, "Regain health during combat."),
            Ability("Battle Focus", 0, "Gain a temporary combat bonus.")
        ]
        super().__init__("Warrior", ["Swordsmanship", "Shield Defense"], abilities, 20)

    def attribute_bonus(self):
        return Attribute(strength=2, constitution=2)


class Mage(CharacterClass):
    def __init__(self):
        abilities = [
            Ability("Fireball", 5, "Deals fire damage in an area."),
            Ability("Teleport", 0, "Instantly moves to a nearby location.")
        ]
        super().__init__("Mage", ["Spellcasting", "Arcane Knowledge"], abilities, 10)

    def attribute_bonus(self):
        return Attribute(intelligence=3, wisdom=1)


class Rogue(CharacterClass):
    def __init__(self):
        abilities = [
            Ability("Sneak Attack", 10, "Deals extra damage from stealth."),
            Ability("Evasion", 0, "Avoid damage from certain attacks.")
        ]
        super().__init__("Rogue", ["Stealth", "Lockpicking"], abilities, 15)

    def attribute_bonus(self):
        return Attribute(dexterity=3, charisma=1)
