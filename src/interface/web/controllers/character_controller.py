from flask import Blueprint, render_template, request, current_app
from src.application.character_creation import CharacterCreationService

character_bp = Blueprint("character", __name__)

@character_bp.route("/", methods=["GET", "POST"])
def create_character():
    if request.method == "POST":
        name = request.form.get("name")
        race = request.form.get("race")
        char_class = request.form.get("char_class")
        distribution = request.form.get("distribution")
        strong_attr = request.form.get("strong_attr") or None

        character = CharacterCreationService.create_character(
            name, race, char_class, distribution, strong_attr
        )

        return render_template("create_character.html", character=character)

    return render_template("create_character.html", character=None)
