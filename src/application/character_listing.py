class CharacterListingService:
    @staticmethod
    def list_characters(repository):
        characters = repository.list("character")
        if not characters:
            return []
        return characters
