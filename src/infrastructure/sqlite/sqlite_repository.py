import sqlite3
import json
from src.infrastructure.repository.Repository import Repository

class SQLiteRepository(Repository):
    def __init__(self, db_file="game.db"):
        self.conn = sqlite3.connect(db_file)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS entities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                entity_type TEXT,
                key TEXT UNIQUE,
                data TEXT
            )
        """)
        self.conn.commit()

    def save(self, entity_type: str, entity_data):
        # Converte objetos do domínio para dict
        if hasattr(entity_data, "to_dict"):
            entity_data = entity_data.to_dict()
            
        key = entity_data["name"]
        
        self.conn.execute(
            "INSERT INTO entities (entity_type, key, data) VALUES (?, ?, ?)",
            (entity_type, key, json.dumps(entity_data))
        )           
        self.conn.commit()  
        
        # Retorna o ID gerado automaticamente
        cursor = self.conn.execute("SELECT last_insert_rowid()")
        return cursor.fetchone()[0]


    def load(self, entity_type: str, key: str) -> dict:
        cursor = self.conn.execute(
            "SELECT data FROM entities WHERE entity_type=? AND key=?",
            (entity_type, key)
        )
        row = cursor.fetchone()
        return json.loads(row[0]) if row else None

    def list(self, entity_type: str):
        cursor = self.conn.execute(
            "SELECT data FROM entities WHERE entity_type=?",
            (entity_type,)
        )
        rows = cursor.fetchall()
        return [json.loads(row[0]) for row in rows]
