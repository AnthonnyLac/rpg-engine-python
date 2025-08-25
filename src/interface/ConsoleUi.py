import src.application.character_creation as CharacterCreationService

class ConsoleUi:
    def __init__(self, repository):
        self.repository = repository
        
    VALID_RACES = ["human", "elf", "dwarf"]
    VALID_CLASSES = ["warrior", "mage", "rogue"]
    VALID_DISTRIBUTIONS = ["classic", "heroic", "adventurer"]
    VALID_ATTRIBUTES = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]
    
    @staticmethod
    def ask_choice(prompt, valid_choices):
        choice = input(prompt).lower()
        while choice not in valid_choices:
            print(f"Escolha inválida! Opções: {', '.join(valid_choices)}")
            choice = input(prompt).lower()
        return choice

    @staticmethod
    def get_character_data():
        name = input("Digite o nome do personagem: ")
        race = ConsoleUi.ask_choice("Escolha a raça (human, elf, dwarf): ", ConsoleUi.VALID_RACES)
        char_class = ConsoleUi.ask_choice("Escolha a classe (warrior, mage, rogue): ", ConsoleUi.VALID_CLASSES)
        distribution = ConsoleUi.ask_choice("Distribuição de atributos (classic, heroic, adventurer): ", ConsoleUi.VALID_DISTRIBUTIONS)

        strong_attr = None
        if distribution == "adventurer":
            strong_attr = ConsoleUi.ask_choice(
                "Escolha o atributo forte (strength, dexterity, constitution, intelligence, wisdom, charisma): ",
                ConsoleUi.VALID_ATTRIBUTES
            )

        return {
            "name": name,
            "race": race,
            "class": char_class,
            "distribution": distribution,
            "strong_attr": strong_attr
        }

    def start(self):
        print("=== Bem-vindo ao Criador de Personagens RPG ===")
        data = ConsoleUi.get_character_data()
        character = CharacterCreationService.CharacterCreationService.create_character(data, repository=self.repository)            
        
        print("\nPersonagem criado com sucesso!")
        print(character)
