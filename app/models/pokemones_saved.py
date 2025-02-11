from app import mongo

class Pokemon_saved:
    collection = mongo.db.pokemons

    @staticmethod
    def find_all():
        pokemons = Pokemon_saved.collection.find()
        return list(pokemons)
    @staticmethod
    def find_by_id(pokemon_id):
        pokemon = Pokemon_saved.collection.find_one({
            "_id": pokemon_id
        })
        return pokemon
    @staticmethod
    def create(data):
        pokemon = Pokemon_saved.collection.insert_one(data)
        return pokemon.inserted_id
    @staticmethod
    def update(pokemon_id, data):
        pokemon = Pokemon_saved.collection.update_one({"_id":pokemon_id},{
            "$set": data
        })
        return pokemon
    @staticmethod
    def delete(pokemon_id):
        return Pokemon_saved.collection.delete_one({"_id":pokemon_id})

        
