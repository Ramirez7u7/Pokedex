from app.models.pokemon import Pokemon
from app.models.pokemons_favorites import PokemonFavorites
from app.models.users import User

class ModelFactory:
    @staticmethod
    def get_model(collection_name):
        models ={
            "users": User,
            "pokemons": Pokemon,
            "pokemons_favorite": PokemonFavorites
        }
        if collection_name in models:
            return models[collection_name]()
        raise ValueError(f"la coleccion enviado:{collection_name} no existe")