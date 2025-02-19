from app import mongo
from app.models.super_class import SuperClass


class PokemonFavorites(SuperClass):
    def __init__(self):
        super().__init__("pokemons_favorites")




