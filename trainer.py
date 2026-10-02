from xmlrpc.client import INVALID_ENCODING_CHAR

from moves import moves
from pokemon import Pokemon #precisa importar o pokemon pra comparar se um item recebido é um pokemon realmente.
from pokemoncentral import create_pk, random_iv, random_ev, random_nature
from pokedex import pokedex

import random

class Trainer:
    def __init__(self, nick):
        self.nick = nick
        self.team = []
        self.money = 1000

        self.box = []

        self.npc_battle_requests = []

    def choice_move(self, pokemon): 
        selected = random.choice(pokemon.moves)
        return selected

    def choice_turn_action(self):
        while True:
            #actions = ["attack", "run", "capture", "switch"]

            params = {
                "action" : "attack",
                "move" : self.choice_move(self.team[0])
            }

            return params



    def receive_pokemon(self, pokemon): #pokemon tem que ser um membro da classe pokemon
        assert isinstance(pokemon, Pokemon), f"erro, {pokemon} não é um pokemon"

        pokemon.update_stats() #aí todo o bagulho de raça tem que acontecer dentro desse refresh que vai servir tanto pra curar quanto pra atualizar. E o stat de hp tem que guardar o max e o atual.

        if len(self.team) < 6:
            bag = self.team
            bag.append(pokemon) #usar str no lugar do id claramete não tá funcionando.
        else:
            bag = self.box
            bag.append(pokemon)

        pkindex = len(bag) - 1

        bag[pkindex].teamindex = pkindex + 1 #funciona mas esse nome teamindex não é muito bom, devia ser bagindex
        bag[pkindex].iswild = False
        bag[pkindex].owner_name = self.nick

    def get_first_pk(self):
        return self.team[0]

        

    def swap_pokemon(self, slot1, slot2): #slot1 e 2 tem que ser números de 1 a 6
            
        if 0 < slot1 <= 6 and 0 < slot2 <= 6: #arrumar o tratamento dos slots.
                
            slot1pk = self.team[slot1-1]
            slot2pk = self.team[slot2-1]

            slot1pk.teamindex = slot2
            slot2pk.teamindex = slot1 #tem que fazer o pk saber o index e trocar a arquitetura antiga de dict

            self.team[slot1-1] = slot2pk
            self.team[slot2-1] = slot1pk

    def battle_swap_pokemon(self): #####################################################
        isalivereturn = self.isalive()
        if isalivereturn[0]:
            self.swap_pokemon(1, random.choice(self.isalive()[2]).teamindex)
        else:
            print("não há pokemons vivos para serem trocados.")

    def isalive(self):
        alivepk_quantity = 0
        alivepk = []
        for pokemon in self.team:
            if pokemon.stats["hp"] > 0:
                alivepk_quantity +=1
                alivepk.append(pokemon)

        if alivepk_quantity > 0:
            return True, alivepk_quantity, alivepk
        else:
            return False, alivepk_quantity, alivepk

    def able_to_battle(self):
        alive = False
        for pokemon in self.team:
            if pokemon.stats["hp"] > 0:
                alive = True
                break
        return alive

class Player(Trainer):

    def __init__(self, nick):
        super().__init__(nick)

        self.money = 1000
        self.inventory = {
            "pokeball" : 0
        }
        self.triggers =  {

        }

    def choice_turn_action(self):
        while True:
            actions = ["attack", "run", "capture", "switch"]
            print(actions)
            action = input("selecione uma ação entre as citadas acima. ")
            if action in actions:

                params = {
                    "action" : action
                }

                if action == "attack":
                    params["move"] = self.choice_move(self.team[0])
                elif action == "capture":
                    pass

                return params

    def choice_move(self, pokemon):

        print(pokemon.moves)

        selected_move = input("Digite o nome ou o número de um movimento do seu pokemon. ")

        if selected_move in pokemon.moves:
            return selected_move
        else:
            while True:
                try:
                    selected_move_number = int(selected_move)
                except ValueError:
                        print("Escolha um número para seu movimento. ")

                if 0 < selected_move_number <= len(pokemon.moves): #de 1 a 4, quem controla isso é o appendmove e removemove do player.
                    return pokemon.moves[selected_move_number-1]
                else:
                    print("Escolha um índice de movimento entre 1 e 4. ")

    def choice_pokemon(self): #retorna o index, não o pokemon

        while True:
            try:
                selected = int(input("escolha um número do index de algum pokemon do seu time"))
                if 1<= selected <= len(self.team):
                    return selected
            except ValueError:
                print("escolha um número inteiro válido")

    def choice_alive_pokemon(self):
        if self.isalive()[0]:
            while True:
                choiced = self.choice_pokemon()
                if self.team[choiced-1].stats["hp"] > 0:
                    return choiced
                else:
                    print("erro, escolha um pokemon vivo.")

    def battle_swap_pokemon(self):
        self.swap_pokemon(1, self.choice_alive_pokemon())

    def get_valid_input(self, valid):
        assert isinstance(valid, list)
        while True:
            print(f"comandos válidos: {valid}")
            command = input()
            if command in valid:
                return command

    def receive_item(self, item, quantity):
        assert isinstance(item, str)
        try:
            self.inventory[item] += quantity
        except IndexError:
            self.inventory[item] = quantity

    def remove_item(self, item, quantity):
        assert isinstance(item, str)
        try:
            if self.inventory[item] >= quantity:
                self.inventory[item] -= quantity
                return
        except IndexError:
            pass
        print(f"erro, player não possui {item} o suficiente para ser removido.")



    def start_adventure(self):
        starter = self.get_valid_input(["bulbasaur", "squirtle", "charmander"])
        self.receive_pokemon(create_pk(starter, 5))


def create_trainer(nick, team):
    assert isinstance(team, list)
    assert 0 <= len(team) <= 6 #vou colocar <= no início porque, vai que eu queira criar um trainer sem pokemon.

    trainer = Trainer(nick)

    for pokemon in team:
        assert isinstance(pokemon, Pokemon)
        trainer.receive_pokemon(pokemon)

generics_ivs = {
    "easy" : [0, 0, 0, 0, 0, 0],
    "medium" : [20, 20, 20, 20, 20, 20],
    "hard" : [31, 31, 31, 31, 31, 31]
}

def get_best_evs(pokemon=""): #inacabado.
    pass

generics_evs = {
    "easy" : [0, 0, 0, 0, 0, 0],
    "medium" : [42, 42, 42, 42, 42, 42],
    "hard" : get_best_evs("s")
}

trainers_teams = {
    "starters" : {
        "red" : [create_pk("charmander")],
        "green" : [create_pk("bulbasaur")], #eu terminei de escrever só pra perceber que preciso reescever fundindo create_random_pk com create_pk utilizando parâmetros opcionais e os que você não especificar, o script faz aleatório. Vai ficar bem mais bonito, depois eu faço.
        "blue" : [create_pk("squirtle")],
    },
    "kanto" : {
        "kanto gym leaders" : {
            "Brock" : [create_pk("geodude", 10), create_pk("onix", 11)],
            "Misty" : [create_pk("starmie", 15), create_pk("staryu", 14)],
            "Lt.Surge" : [create_pk("pikachu", 20), create_pk("jolteon", 21), create_pk("raichu", 22)],
            "Erika" : [create_pk("victreebel", 23), create_pk("parasect", 23), create_pk("vileplume", 24), create_pk("tangela", 25)],
            "Koga" : [create_pk("beedrill", 23), create_pk("arbok", 23), create_pk("venomoth", 24), create_pk("tentacruel", 25), create_pk("golbat", 25)],
            "Sabrina" : [create_pk("alakazam", 23), create_pk("slowbro", 23), create_pk("hypno", 24), create_pk("exeggutor", 25), create_pk("mr. mime", 25), create_pk("jynx", 25)],
            "Blaine" : [create_pk("flareon", 23), create_pk("ninetales", 23), create_pk("arcanine", 24), create_pk("rapidash", 25), create_pk("magmar", 25), create_pk("charizard", 25)],
            "Giovanni" : [create_pk("sandslash", 23), create_pk("nidoqueen", 23), create_pk("nidoking", 24), create_pk("golem", 25), create_pk("rhydon", 25), create_pk("marowak", 25)],
        },
        "kanto elite 4" : {
            "Bruno" : [create_pk("primeape", 10), create_pk("poliwrath", 10), create_pk("machamp", 10), create_pk("hitmonlee", 10), create_pk("hitmonchan", 10), create_pk("onix", 10), ],
            "Lorelei" : [create_pk("dewgong", 10), create_pk("lapras", 10), create_pk("jynx", 10), create_pk("cloyster", 10), create_pk("blastoise", 10), create_pk("articuno", 10), ],
            "Agatha" : [create_pk("haunter", 10), create_pk("haunter", 10), create_pk("pinsir", 10), create_pk("weezing", 10), create_pk("gengar", 10), create_pk("gengar", 10), ],
            "Lance" : [create_pk("dragonair", 10), create_pk("gyarados", 10), create_pk("dragonair", 10), create_pk("dragonite", 10), create_pk("aerodactyl", 10), create_pk("dragonite", 10), ],
        },
        "kanto champion" : [create_pk("dragonair", 10), create_pk("gyarados", 10), create_pk("mew", 10), create_pk("venusaur", 10), create_pk("blastoise", 10), create_pk("charizard", 10), ],
    },
}