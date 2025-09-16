import os
from src.infrastructure.sqlite.sqlite_repository import SQLiteRepository

def run_ui(ui):
    ui.start()

def main():
    repository = SQLiteRepository("game.db")
    mode = os.getenv("RUN_MODE", "web").lower()

    if mode == "cli":
        # Import lazy para não trazer dependências web no modo CLI
        from src.interface.ConsoleUi import ConsoleUi
        console_ui = ConsoleUi(repository)
        console_ui.start()

    elif mode == "web":
        # Import lazy para não quebrar CLI se Flask não estiver instalado
        from web.app import create_app
        app = create_app(repository)
        app.run(debug=True)

    else:
        raise ValueError(f"Modo inválido: {mode}. Use RUN_MODE=cli ou RUN_MODE=web.")

if __name__ == "__main__":
    main()