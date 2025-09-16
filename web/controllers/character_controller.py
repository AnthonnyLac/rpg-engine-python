from flask import Blueprint, render_template, request, jsonify, current_app
from src.application.character_creation import CharacterCreationService

character_bp = Blueprint("character", __name__)

# Mantenha as constantes de validação
VALID_RACES = ["human", "elf", "dwarf"]
VALID_CLASSES = ["warrior", "mage", "rogue"]
VALID_DISTRIBUTIONS = ["classic", "heroic", "adventurer"]
VALID_ATTRIBUTES = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]


@character_bp.route("/", methods=["GET"])
def create_character_form():
    return render_template("create_character.html",
                           races=VALID_RACES,
                           classes=VALID_CLASSES,
                           distributions=VALID_DISTRIBUTIONS)


@character_bp.route("/roll-attributes", methods=["POST"])
def roll_attributes():
    try:
        data = request.get_json()
        distribution_style = data.get("distribution")

        if distribution_style not in VALID_DISTRIBUTIONS:
            return jsonify({"error": "Distribuição inválida"}), 400

        # Simulação da rolagem (a lógica real será no frontend)
        # Esta rota pode ser usada para validação se necessário
        return jsonify({"message": "Rolagem deve ser feita no frontend"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@character_bp.route("/create", methods=["POST"])
def create_character():
    try:
        data = request.get_json()

        # Validações
        if not data.get("name"):
            return jsonify({"error": "Nome é obrigatório"}), 400

        if data.get("race") not in VALID_RACES:
            return jsonify({"error": "Raça inválida"}), 400

        if data.get("class") not in VALID_CLASSES:
            return jsonify({"error": "Classe inválida"}), 400

        if data.get("distribution") not in VALID_DISTRIBUTIONS:
            return jsonify({"error": "Distribuição inválida"}), 400

        # Validar atributos
        attributes = data.get("attributes", {})
        for attr in VALID_ATTRIBUTES:
            if attr not in attributes:
                return jsonify({"error": f"Atributo {attr} faltando"}), 400
            if not isinstance(attributes[attr], int) or attributes[attr] < 3 or attributes[attr] > 18:
                return jsonify({"error": f"Atributo {attr} inválido"}), 400

        # Criar personagem usando o service
        character_data = {
            "name": data["name"],
            "race": data["race"],
            "class": data["class"],
            "distribution": data["distribution"],
            "attributes_distribution": attributes
        }

        character = CharacterCreationService.create_character(character_data, current_app.repository)
        character_dict = character.to_dict()

        return jsonify({
            "success": True,
            "character": character_dict,
            "message": "Personagem criado com sucesso!"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@character_bp.route("/characters", methods=["GET"])
def list_characters():
    service = CharacterCreationService(current_app.repository)
    characters = service.get_all_characters()
    return render_template("character_list.html", characters=characters)


@character_bp.route("/character/<int:character_id>", methods=["GET"])
def character_detail(character_id):
    service = CharacterCreationService(current_app.repository)
    character = service.get_character_by_id(character_id)

    if not character:
        return jsonify({"error": "Personagem não encontrado"}), 404

    return render_template("character_detail.html", character=character)