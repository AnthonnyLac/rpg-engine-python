# src/application/character_listing.py

class CharacterListingService:
    @staticmethod
    def list_characters(repository):
        characters = repository.list("character")
        if not characters:
            print("⚠️ Nenhum personagem encontrado.")
            return []
        return characters
