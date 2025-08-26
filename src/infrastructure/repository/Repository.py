from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def save(self, entity_type: str, entity_data: dict):
        pass

    @abstractmethod
    def load(self, entity_type: str, key: str) -> dict:
        pass

    @abstractmethod
    def list(self, entity_type: str) -> list[dict]:
        """
        Lista todas as entidades de um tipo.
        Retorna uma lista de dicionários.
        """ 
        pass