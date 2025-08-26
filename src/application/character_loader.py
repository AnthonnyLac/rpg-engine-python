# src/application/character_loader.py

class CharacterLoaderService:
    @staticmethod
    def load_character(name: str, repository):
        data = repository.load("character", key=name)
        if not data:
            print(f"⚠️ Personagem '{name}' não encontrado.")
            return None
        return data
