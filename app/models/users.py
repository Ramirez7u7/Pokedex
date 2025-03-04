from app import mongo
from app.models.super_class import SuperClass

class User(SuperClass):
    def __init__(self):
        super().__init__("users")
    
    def find_all(self):
        raise NotImplementedError("No es Necesario Todos los Usuarios")
    
    def get_by_email_password(self, email, password):
        user = self.collection.find_one({"email": email, "password": password})
        if user:
            user["_id"] = str(user["_id"])
        return user