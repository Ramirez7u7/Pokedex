from flask import Blueprint, request, jsonify
from app.schemas.pokemon_favorite_schema import PokemonFavoriteSchema
from marshmallow import ValidationError
from app.models.factory import ModelFactory
from bson import ObjectId
from bson.errors import InvalidId
from app.tools.response_manager import ResponseManager
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint("Favorite_Pokemons", __name__, url_prefix="/Favorite-Pokemons")
RM = ResponseManager()
PokemonFavoriteSchema_Schema = PokemonFavoriteSchema()
PokemonFavorites_model = ModelFactory.get_model("pokemons_favorite")




@bp.route("/", methods=["POST"])
@jwt_required()
def create():
    user_id = get_jwt_identity()
    try:
        data = request.json
        data["user_id"] = user_id
        validated_data = PokemonFavoriteSchema_Schema.load(data)
        pokemon_id = PokemonFavorites_model.create(validated_data)
        return RM.success({"_id": str(pokemon_id)})
    except ValidationError as err:
        print(err.messages)
        return RM.error("Los parámetros enviados son incorrectos")

@bp.route("/delete_pokemon/<string:pokemon_id>", methods=["DELETE"])
@jwt_required()
def delete(pokemon_id):
    try:
        pokemon_object_id = ObjectId(pokemon_id)
    except InvalidId:
        return RM.error("ID de Pokémon inválido")

    if not PokemonFavorites_model.find_by_id(pokemon_object_id):
        return RM.error("Pokémon no encontrado")

    PokemonFavorites_model.delete(pokemon_object_id)
    return RM.success("Pokémon eliminado con éxito")

@bp.route("/get", methods=["GET"])
@jwt_required()
def get_all():
    user_id = get_jwt_identity()
    data = PokemonFavorites_model.find_all(user_id)
    return RM.success(data)





