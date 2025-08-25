# src/domain/models/ability.py

class Ability:
    def __init__(self, name, damage=0, description="", cost=0, scaling_attr=None, target="enemy"):
        """
        :param name: Nome da habilidade
        :param damage: Dano base da habilidade
        :param description: Descrição narrativa
        :param cost: Custo (mana, stamina, etc.)
        :param scaling_attr: Atributo que escala o dano (ex: 'strength', 'intelligence')
        :param target: Alvo da habilidade ('enemy', 'ally', 'self', 'area')
        """
        self.name = name
        self.damage = damage
        self.description = description
        self.cost = cost
        self.scaling_attr = scaling_attr  # opcional, para multiplicar dano
        self.target = target

    def calculate_damage(self, user, target=None):
        """
        Calcula o dano final levando em conta atributos do usuário.
        :param user: Personagem que usa a habilidade (Character)
        :param target: Alvo (Character ou None)
        :return: Valor numérico do dano
        """
        final_damage = self.damage
        if self.scaling_attr and hasattr(user, "attributes"):
            final_damage += user.attributes.get(self.scaling_attr, 0)
        return final_damage

    def __repr__(self):
        scaling = f", Scales with: {self.scaling_attr}" if self.scaling_attr else ""
        return (f"{self.name} (Damage: {self.damage}, Cost: {self.cost}, "
                f"Target: {self.target}{scaling}, Description: {self.description})")
