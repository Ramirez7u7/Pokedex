from marshmallow import Schema, fields, ValidationError




class UserSchema(Schema):
    name = fields.Str(
        required=True,
        validate=lambda x: len (x) > 0,
        error_messages={
            "required": "El Nombre es Requerido"
        }   
    )
    password = fields.Str(
        required=True,
        validate=lambda x: len (x) > 0,
        error_messages={
            "required": "La Contraseña es Requerida"
        }   
    )
    email = fields.Email(
        required=True,
        validate=lambda x: "@utma.edu.mx" in x,
        error_messages={
            "required": "El Correo es Requerido"
        }   
    )

    
