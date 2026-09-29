from moves import moves
from pokedex import pokedex
import random

#todo pokemon é inicialmente wild até ser adicionado ao time ou pc de alguém.

class Pokemon: #alive
    def __init__(self, raceid, level, iv, ev, nature): #moves eu coloco depois, no momento só tackle e quick attack pra todo mundo

        self.race_name = pokedex.pokedex[raceid-1]["name"]
        self.raceid = raceid #lembrando que aqui tamo subtraindo 1 pra usar na table sem estresse. Na verdade eu acho que tá dando erro nisso, não era pra subtrair.

        self.owner_name = "wild"
        self.nick = self.owner_name + " " + self.race_name
        self.catch_rate = 0.5

        self.level = level

        self.nature = nature
        self.teamindex = 0

        self.iswild = True

        self.stats = {
            "hp" : 0,
            "attack" : 0, 
            "defense" : 0,
            "spattack" : 0,
            "spdefense" : 0,
            "speed" : 0,
        }

        self.iv = {
            "hp" : iv[0],
            "attack" : iv[1], 
            "defense" : iv[2],
            "spattack" : iv[3],
            "spdefense" : iv[4],
            "speed" : iv[5],
        }
        self.ev = {
            "hp" : 255,
            "attack" : 120, 
            "defense" : 0,
            "spattack" : 120,
            "spdefense" : 0,
            "speed" : 0,
        }

        self.moves = ["quick attack", "tackle"]

    def choice_move(self): #acho que isso é obsoleto agora.

        if self.iswild:
            move_command = random.choice(self.moves)

            return move_command

    def choice_turn_action(self):
        #choisable = ["attack", "run"] #porque é só isso que o wild faz.
        params = {
            
        }

        params["action"] = "attack"
        params["move"] = self.choice_move()
        return params
            
    def isalive(self):
        if self.stats["hp"] > 0:
            return True
        else:
            return False

    def able_to_battle(self):
        return self.isalive()
        
    def battle_request(self):
        return True
    
    def calculate_hp(self): 

        hp = (((2 * int(pokedex.import_race(self.raceid)['hp']) + self.iv["hp"] + int((self.ev["hp"]/4))) * self.level / 100) + self.level + 10)
        #posso temporariamente carregar toda a pokedex ou posso criar uma função get pra isso.
        return hp

    def calculate_stats(self, stat):
        stat = (((2 * int(pokedex.import_race(self.raceid)[stat]) + self.iv[stat] + int((self.ev[stat]/4))) * self.level / 100) + 5)
        return stat

    def update_stats(self): #isso não deveria estar na dex? Depois eu vejo.

        naturesinfo = {
            "hardy": {
                "increase" : "none",
                "decrease" : "none"
            },
            "docile": {
                "increase" : "none",
                "decrease" : "none"
            },
            "serious" : {
                "increase" : "none",
                "decrease" : "none"
            },
            "bashful": {
                "increase" : "none",
                "decrease" : "none"
            },
            "quirky": {
                "increase" : "none",
                "decrease" : "none"
            },
            "lonely": {
                "increase" : "attack",
                "decrease" : "defense"
            },
            "adamant": {
                "increase" : "attack",
                "decrease" : "spattack"
            },
            "naughty": {
                "increase" : "attack",
                "decrease" : "spdefense"
            },
            "brave": {
                "increase" : "attack",
                "decrease" : "speed"
            },
            "bold": {
                "increase" : "defense",
                "decrease" : "attack"
            },
            "impish": {
                "increase" : "defense",
                "decrease" : "spattack"
            },
            "lax": {
                "increase" : "defense",
                "decrease" : "spdefense"
            },
            "relaxed": {
                "increase" : "defense",
                "decrease" : "speed"
            },
            "timid": {
                "increase" : "speed",
                "decrease" : "attack"
            },
            "hasty" : {
                "increase" : "speed",
                "decrease" : "defense"
            },
            "jolly" : {
                "increase" : "speed",
                "decrease" : "spattack"
            },
            "naive": {
                "increase" : "speed",
                "decrease" : "spdefense"
            },
            "modest": {
                "increase" : "spattack",
                "decrease" : "attack"
            },
            "mild": {
                "increase" : "spattack",
                "decrease" : "defense"
            },
            "rash": {
                "increase" : "spattack",
                "decrease" : "spdefense"
            },
            "quiet": {
                "increase" : "spattack",
                "decrease" : "speed"
            },
            "calm": {
                "increase" : "spdefense",
                "decrease" : "attack"
            },
            "gentle": {
                "increase" : "spdefense",
                "decrease" : "defense"
            },
            "careful": {
                "increase" : "spdefense",
                "decrease" : "spattack"
            },
            "sassy": {
                "increase" : "spdefense",
                "decrease" : "speed"
            }
        }

        self.stats['hp'] = int(self.calculate_hp())

        for key, value in self.stats.items():
            naturemodifier = 1
            if key == naturesinfo[self.nature]["increase"]: #parece que os stats não tão sendo calculados direito.
                naturemodifier = 1.1
            if key == naturesinfo[self.nature]["decrease"]: 
                naturemodifier = 0.9

            self.stats[key] = int(self.calculate_stats(key) * naturemodifier)

    def get_first_pk(self):
        return self