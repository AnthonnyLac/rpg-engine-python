# main.py
from src.infrastructure.sqlite.sqlite_repository import SQLiteRepository
from src.interface.ConsoleUi import ConsoleUi

def run_ui(ui):
    ui.start()

def main():
    # Cria repositório concreto (Infrastructure Layer)
    repository = SQLiteRepository("game.db")
    
    # Cria UI passando o repositório
    console_ui = ConsoleUi(repository)
    
    # Roda a UI de forma genérica
    run_ui(console_ui)

if __name__ == "__main__":
    main()
