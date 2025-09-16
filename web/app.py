from flask import Flask
from web.controllers.character_controller import character_bp

def create_app(repository):

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'pool_recycle': 300,
        'pool_pre_ping': True,
    }


    app.repository = repository
    app.register_blueprint(character_bp)
    return app
