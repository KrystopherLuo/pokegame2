class Player:
    def __init__(self, name):
        self.player_name = name
        self.money = 0
        self.PK_team = []
        self.PK_bag = []

class Pokemon:
    def __init__(self):
        self.pokedex_id = 1 #espécie
        self.iv = {
            'hp' : 0,
            'attack' : 0,
            'defense' : 0,
            'sp.attack' : 0,
            'sp.defense' : 0,
            'speed' : 0
        }

        self.ev = {
            'hp' : 0,
            'attack' : 0,
            'defense' : 0,
            'sp.attack' : 0,
            'sp.defense' : 0,
            'speed' : 0
        }

        self.stats = {
            'hp' : 0,
            'attack' : 0,
            'defense' : 0,
            'sp.attack' : 0,
            'sp.defense' : 0,
            'speed' : 0
        }

        self.moves = []



# pokedex_settings = [
#     {
#         'Name' : 'bulbasaur',

#         'type 1' : 'grass',
#         'type 2' : 'poison',

#         'base_stats' : {
#             'hp' : 45,
#             'attack' : 49,
#             'defense' : 49,
#             'sp. atk' : 65,
#             'sp. def' : 65,
#             'speed' : 45,
#         },

#         'moves' : {
#             'egg_moves' : ['bla1', 'bla2', 'bla3', 'bla4'],
#             'moves' : [],
#             'tm_moves' : [],
#         },

#         'ability' : 'clorophill'
#     },
#     {
#         'Name' : 'ivysaur',

#         'type 1' : 'grass',
#         'type 2' : 'poison',

#         'base_stats' : {
#             'hp' : 60,
#             'attack' : 62,
#             'defense' : 63,
#             'sp. atk' : 80,
#             'sp. def' : 60,
#             'speed' : 60,
#         },

#         'moves' : {
#             'egg_moves' : ['bla1', 'bla2', 'bla3', 'bla4'],
#             'moves' : [],
#             'tm_moves' : [],
#         },

#         'ability' : 'clorophill'
#     },
#     {
#         'Name' : 'venusaur',

#         'type 1' : 'grass',
#         'type 2' : 'poison',

#         'base_stats' : {
#             'hp' : 80,
#             'attack' : 82,
#             'defense' : 83,
#             'sp. atk' : 100,
#             'sp. def' : 100,
#             'speed' : 80,
#         },

#         'moves' : {
#             'egg_moves' : ['bla1', 'bla2', 'bla3', 'bla4'],
#             'moves' : [],
#             'tm_moves' : [],
#         },

#         'ability' : 'clorophill'


#     },
# ]

#criar um módulo que guarda todas as funções dos movimentos. No início da batalha, o jogo importa apenas as funções dos movimentos utilizados pelos pokemon
#em campo.
#eu vou ter que saber manipular arquivos externos.