from app import mongo
from app.models.super_class import SuperClass
from bson import ObjectId

class PokemonFavorites(SuperClass):
    def __init__(self):
        super().__init__("pokemons_favorites")
    def update(self, object_id,data):
        raise NotImplementedError("los poekemons no se pueden actualizar")

def find_by_id(self, object_id):
    raise NotADirectoryError("No se pueden encontrar de manera indivudual")
def find_all(self,user_id):
    data = self.collection.find({"user_id": ObjectId(user_id)})
    return data


