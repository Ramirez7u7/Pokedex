from marshmallow import Schema, fields, ValidationError


class PokemonFavoriteSchema(Schema):
    name = fields.Str(
        required=True,
        validate=lambda x: len (x) > 0,
        error_messages={
            "required": "El Id de pokemon Es Requerido"
        }   
    )








    