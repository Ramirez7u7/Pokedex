from flask import Blueprint, request
from app.tools.response_manager import ResponseManager
from bson import ObjectId
from app.models.factory import ModelFactory
from flask_jwt_extended import jwt_required





bp = Blueprint("pokemon",__name__,url_prefix="/pokemons")
RM = ResponseManager()
pokemon_model = ModelFactory.get_model("pokemons")

@bp.route("/get/<string:pokemon_id>",methods =["GET"])
@jwt_required()
def get_pokemon(pokemon_id):
    pokemon = pokemon_model.find_by_id(ObjectId(pokemon_id))
    return RM.success(pokemon)

@bp.route("/",methods=["GET"])
@jwt_required()
def get_all():
   data = pokemon_model.find_all()
   return RM.success(data)