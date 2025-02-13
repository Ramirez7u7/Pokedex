from app import mongo
from app.models.super_class import SuperClass

class User(SuperClass):
    def __init__(self):
        super().__init__("users")
    
    def find_all(self):
        raise NotImplementedError("No es Necesario Todos los Usuarios")
    
    