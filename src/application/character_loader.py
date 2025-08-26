# src/application/character_loader.py

class CharacterLoaderService:
    @staticmethod
    def load_character(name: str, repository):
        data = repository.load("character", key=name)
        if not data:
            return None
        return data
