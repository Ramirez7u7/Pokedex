from flask import Blueprint, request, jsonify
from app.schemas.pokemon_favorite_schema import PokemonFavoriteSchema
from marshmallow import ValidationError
from app.models.factory import ModelFactory
from bson import ObjectId
from app.tools.response_manager import ResponseManager
from flask_jwt_extended import jwt_required, get_jwt_identity



bp = Blueprint("Favorite_Pokemons",__name__, url_prefix="/Favorite-Pokemons")
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
        data = PokemonFavoriteSchema_Schema.load(data)
        created_pokemon_favorite = PokemonFavorites_model.create(data)
        return RM.success({"_id":PokemonFavorites_model})
    except ValidationError as err:
        print(err)
        return RM.error("Es necesario datos")

@bp.route("/<string:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    PokemonFavorites_model.delete(ObjectId(id))
    return RM.success("pokemon eliminado, uno menos")

@bp.route("/", methods=["GET"])
@jwt_required()
def get_all(user_id):
    user_id = get_jwt_identity()
    data = PokemonFavorites_model.find_all()
    return RM.success(data)














