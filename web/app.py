from flask import Flask
from web.controllers.character_controller import character_bp

def create_app(repository):

    app = Flask(__name__)
    app.repository = repository
    app.register_blueprint(character_bp)
    return app
