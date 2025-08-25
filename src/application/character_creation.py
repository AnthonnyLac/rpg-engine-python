# src/application/character_creation.py
from src.domain.factories.character_factory import CharacterFactory

class CharacterCreationService:
    @staticmethod
    def create_character(data: dict, repository=None):
        # Cria o personagem usando a factory
        character = CharacterFactory.create(
            data["name"],
            data["race"],
            data["class"],
            data["distribution"],
            data.get("strong_attr")
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
