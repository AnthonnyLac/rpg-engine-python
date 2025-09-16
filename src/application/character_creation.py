from src.domain.factories.character_factory import CharacterFactory

class CharacterCreationService:
    @staticmethod
    def create_character(data: dict, repository=None):
        character = CharacterFactory.create(
            data["name"],
            data["race"],
            data["class"],
            data["distribution"],
            data.get("attributes_distribution")
        )
        
        # Se for passado um repositório, salva imediatamente
        if repository:
            # Converter para dict (assumindo que a factory retorna objeto)
            if hasattr(character, "to_dict"):
                repository.save("character", character.to_dict())
            else:
                # Se factory já retorna dict
                repository.save("character", character)
        
        return character

    @staticmethod
    def _validate_attributes(attributes):
        required_attrs = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

        for attr in required_attrs:
            if attr not in attributes or not isinstance(attributes[attr], int):
                return False
            if attributes[attr] < 3 or attributes[attr] > 18:
                return False

        return True

    @staticmethod
    def get_all_characters(repository):
        return repository.get_all_characters()

    @staticmethod
    def get_character_by_id(repository, character_id):
        return repository.get_character_by_id(character_id)
