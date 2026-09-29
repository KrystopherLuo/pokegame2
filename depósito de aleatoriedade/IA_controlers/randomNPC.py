import random

class IAmanager:
    def __init__(self):
        pass
    def create_ia(self,):
        pass

class IAGenericController:
    def __init__(self):
        pass

    def choice(self, pokemon):
        selected = random.choice(pokemon.moves)
        return selected

    def swap_pokemon(self, trainer): #o npc só escolhe pokemons vivos necessariamente então não é preciso se preocupar com os mortos diferente do player.
        choiced = random.choice(trainer.isalive()[2])
        return choiced.teamindex

    def respond_request(self):
        return True

#IA cyntia = IAmanager.create(IAgeneric, função da cyntia)