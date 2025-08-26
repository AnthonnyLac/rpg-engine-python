import src.application.character_creation as CharacterCreationService

class ConsoleUi:
    def __init__(self, repository):
        self.repository = repository
        self.state = "main_menu"  
        self.current_character = None
        
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
        
    def create_character(self):
        data = ConsoleUi.get_character_data()
        character = CharacterCreationService.CharacterCreationService.create_character(
            data, repository=self.repository
        )
        print("\n✅ Personagem criado com sucesso!")
        self.current_character = character.to_dict()
        self.state = "character_menu"
        return character

    def load_character(self):
        name = input("Digite o nome do personagem para carregar: ")
        data = self.repository.load("character", name)
        if data:
            print("\n📂 Personagem carregado com sucesso!")
            self.current_character = data
            self.state = "character_menu"
            return data
        else:
            print("\n⚠️ Nenhum personagem encontrado com esse nome.")
            return None

    def list_characters(self):
        characters = self.repository.list("character")
        if characters:
            print("\n📜 Personagens cadastrados:")
            for c in characters:
                print(f"- {c['name']} ({c['race']} {c['class']})")
        else:
            print("\n⚠️ Nenhum personagem criado ainda.")
            
    def start(self):
        while True:
            if self.state == "main_menu":
                self.show_main_menu()
            elif self.state == "character_menu":
                self.show_character_menu()
            else:
                break  

    def show_main_menu(self):
        print("\n=== Menu Principal ===")
        print("1 - Criar personagem")
        print("2 - Carregar personagem")
        print("3 - Listar personagens")
        print("4 - Sair")
        choice = input("Escolha: ")

        if choice == "1":
            self.create_character()
        elif choice == "2":
            self.load_character()
        elif choice == "3":
            self.list_characters()
        elif choice == "4":
            print("👋 Saindo...")
            self.state = "exit"
        else:
            print("Opção inválida!")

    def show_character_menu(self):
        print(f"\n=== Olá, {self.current_character['name']}! ===")
        print("1 - Listar atributos")
        print("2 - Voltar ao menu principal")
        choice = input("Escolha: ")

        if choice == "1":
            self.list_attributes()
        elif choice == "2":
            self.current_character = None
            self.state = "main_menu"
        else:
            print("Opção inválida!")
    
    def list_attributes(self):
        attrs = self.current_character.get("attributes", {})
        print("\n🧬 Atributos do personagem:")
        for k, v in attrs.items():
            print(f"- {k.capitalize()}: {v}")