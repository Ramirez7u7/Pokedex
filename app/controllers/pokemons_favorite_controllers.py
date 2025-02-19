from flask import Blueprint, request, jsonify
from app.schemas.pokemon_favorite_schema import PokemonFavoriteSchema
from marshmallow import ValidationError
from app.models.factory import ModelFactory
from bson import ObjectId

bp = Blueprint("Favorite Pokemons",__name__, url_prefix="/FavoritePokemons")
user_Schema = user_Schema()
user_model = ModelFactory.get_model("pokemons_favorites")

@bp.route("/dalete/<string:pokemon_id>", methods={"DALATE"})
def dalete(pokemons_id):
    pokemons_favorites.delete(ObjectId(poekemons_id))
    return jsonify("Pokemon Eliminado de la Lista")

@bp.route("/get/<string:pokemon_id>", methods={"CREATE"})
def create_pokemon(pokemon_id):
    pokemon = pokemon_favorite.find_by_id(ObjectId(ObjectId))
    return jsonify(pokemon,200)

@bp.route("/get/<string:pokemon_id>", methods={"GET"})
def get_pokemon(pokemon_id):
    pokemon = pokemon_Model.find_by_id(ObjectId(ObjectId))
    return jsonify(user,200)

@bp.route("/get/<string:pokemons_all>", methods={"GET"})
def get_pokemons(pokemon_id):
    pokemons = pokemon_Model.find_by_all(ObjectId(ObjectId))
    return jsonify(user,200)
    