from flask import Blueprint, request, jsonify
from app.schemas.pokemon_favorite_schema import PokemonFavoriteSchema
from marshmallow import ValidationError
from app.models.factory import ModelFactory
from bson import ObjectId
from app.tools.response_manager import ResponseManager




bp = Blueprint("Favorite_Pokemons",__name__, url_prefix="/Favorite-Pokemons")
RM = ResponseManager()
PokemonFavoriteSchema_Schema = user_Schema()
PokemonFavorites_model = ModelFactory.get_model("pokemons_favorites")



@bp.route("/", methods=["POST"])
def create():
    try:
        data = request.json
        data = PokemonFavoriteSchema_Schema.Validate(data)
        PokemonFavorites_model = PokemonFavorites_model.create(data)
        return RM.succes({"_id":PokemonFavorites_model})
    except ValidationError as err:
        print(err)
        return RM.error("Es necesario datos")

@bp.route("/", methods["DELETE"])
def delete(id):
    PokemonFavorites_model.delete(ObjectId(id))
    return RM.succes("pokemon eliminado, uno menos")

@bp.route("/", methods=["GET"])
def get_all(user_id):
    data = PokemonFavorites_model.find_all()
    return RM.succes(data)














