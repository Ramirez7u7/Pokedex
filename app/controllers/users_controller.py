from flask import Blueprint, request, jsonify
from app.schemas.UserSchema import UserSchema
from marshmallow import ValidationError
from app.models.factory import ModelFactory
from bson import ObjectId





bp = Blueprint("users",__name__, url_prefix="/users")
user_Schema = user_Schema()
user_model = ModelFactory.get_model("users")

@bp.route("/login",methods=["POST"])
def login():
    data = request.json
    email = data.get("email",None)
    password = data.get("paswword", None)
    if not email or not password:
        return jsonify("Falta Contraseña/Correo")
    user = user_model.get_by_email_password(email,password)
    if not user:
        return jsonify("No existe el usuario", 400)
    return jsonify(user,200)


@bp.route("/register", methods=["POST"])
def register():
    try:
       data = user_Schema.load(request.json)
       user_id = user_model.create(data)
       return jsonify({"user_id":str(user_id)},200)
    except ValidationError as err:
        return jsonify("Los Parametros enviados son incorrectos",400)

@bp.route("/update/<string:user_id>", methods={"PUT"})
def update(user_id):
    try:
        data = user_Schema.load(request.json)
        user = user_model.update(ObjectId(user_id), data)
        return jsonify({"data":user},200)
    except ValidationError as err:
        return jsonify("Los parametros enviados son incorrectos", 400)

@bp.route("/dalete/<string:user_id>", methods={"DALATE"})
def dalete(user_id):
    user_model.delete(ObjectId(user_id))
    return jsonify("Usuarios Eliminado, adios tonoto")

@bp.route("/get/<string:user_id>", methods={"GET"})
def get_user(user_id):
    user = user_model.find_by_id(ObjectId(ObjectId))
    return jsonify(user,200)